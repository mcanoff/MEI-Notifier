import os
from dotenv import load_dotenv
from email_mei.email_sender import Email
from email_mei.data_processing import load_and_clean_data
from email_mei.history import update_history, can_send_email
from email_mei.valid_email import is_valid_email

# Caminho do arquivo
MAIN_DIR = r'C:\Users\miria\OneDrive\Área de Trabalho\mbk-email-mei-projeto'
HISTORY_FILE = os.path.join(MAIN_DIR, "email_history.csv")

# Instanciação do Email
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PWD = os.getenv("PWD")
email_mbk = Email(EMAIL_ADDRESS, PWD)

# Carregar e tratar a base de dados
caminho_arquivo = os.path.join(MAIN_DIR, 'clients', 'base_de_dados_teste.csv')
clients_df = load_and_clean_data(caminho_arquivo)
# corpo_email = email_mbk.load_email_body("BAIXADO")
# email_mbk.send("mcanoff16@gmail.com", "Florianópolis", "Mirian", corpo_email)


if clients_df is None or clients_df.empty:
    print("Falha ao carregar os dados ou DataFrame vazio.")
else:
    # Aqui o código para enviar os e-mails (se houver dados válidos)
    for row in clients_df.itertuples():
        email_cliente = row.email
        municipio = row.municipio
        nome = row.razao_social
        situacao_cadastral = row.descricao_situacao_cadastral.strip()

        if is_valid_email(email_cliente):
            if can_send_email(HISTORY_FILE, email_cliente):
                corpo_email = email_mbk.load_email_body(situacao_cadastral)
                email_mbk.send(email_cliente, municipio, nome, corpo_email)
                update_history(HISTORY_FILE, email_cliente)