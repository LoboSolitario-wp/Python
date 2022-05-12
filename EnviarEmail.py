##Abrir Outlook
#from email.message import EmailMessage
#import os

import win32com.client as win32

#criar a integração com outlook
outlook = win32.Dispatch('outlook.application')

#Criar um email
email = outlook.CreateItem(0)

#configurar as informações do seu e-mail
email.to = 'gbrasil@pagseguro.com'
email.Subject = "test"
email.HTMLBody = """
<p>Olá,</p> 
<p>email de teste</p>
"""

email.Send()

print('Email enviado')
