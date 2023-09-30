from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup)

from random import shuffle

app = QApplication([])
wind = QWidget()
wind.setWindowTitle('вопрос номер 3157')
wind.resize(450, 450)

ques = QLabel('когда прекратятся взрывы домов на вж?')
oi = QPushButton('проверить догадки')
grpa1 = QGroupBox(' ')
a1 = QRadioButton('когда рак на горе свистнет')
a2 = QRadioButton('сегодня')
a3 = QRadioButton('завтра')
a4 = QRadioButton('никогда')

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout()

v_line1.addWidget(a1)
v_line1.addWidget(a3)
v_line2.addWidget(a2)
v_line2.addWidget(a4)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)
grpa1.setLayout(h_line1)

grpa2 = QGroupBox(' ')
otvet = QLabel('когда рак на горе свистнет')
vline1 = QVBoxLayout()

vline1.addWidget(otvet, alignment = Qt.AlignCenter)
grpa2.setLayout(vline1)

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(ques, alignment = Qt.AlignCenter)
hline2.addWidget(grpa1)
hline2.addWidget(grpa2)
hline3.addWidget(oi, alignment = Qt.AlignCenter, stretch=3)

vvline = QVBoxLayout()
vvline.addLayout(hline1)
vvline.addLayout(hline2)
vvline.addLayout(hline3)

grpa2.hide()
wind.setLayout(vvline)

def show_result():
    grpa1.hide()
    grpa2.show()
    oi.setText('Следующий вопрос')

ButGroup = QButtonGroup()
ButGroup.addButton(a1)
ButGroup.addButton(a2)
ButGroup.addButton(a3)
ButGroup.addButton(a4)

def show_r():
    grpa1.show()
    grpa2.hide()
    ButGroup.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    ButGroup.setExclusive(True)
    oi.setText('проверить догадки')

answers = [a1, a2, a3, a4]

def add_ques(ques, a1, a2, a3, a4):
    shuffle(answers)
    ans[0].setText(a1)
    ans[1].setText(a2)
    ans[2].setText(a3)
    ans[3].setText(a4)
    correct.setText(a1)
    show_r()


def check_answer():
    if ans[0].isChecked():
        show_correct('да...ета действительно грустно...')
    elif ans[1].setText(a2) or ans[2].setText(a3) or ans[3].setText(a4):
        show_correct('к сожалению неверно...')
    else:
        show_correct('чо')


def show_correct(res):
    result.setText(res)
    show_result()



def start():
    if 'проверить догадки' == oi.text():
        show_result()
    else:
        show_r()

ques1 = QLabel('скажи пять раз слово кровь..')
a11 = QRadioButton('кровь кровь кровь кровь кровь')
a22 = QRadioButton('нет')
a33 = QRadioButton('что пьет кровь')
a44 = QRadioButton('на какой красный нужно переходить дорогу')
        
otvet1 = QLabel('кровь кровь кровь кровь кровь')
vline11 = QVBoxLayout()

vline11.addWidget(otvet1, alignment = Qt.AlignCenter)
grpa2.setLayout(vline11)

oi.clicked.connect(start)

wind.show()
app.exec_()
