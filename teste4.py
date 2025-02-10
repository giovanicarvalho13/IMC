from PyQt6 import uic,QtWidgets
from tkinter import messagebox
def calcular_imc():
    nome = tela_imc.lineEdit.text()
    altura = tela_imc.lineEdit_2.text()
    peso = tela_imc.lineEdit_3.text()


    try:

        altura_float = float(altura.replace(',','.')) # Utilizando o 'replace' converte a virgula em '.'
        peso_float = float(peso.replace(',','.'))

        imc = (peso_float/(altura_float ** 2))

        tela_resultado.show()
        tela_resultado.label.setText(f'Olá {nome.capitalize()} !')
        if imc <= 18.5:
            tela_resultado.label_2.setText(f'Seu IMC é de {imc:.2f} e está classificado como magreza')
        elif imc < 24.9:
            tela_resultado.label_2.setText(f'Seu IMC é de {imc:.2f} e está classificado como normal')
        elif imc < 29.9:
            tela_resultado.label_2.setText(f'Seu IMC é de {imc:.2f} e está classificado como sobrepeso')
        else:
            tela_resultado.label_2.setText(f'Seu IMC é de {imc:.2f} e está classificado como obeso')
    except:
        messagebox.showerror('Erro','Digite um valor válido')

#Limpar campos preenchidos
def limpar():   
    tela_imc.lineEdit.setText('')
    tela_imc.lineEdit_2.setText('')
    tela_imc.lineEdit_3.setText('')

def fechar():
    tela_resultado.close()


app = QtWidgets.QApplication([])
tela_imc = uic.loadUi('imcc.ui')
tela_resultado = uic.loadUi('resultado_imc.ui')
tela_imc.pushButton.clicked.connect(calcular_imc)
tela_imc.pushButton_2.clicked.connect(limpar)
tela_resultado.pushButton.clicked.connect(fechar)

tela_imc.show()
app.exec()