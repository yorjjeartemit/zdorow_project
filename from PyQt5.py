from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication ,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
                        QLineEdit,QPushButton,QWidget)

from instr import*
from my_app2 import*

class MainWin(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.set_appear()
    self.initUI()
    self.connect()
  def set_appear(self):
    self.setWindowTitle(title_txt)
    self.resize(win_width,win_height)
    self.move(win_x,win_y)

  def initUI(self):
    self.hello_txt=QLabel(txt_hello)
    self.button=QPushButton(txt_next)
    self.instructions = QLabel(txt_instructions)
    self.layout=QVBoxLayout()

    self.layout.addWidget(self.hello_txt)
    self.layout.addWidget(self.button)
    self.layout.addWidget(self.instructions)
    self.setLayout(self.layout)

    self.text_timer=QLabel(txt_timer)
    self.text_name=QLabel(txt_name)
    self.text_name=QLineEdit(txt_hintname)
    self.line_age=QLabel(txt_hintage)
    self.line_age=QLabel(text_1)
    self.text_age=QLabel(text_2)
    self.btn_test1=QLabel(text_3)
    self.line_test1=QLabel(txt_sendresults)
    self.text_test2=QLabel(txt_hintest1)
    self.btn_test2=QLabel(txt_hinttest2)
    self.text_test3=QLabel(txt_hinttest3)
    self.btn_test3=QLabel(txt_starttest1)
    self.line_test2=QLabel(txt_starttest2)
    self.line_test3=QLabel(txt_starttest3)
    self.btn_test=QLabel(txt_timer)


    self.l_line=QHBoxLayout()
    self.r_line=QVBoxLayout()
    self.h_line=QVBoxLayout()

    self.r_line.addWidget(self.text_timer, alignment= Qt.Aligncenter)
    self.l_line.addWidget(self.text_name, alignment= Qt.AlignLeft)
    self.l_line.addWidget(self.text_name, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.line_age, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.text_age, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.btn_test1, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.line_test1, alignment= Qt.AligncLeft)
    self.r_line.addWidget(self.text_test2, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.btn_test2, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.test_test3, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.btn_test3, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.line_test2, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.line_test3, alignment= Qt.AlignLeft)
    self.r_line.addWidget(self.btn_test, alignment= Qt.Aligncenter)
    self.h_line.addLayout(self.l_line)
    self.setLayout(self.h_line)

  def connect(self):
    self.btn_next.cliked.conect(self.next_click)

  def next_click(self):
    self.fw=Finalwin()
    self.hide()

  
