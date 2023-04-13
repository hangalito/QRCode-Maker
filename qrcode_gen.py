"""
   O qrcode_gen é um programa que cria códigos QR
e salva a imagem gerada com o código numa pasta
com o nome QRCode na Pasta Pessoal

    Atualmente só está disponível para sistemas operativos Linux


    Desenvolvedor: Bartolomeu JJ Hangalo
    Data: Abril, 13, 2023
"""

import qrcode
from tkinter import *
from functools import partial
from datetime import datetime as dt
from subprocess import run

# variável global que vai armazenar os dados
global data

# GERAR O CÓDIGO QR
def getData(obj):
    # pegar os dados introduzidos pelo usuário
    data = obj.get()

    # criar isntância de qr
    qr = qrcode.QRCode(version=None, box_size=15, border=1.2)
    
    # adicionar ao qr
    qr.add_data(data)
    
    # gerar uma matrix de qrcode
    qr.make(fit=True)
    
    # criar a imagem com o código qr
    img = qr.make_image(fill_color='black', back_color='white')

    # nome da imagem
    name = str(dt.now())

    # pega o nome do usuário
    user_path = run(['ls', '/home/'], capture_output=True)
    user_name = str(user_path.stdout)
    user_name = user_name.replace('b\'', '')
    user_name = user_name.replace('\\n\'', '')

    # salvar a imagem
    try:
        img.save(rf'/home/{user_name}/QRCode/{name}.png')
    except FileNotFoundError:
        # caso a pasta QRCode não exista, cria a pasta e salva a imagem
        user_path = run(['mkdir', f'/home/{user_name}/QRCode'], capture_output=True)

        img.save(rf'/home/{user_name}/QRCode/{name}.png')

    win.destroy()
    # fechar a janela


# CRIAR A JANELA

# criar uma janela Tk
win = Tk()

# criar uma caixa de texto
data_entry = Entry(win)

# cria o botão para adicionar o texto
button_save_data = Button(win)


# CONFIGURAÇÕES DA JANELA E OS WIDGETS

# titulo da janela
win.title('Gerador de QR Code')

# definir um padding de 6 pixels para adicionar um espaço entre os widgets
win['padx'] = win['pady'] = 6

# adicoinar e posicionar a caixa de texto na janela
data_entry.pack(side=LEFT, anchor=CENTER, expand=1)

# mais configurações da caixa de texto
data_entry.config(font=('Ubuntu', '13'))

# adicoinar e posicionar o botão na janela
button_save_data.pack(side=RIGHT, anchor=CENTER, expand=1)

# mais configurações do botão
button_save_data.config(text='Criar QR',
                        font=('Ubuntu', '11'),
                        command=partial(getData, data_entry))



# executar em loop
win.mainloop()
