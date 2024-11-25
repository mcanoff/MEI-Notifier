import os
import time
import smtplib
import pandas as pd
import email.message
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta

# Criar a classe que envia os emails
class Email:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send(self, client_email, client_name, client_city, retries=3):
        retries = int(retries)
        for attempt in range(retries):
            try:
                msg = MIMEMultipart()
                msg['From'] = self.sender
                msg['To'] = client_email
                msg['Subject'] = "RECEITA FEDERAL NOTIFICA EXCLUSÃO DE MEIs - Regularize o seu!"
                msg['Cc'] = 'mcanoff16@gmail.com'

                email_body = f"""
                    <!DOCTYPE html>
                    <html lang="pt-BR">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Notificação de Exclusão MEI</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                color: #333;
                                line-height: 1.6;
                                background-color: #f9f9f9;
                                padding: 0;
                                margin: 0;
                            }}
                            .container {{
                                max-width: 600px;
                                margin: 20px auto;
                                background: #ffffff;
                                border: 1px solid #ddd;
                                border-radius: 10px;
                                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                overflow: hidden;
                            }}
                            .header {{
                                background-color: #4CAF50;
                                color: white;
                                text-align: center;
                                padding: 20px;
                                font-size: 1.5em;
                            }}
                            .content {{
                                padding: 20px;
                            }}
                            .content p {{
                                margin-bottom: 15px;
                                text-align: justify; /* Adiciona justificação aos parágrafos */
                            }}
                            .cta {{
                                text-align: center;
                                margin: 20px 0;
                            }}
                            .cta a {{
                                background-color: #4CAF50;
                                color: white;
                                text-decoration: none;
                                padding: 10px 20px;
                                border-radius: 5px;
                                font-weight: bold;
                            }}
                            .cta a:hover {{
                                background-color: #45a049;
                            }}
                            .footer {{
                                background-color: #f1f1f1;
                                text-align: center;
                                padding: 20px;
                                font-size: 0.9em;
                                color: #777;
                            }}
                            .footer p {{
                                margin: 5px 0;
                            }}
                            .footer a {{
                                color: #0056b3;
                                text-decoration: none;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div class="header">
                                Notificação de Exclusão MEI
                            </div>
                            <div class="content">
                                <p>Prezado(a) <strong>{client_name}</strong>,</p>
                                <p>
                                    A Receita Federal enviou uma <strong>NOTIFICAÇÃO DE EXCLUSÃO</strong> para 1,1 milhão de Microempreendedores Individuais em todo o Brasil — e um deles é você.
                                </p>
                                <p>
                                    ⚠ <strong>Atenção:</strong> A exclusão do regime MEI implica no pagamento de mais impostos, custos com contador e uma série de outras obrigações que, se não regularizadas, podem afetar diretamente seu CPF como sócio.
                                </p>
                                <p>
                                    <strong>Mas como regularizar sua situação agora?</strong>
                                </p>
                                <p>
                                    Acesse o <a href="" target="_blank">Portal do MEI</a>, preencha a <strong>DASN-MEI</strong> e faça o envio da declaração.
                                </p>
                                <p>
                                    Simples, não? Mas para empreendedores como você, o tempo vale o dobro... E nós sabemos disso.
                                </p>
                                <p>
                                    Por isso, se você quer ter sua empresa regularizada, entre em contato com nossos especialistas da <strong>MBK MEI</strong>, o braço da MBK - Grupo de Serviços Empresariais focado em otimizar resultados de microempreendedores em <strong>{client_city}</strong>.
                                </p>
                                <p>
                                    Evite complicações: simplifique com a <strong>MBK MEI</strong> e dedique seu tempo ao que realmente importa para o seu negócio.
                                </p>
                                <div class="cta">
                                    <a href="" target="_blank">👉 Chame no WhatsApp</a>
                                </div>
                            </div>
                            <div class="footer">
                                <p><strong>Bruno Fey</strong><br>Diretor - MBK Contabilidade</p>
                                <p>"Simplificando processos burocráticos há 30 anos."</p>
                                <p>Tel: <a href="tel:+5541984443380">(41) 98444-3380</a></p>
                                <p>E-mail: <a href="mailto:contato@mbkcontabilidade.com">contato@mbkcontabilidade.com</a></p>
                                <p>
                                    <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4wH-bUT5TfOrAlZ5z6Qv74MLUwFzmsShtYX7Zw4HuIUWWqn2QushlYpXeySgH_Wx1qoMwv-irw" alt="MBK Logo" width="200">
                                </p>
                                <p style="background-color: #eee; padding: 10px; font-size: 0.8em; font-style: italic; border-radius: 5px;">
                                    Este e-mail é confidencial e destinado apenas ao destinatário. Caso tenha recebido por engano, notifique-nos imediatamente e exclua a mensagem.
                                </p>
                            </div>
                        </div>
                    </body>
                    </html>
                    """

                # anexar arquivos de anexo, caso precise
                caminho_arquivo = r"Anexo/test_file.txt"
                with open(caminho_arquivo, "rb") as arquivo:
                    msg.attach(MIMEApplication(arquivo.read(), Name="Anexo teste"))

                msg.attach(MIMEText(email_body, 'html'))

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

    