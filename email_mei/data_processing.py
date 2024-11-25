import pandas as pd
def load_and_clean_data(file_path):
    """
    Carrega informações de clientes de um arquivo CSV que possuem 'opcap_pelo_mei'como True.
    
    Remover os dados NaN da coluna "email" e trata os dados da coluna "razao_social".
    """
    try:
        clients_df = pd.read_csv(file_path, encoding='latin1', usecols=['email', 'municipio', 'razao_social', 'opcao_pelo_mei'])
        # Filter for MEI option
        clients_df = clients_df.loc[clients_df['opcao_pelo_mei'] == True, :]
        # Drop rows with NaN in 'email'
        clients_df = clients_df.dropna(subset=['email'])
        clients_df['razao_social'] = clients_df['razao_social'].str.replace(r'[^a-zA-Z\s]', '', regex=True).str.strip()
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
            client_name = row['razao_social']
            client_city = row['municipio']
            client_data = client_email, client_name, client_city
        

        return client_data
    except Exception as e:
        return f"Error during iteration: {e}"