import pandas as pd
import os

def load_and_clean_data(file_path):

    """
    Carrega e limpa dados de um arquivo CSV.

    Parâmetros:
        file_path (str): Caminho para o arquivo CSV.

    Retorna:
        pd.DataFrame: DataFrame com os dados limpos ou vazio em caso de erro.
    """

    if not os.path.exists(file_path): 
        print(f"Arquivo não encontrado: {file_path}")
        return pd.DataFrame()

    try:
        clients_df = pd.read_csv(
            file_path,
            encoding='latin1',  
            quotechar='"',
            escapechar='\\',
            skipinitialspace=True
        )
    
        # Verifica se as colunas de interesse estão presentes
        missing_cols = [col for col in ['email', 'municipio', 'razao_social', 'descricao_situacao_cadastral'] if col not in clients_df.columns]
        if missing_cols:
            print(f"Colunas ausentes no arquivo CSV: {missing_cols}")
            return pd.DataFrame()

        # Filtra as colunas desejadas
        clients_df = clients_df[['email', 'municipio', 'razao_social', 'descricao_situacao_cadastral']]
        
        # Limpar quebras de linha, espaços em branco e caracteres invisíveis nas colunas selecionadas
        for col in clients_df.columns:
            if clients_df[col].dtype == 'object':
                clients_df[col] = clients_df[col].astype(str) \
                    .str.replace('\n', ' ', regex=False) \
                    .str.replace('\r', ' ', regex=False) \
                    .str.strip()

        # Remover números e CPFs da coluna 'razao_social'
        clients_df['razao_social'] = clients_df['razao_social'].str.replace(r'\b\d{11}\b', '', regex=True)
        clients_df['razao_social'] = clients_df['razao_social'].str.replace(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '', regex=True) 
        clients_df['razao_social'] = clients_df['razao_social'].str.replace(r'\d+', '', regex=True)
        clients_df['razao_social'] = clients_df['razao_social'].str.strip()  

        return clients_df

    except Exception as e:
        print(f"Erro ao filtrar os dados: {e}")
        return pd.DataFrame()
