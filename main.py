import random
import numpy as np
from PyQt5 import uic,QtWidgets

def sortear():
    numeros = list(np.random.randint(1,60, 6))
    random.shuffle(numeros)
    tela.label.setText(str(numeros[0]))
    tela.label_2.setText(str(numeros[1]))
    tela.label_3.setText(str(numeros[2]))
    tela.label_4.setText(str(numeros[3]))
    tela.label_5.setText(str(numeros[4]))
    tela.label_6.setText(str(numeros[5]))


app=QtWidgets.QApplication([])
tela=uic.loadUi('TelaDeAposta.ui')

tela.pushButton.clicked.connect(sortear)

tela.show()
app.exec()