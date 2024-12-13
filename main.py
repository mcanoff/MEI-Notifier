import time
import os
from dotenv import load_dotenv
from email_mei.email_sender import Email
from email_mei.data_processing import load_and_clean_data
from email_mei.history import update_history, can_send_email
from email_mei.valid_email import is_valid_email
from datetime import datetime, timedelta

# Caminho do arquivo
MAIN_DIR = r'C:\Users\miria\OneDrive\Área de Trabalho\mbk-email-mei-projeto'

# substituir "curitiba" por todas as possíveis cidades.
DATAFRAMES_DIR = os.path.join(MAIN_DIR, 'clients', 'curitiba')
HISTORY_FILE = os.path.join(MAIN_DIR, "email_history.csv")
lista_base_de_dados = os.listdir(DATAFRAMES_DIR)

# Instanciação do Email
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PWD = os.getenv("PWD")
email_mbk = Email(EMAIL_ADDRESS, PWD)


print("Iniciando o envio de e-mails de teste...")
max_emails_per_run = 1000
email_count = 0

for base_de_dados in lista_base_de_dados:
    caminho_arquivo = os.path.join(DATAFRAMES_DIR, f'{base_de_dados}')
    clients_df = load_and_clean_data(caminho_arquivo)
    for row in clients_df.itertuples():
        if email_count >= max_emails_per_run:
            print("Número máximo de e-mails por execução atingido. Parando o envio.")
            break
        
        email_cliente = row.email
        if is_valid_email(email_cliente) and can_send_email(HISTORY_FILE, email_cliente):
            municipio = row.municipio
            nome = row.razao_social
            situacao_cadastral = row.descricao_situacao_cadastral.strip()
            try:
                corpo_email = email_mbk.load_email_body(situacao_cadastral)
                email_mbk.send(email_cliente, municipio, nome, corpo_email)
                update_history(HISTORY_FILE, email_cliente)
                email_count += 1
                time.sleep(5)  # Pausa de 5 segundos entre os envios
            except Exception as e:
                print(f"Erro ao enviar e-mail para {email_cliente}: {e}")
        else:
            if not is_valid_email(email_cliente):
                print(f"Endereço de e-mail inválido: {email_cliente}. Ignorando.")
            else:
                print(f"E-mail já enviado para {email_cliente} nos últimos 30 dias. Ignorando.")
    
print("Envio de e-mails concluído.")