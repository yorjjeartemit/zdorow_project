from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication ,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QWidget,
                        QLineEdit,QPushButton,)

app=QApplication([])
main = QWidget()



class Forld_line(QWidget):
    def line(self):
        layout=QVBoxLayout()
        layout1=QVBoxLayout()
        layout2=QHBoxLayout()
        layout3=QHBoxLayout()
        layout.addWidget(text1)
        layout1.addWidget(text2,Aligment = Qt.Aligncenter)
        layout2.addWidget(text3,Aligment = Qt.Aligncenter)
        layout3.addWidget(text4,Aligment = Qt.Aligncenter)
        layout2.addWidget(text5,Aligment = Qt.Aligncenter)
    def viget(self):
        text1=QLabel("Введіть П.І.Б.")
        text2=QLabel("повних років")
        text3=QLabel("ляжте на спину і заміряйте пульс на 15 секунд Натисніть кнопку 'Почати перший тест' щоб запустити таймер результат запишіть відповідне поле")
        text4=QLabel("виконайте 30 присідань за 45 секунд для цього натисніть кнопку 'начати приідання'щоб запустити лічильник присідань ")
        text5=QLabel("лягте на спину і заміряйте пульс спочатку за перші 15 секунд хвилини без виміру пульсацій езультат запишіть у відповідне поле")
        button=QPushButton("")
        button1=QPushButton("")
        button2=QPushButton("")
        button3=QPushButton("")



app.exec_()
main.show()
