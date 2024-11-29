import os
from dotenv import load_dotenv
from email_mei.email_sender import Email
from email_mei.data_processing import load_and_clean_data
from email_mei.data_processing import display_and_iterate
from email_mei.history import update_history, can_send_email
from email_mei.valid_email import is_valid_email

# Caminho do arquivo
MAIN_DIR = r'C:\Users\miria\OneDrive\Área de Trabalho\mbk-email-mei-projeto'
HISTORY_FILE = os.path.join(MAIN_DIR, "email_history.csv")

caminho_arquivo = os.path.join(MAIN_DIR, 'clients', 'Base_teste_camboriu.csv')
clients_df = load_and_clean_data(caminho_arquivo)
client_data = display_and_iterate(clients_df)
print(client_data)

email_cliente, nome_cliente, cidade_cliente = client_data

if is_valid_email(email_cliente):
     
    if can_send_email(HISTORY_FILE, email_cliente):
        load_dotenv()
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        PWD = os.getenv("PWD")
        email_mbk = Email(EMAIL_ADDRESS, PWD)
        email_mbk.send(client_data)
        update_history(HISTORY_FILE, email_cliente)