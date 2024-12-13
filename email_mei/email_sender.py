import os
import time
import smtplib
import pandas as pd
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta

class Email:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password
        self.corp_email_files = {
            'ATIVO': 'ativo.txt',
            'SUSPENSO': 'suspenso.txt',
            'BAIXADO': 'baixado.txt',
            'INAPTO': 'inapto.txt'
        }

    def load_email_body(self, client_situation):
            """
            """
            client_situation = str(client_situation.lower())
            SCRIPT_DIR = r"C:\Users\miria\OneDrive\Área de Trabalho\mbk-email-mei-projeto\email_mei"
            # arquivo_email_body = self.corp_email_files.get(client_situation)
            caminho_email_body = os.path.join(SCRIPT_DIR, f'{client_situation}.txt')
            if os.path.exists(caminho_email_body):
                with open(caminho_email_body , 'r', encoding='utf-8') as file:
                    email_body = file.read()
                    return email_body
            else:
                print(f"Corpo de e-mail não encontrado para a situação: {client_situation}.")
                return None

    def send(self, client_email, client_city, client_name, email_body, retries=3):
        """
        """
        retries = int(retries)
        for attempt in range(retries):
            try:

                msg = MIMEMultipart()
                msg['From'] = self.sender
                msg['To'] = client_email
                msg['Subject'] = "RECEITA FEDERAL NOTIFICA EXCLUSÃO DE MEIs - Regularize o seu!"
                msg['Cc'] = ''

                corpo_email = email_body.format(client_name=client_name, client_city=client_city)

                msg.attach(MIMEText(corpo_email, 'html'))
                # anexar arquivos de anexo, caso precise
                # caminho_arquivo = r"Anexo/test_file.txt"
                # with open(caminho_arquivo, "rb") as arquivo:
                #     msg.attach(MIMEApplication(arquivo.read(), Name="Anexo teste"))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.sender, self.password)
                server.send_message(msg)
                server.quit()
                print(f"E-mail enviado para {client_email}")
                return
            
            except Exception as e:
                print(f"Erro ao enviar e-mail para {client_email}: {e}")
                time.sleep(10)  # Aguarda antes de tentar novamente

    