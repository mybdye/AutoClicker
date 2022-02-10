import pyautogui, configparser, time, os
import globalvar as gv
# import faulthandler;faulthandler.enable()

from sys import argv, exit
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator
from ui_AutoClicker import Ui_Dialog

ini_path = os.path.dirname(argv[0])


class MainPage(QtWidgets.QMainWindow):
    _startThread = pyqtSignal()

    def __init__(self):
        super(MainPage, self).__init__()
        self.callUi = Ui_Dialog()
        self.callUi.setupUi(self)
        gv._init()
        # print('ini_path:', ini_path)
        self.config_read()  # 读取配置

        # 日志输出
        self.callUi.textBrowser.textChanged.connect(self.tb_changed)
        # 输入框
        self.callUi.lineEdit_counter.textChanged.connect(self.lineEdit_counter_changed)
        self.callUi.lineEdit_intervalTime.textChanged.connect(self.lineEdit_intervalTime_changed)
        self.callUi.lineEdit_waitFirstTime.textChanged.connect(self.lineEdit_waitFirstTime_changed)
        # 限制输入 int
        self.callUi.lineEdit_counter.setValidator(QIntValidator())
        self.callUi.lineEdit_intervalTime.setValidator(QIntValidator())
        self.callUi.lineEdit_waitFirstTime.setValidator(QIntValidator())
        # 按钮
        self.callUi.pushButton_save.clicked.connect(self.pb_save_clicked)
        self.callUi.pushButton_start.clicked.connect(self.pb_start_clicked)
        self.callUi.pushButton_pause.clicked.connect(self.pb_pause_clicked)
        # 进度条
        self.callUi.progressBar_left.setValue(0)

        self.myT = Runthread()
        self.thread = QThread(self)
        self.myT.moveToThread(self.thread)
        self._startThread.connect(self.myT.run)
        self.myT.signal.connect(self.call_backlog)

    def call_backlog(self, msg):
        counter = int(self.callUi.lineEdit_counter.text())
        self.callUi.textBrowser.append(str(msg[1:][0]))
        self.callUi.progressBar_left.setValue((msg[0] / counter) * 100)

    # textbrowser 日志输出框
    def tb_changed(self):  # 日志输出框自动滚到底部（滚动条100%）
        print('tb changed')
        self.callUi.textBrowser.verticalScrollBar().setValue(self.callUi.textBrowser.verticalScrollBar().maximum())

    def config_read(self):
        try:
            config = configparser.ConfigParser()
            config.read(ini_path + '/config.ini')
            # 输入框
            self.callUi.lineEdit_counter.setText(config.get('DEFAULT', 'lineEdit_counter'))
            self.callUi.lineEdit_intervalTime.setText(config.get('DEFAULT', 'lineEdit_intervalTime'))
            self.callUi.lineEdit_waitFirstTime.setText(config.get('DEFAULT', 'lineEdit_waitFirstTime'))
            # 写全局
            gv.set_value('lineEdit_counter', int(config.get('DEFAULT', 'lineEdit_counter')))
            gv.set_value('lineEdit_intervalTime', int(config.get('DEFAULT', 'lineEdit_intervalTime')))
            gv.set_value('lineEdit_waitFirstTime', int(config.get('DEFAULT', 'lineEdit_waitFirstTime')))
            self.callUi.textBrowser.append('>>> 已读取配置!')
        except:
            self.callUi.textBrowser.append('>>> 未找到配置,请输入!')

    def config_write(self):
        config = configparser.ConfigParser()
        config.read(ini_path + '/config.ini')
        config.set('DEFAULT', 'lineEdit_counter', self.callUi.lineEdit_counter.text())
        config.set('DEFAULT', 'lineEdit_intervalTime', self.callUi.lineEdit_intervalTime.text())
        config.set('DEFAULT', 'lineEdit_waitFirstTime', self.callUi.lineEdit_waitFirstTime.text())
        config.write(open(ini_path + '/config.ini', 'w'))
        self.callUi.textBrowser.append('>>> 配置已保存!')
        self.config_read()

    def lineEdit_counter_changed(self):
        print('lineEdit_counter changed')
        le_counter = self.callUi.lineEdit_counter.text()
        if len(le_counter) > 0:
            gv.set_value('lineEdit_counter', int(le_counter))
            # self.callUi.textBrowser.append('次数：' + str(le_counter))

    def lineEdit_intervalTime_changed(self):
        print('lineEdit_intervalTime changed')
        le_intervalTime = self.callUi.lineEdit_intervalTime.text()
        if len(le_intervalTime) > 0:
            gv.set_value('lineEdit_intervalTime', int(le_intervalTime))
            # self.callUi.textBrowser.append('间隔：' + str(le_intervalTime))

    def lineEdit_waitFirstTime_changed(self):
        print('lineEdit_waitFirstTime changed')
        le_waitFirstTime = self.callUi.lineEdit_waitFirstTime.text()
        if len(le_waitFirstTime) > 0:
            gv.set_value('lineEdit_waitFirstTime', int(le_waitFirstTime))
            # self.callUi.textBrowser.append('等待：' + str(le_waitFirstTime))

    def pb_save_clicked(self):
        print('pb_save clicked')
        self.config_write()
        gv.set_value('flag_save', 1)

    def pb_start_clicked(self, msg):
        print('pb_start clicked')
        if gv.get_value('flag_done') == 1:  # 前一次完成则重新计数
            self.myT.flag = False
            self.stop_thread()
            gv.set_value('lineEdit_counter', int(self.callUi.lineEdit_counter.text()))
            gv.set_value('flag_done', 0)

        if len(self.callUi.lineEdit_counter.text()) and len(self.callUi.lineEdit_intervalTime.text()) and len(
                self.callUi.lineEdit_waitFirstTime.text()) > 0:
            if self.thread.isRunning():
                return
            self.myT.flag = True
            self.thread.start()
            self._startThread.emit()
        else:
            print('请检查配置!')
            self.callUi.textBrowser.append('>>> 请检查配置!')

    def pb_pause_clicked(self):
        print('pb_pause clicked')
        self.callUi.textBrowser.append('>>> 暂停')
        if not self.thread.isRunning():
            return
        self.myT.flag = False
        self.stop_thread()

    def stop_thread(self):
        print('>>> stop_thread')
        if not self.thread.isRunning():
            return
        self.thread.quit()
        self.thread.wait()
        print('>>> stop_thread End')


