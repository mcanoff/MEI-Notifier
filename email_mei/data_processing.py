import pandas as pd
def load_and_clean_data(file_path):
    """
        Carrega e filtra os dados do arquivo csv informado.
    """
    try:
        # Carregar apenas as colunas necessárias
        clients_df = pd.read_csv(
            file_path,
            encoding='latin1',
            usecols=['email', 'municipio', 'razao_social', 'descricao_situacao_cadastral'],
            quotechar='"',
            escapechar='\\',
            skipinitialspace=True
        )
        
        # Limpar quebras de linha e espaços em branco nas colunas selecionadas
        for col in clients_df.columns:
            clients_df[col] = clients_df[col].astype(str).str.replace('\n', ' ').str.replace('\r', ' ').str.strip()

        return clients_df
    except Exception as e:
        print(f"Erro ao filtrar os dados: {e}")
        return pd.DataFrame()
    
def display_and_iterate(data):
    """
    
    """
    try:
        for index, row in data.iterrows():
            client_email = row['email']
            client_city = row['municipio']
            client_name = row['razao_social']
            client_situation = row['descricao_situacao_cadastral']
            client_data = client_email, client_city, client_name, client_situation
        

        return client_data
    except Exception as e:
        return f"Error during iteration: {e}"