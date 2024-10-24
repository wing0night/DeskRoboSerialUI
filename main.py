# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
import webbrowser
# for serial communication
import serial
import time

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.set_signals()
        self.initcombobox()
    
    def initcombobox(self):
        self.ui.comChoose.addItem("COM1")
        self.ui.comChoose.addItem("COM2")
        self.ui.comChoose.addItem("COM3")
        self.ui.comChoose.addItem("COM4")
        self.ui.comChoose.addItem("COM5")
        self.ui.comChoose.addItem("COM6")
        self.ui.comChoose.addItem("COM7")
    
    def open_serialPort(self):
        # 设置串口参数
        # 获取 QComboBox 中选中的项
        port = self.ui.comChoose.currentText()  # 串口名称，例如 'COM3' 或 '/dev/ttyS0'
        baudrate = 115200  # 波特率
        bytesize = serial.EIGHTBITS  # 数据位
        parity = serial.PARITY_NONE  # 奇偶校验位
        stopbits = serial.STOPBITS_ONE  # 停止位
        # 打开串口
        self.ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=1)
        print("Serial opened")
    
    def close_serialPort(self):
        # 检查串口是否已经打开
        if self.ser is not None and self.ser.is_open:
            # 关闭串口
            self.ser.close()
            print("Serial closed")
        else:
            print("Serial is not open or is already closed")
    
    # 设置信号与槽
    def set_signals(self):
        self.ui.github.clicked.connect(self.go_to_github)
        self.ui.eye_blink.clicked.connect(self.eye_blink)
        self.ui.eye_sad.clicked.connect(self.eye_sad)
        self.ui.eye_anger.clicked.connect(self.eye_anger)
        self.ui.eye_surprise.clicked.connect(self.eye_surprise)
        self.ui.eye_right.clicked.connect(self.eye_right)
        self.ui.head_center.clicked.connect(self.head_center)
        self.ui.head_nod.clicked.connect(self.head_nod)
        self.ui.head_shake.clicked.connect(self.head_shake)
        self.ui.head_roll.clicked.connect(self.head_roll)
        self.ui.open.clicked.connect(self.open_serialPort)
        self.ui.close.clicked.connect(self.close_serialPort)
    
    # 跳转到 GitHub 查看源代码
    def go_to_github(self):
        url = 'https://github.com/wing0night/DeskRoboSerialUI.git'
        webbrowser.open(url)
    
    def eye_blink(self):
        # # 检查串口是否打开
        # if self.ser.is_open:
        #     print("串口已打开")
        # try:
        # 发送数据
        data_to_send = "eye_blink"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
        # finally:
        #     # 关闭串口
        #     self.ser.close()
        #     print("串口已关闭")
    def eye_sad(self):
        data_to_send = "eye_sad"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def eye_anger(self):
        data_to_send = "eye_anger"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def eye_surprise(self):
        data_to_send = "eye_surprise"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def eye_right(self):
        data_to_send = "eye_right"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def eye_left(self):
        data_to_send = "eye_left"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def head_center(self):
        data_to_send = "head_center"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def head_nod(self):
        data_to_send = "head_nod"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def head_shake(self):
        data_to_send = "head_shake"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)
    def head_roll(self):
        data_to_send = "head_roll"  # 要发送的数据
        self.ser.write(data_to_send.encode())  # 发送数据，需要先编码为字节
        print("数据已发送")
        # 等待一段时间，以便看到发送的数据
        time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
