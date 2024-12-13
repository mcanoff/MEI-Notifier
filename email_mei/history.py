import os
import pandas as pd
from datetime import datetime, timedelta

def update_history(history_file, client_email):
    """
    Atualiza o histórico de envio de e-mails.
    
    Se o arquivo de histórico existir, ele é carregado. Caso contrário, um novo arquivo é criado.
    A nova entrada com o email e a data atual é adicionada na última linha do arquivo CSV.
    
    Args:
        client_email (str): O email do cliente a ser registrado no histórico.
    """
    try:
        # Formatar a nova entrada
        now = datetime.now().strftime('%Y-%m-%d')
        new_row = {"Email": client_email, "Data": now}
        
        # Carregar ou criar o DataFrame
        if os.path.exists(history_file) and os.path.getsize(history_file) > 0:
            df = pd.read_csv(history_file)
        else:
            df = pd.DataFrame(columns=["Email", "Data"])
        
        # Adicionar a nova entrada
        df.loc[len(df)] = new_row 
        
        # Salvar o DataFrame atualizado no arquivo
        df.to_csv(history_file, index=False, encoding='utf-8')
        print(f"Registro adicionado ao arquivo: {history_file}")
    except Exception as e:
        print(f"Erro ao atualizar o histórico: {e}")

def can_send_email(history_file, client_email):
    """
    Verifica se é permitido enviar um e-mail para um cliente com base no histórico de envios.

    Parâmetros:
        history_file (str): Caminho para o arquivo CSV contendo o histórico de envios.
        client_email (str): Endereço de e-mail do cliente a ser verificado.

    Retorna:
        bool: True se o envio for permitido, False caso contrário.
    """
    
    # Verifica se o arquivo existe e não está vazio
    if os.path.exists(history_file) and os.stat(history_file).st_size > 0:
        df = pd.read_csv(history_file, encoding='latin1')
    else:
        return True

    # Converte a coluna 'Data' para datetime
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d', errors='coerce') 

    # Define o limite de 30 dias
    date_limit = datetime.now() - timedelta(days=30)

    # Verifica se o email já foi enviado dentro do limite de 30 dias
    if client_email in df['Email'].values:
        last_send_date = df.loc[df['Email'] == client_email, 'Data'].max()
        if last_send_date >= date_limit:
            return False  

    
    return True