class Runthread(QtCore.QObject):  # 线程
    signal = pyqtSignal(list)

    def __init__(self):
        super(Runthread, self).__init__()
        self.flag = True

    def __del__(self):
        print('>>>__del__')

    def run(self):
        counter = gv.get_value('lineEdit_counter')
        intervalTime = gv.get_value('lineEdit_intervalTime')
        waitFirstTime = gv.get_value('lineEdit_waitFirstTime')
        print('>>> run Start')
        self.signal.emit([counter, '>>> 开始'])
        if gv.get_value('flag_save') == 1:  # 保存后取最新的counter
            counter = gv.get_value('lineEdit_counter')
            gv.set_value('flag_save', 0)
        for i in range(0, waitFirstTime):  # 首次等待
            print('倒计时(s):', waitFirstTime - i)
            self.signal.emit([counter, '倒计时(s):' + str(waitFirstTime - i)])
            time.sleep(1)

        while self.flag:
            if counter > 0:
                last_mouse_position = pyautogui.position()  # 对比鼠标当前坐标
                time.sleep(0.5)
                current_mouse_position = pyautogui.position()
                if last_mouse_position == current_mouse_position:
                    time.sleep(intervalTime / 1000)  # 点击间隔
                    pyautogui.click(clicks=1, button='left')  # 点击模式，单击/左键
                    counter = counter - 1
                    gv.set_value('lineEdit_counter', counter)
                    print('剩余次数:' + str(counter))
                    x, y = pyautogui.position()
                    self.signal.emit([counter, '点击 x:' + str(x) + ' y:' + str(y) + '\n剩余次数:' + str(counter)])
                else:
                    print('鼠标移动中!\n剩余次数:' + str(counter))
                    self.signal.emit([counter, '鼠标移动中!\n剩余次数：' + str(counter)])
                continue
            else:
                self.signal.emit([0, '>>> 完成'])
                gv.set_value('flag_done', 1)  # 标记点击已完成
                break

        print('>>> run End')
        self.signal.emit([0, '>>> 进程终止'])


# 程序入口
if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    w = MainPage()
    w.show()
    exit(app.exec_())