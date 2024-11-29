import requests
from requests.structures import CaseInsensitiveDict

class Email:
    def __init__(self, api_url, host_smtp, usuario_smtp, senha_smtp, remetente, nome_remetente):
        self.api_url = api_url
        self.host_smtp = host_smtp
        self.usuario_smtp = usuario_smtp
        self.senha_smtp = senha_smtp
        self.remetente = remetente
        self.nome_remetente = nome_remetente

    def send(self, client_data, retries=3):
        retries = int(retries)
        client_email, client_name, client_city = client_data
        
        for attempt in range(retries):
            try:
                # Corpo do e-mail em HTML
                email_body = f"""
                    <!DOCTYPE html>
                    <html lang="pt-BR">
                    <body>
                        <h1>Notificação de Exclusão MEI</h1>
                        <p>Prezado(a) <strong>{client_name}</strong>,</p>
                        <p>A Receita Federal notificou você sobre a exclusão do regime MEI...</p>
                        <p>Para regularizar sua situação, entre em contato conosco!</p>
                        <a href="https://wa.me/554184443380">Clique aqui para falar no WhatsApp</a>
                    </body>
                    </html>
                """

                # Dados da API
                headers = CaseInsensitiveDict()
                headers["Content-Type"] = "application/json"

                data = {
                    "host_smtp": self.host_smtp,
                    "usuario_smtp": self.usuario_smtp,
                    "senha_smtp": self.senha_smtp,
                    "emailRemetente": self.remetente,
                    "nomeRemetente": self.nome_remetente,
                    "emailDestino": [client_email],
                    "assunto": "Notificação de Exclusão MEI - Regularize agora!",
                    "mensagem": email_body,
                    "mensagemTipo": "html",
                    "mensagemEncoding": "quoted-printable",
                    "mensagemAlt": "Notificação de Exclusão MEI",
                }

                # Chamada à API
                response = requests.post(self.api_url, headers=headers, json=data)

                if response.status_code == 200:
                    print(f"E-mail enviado para {client_email}")
                    return
                else:
                    print(f"Erro ao enviar e-mail: {response.status_code}, {response.text}")
                    time.sleep(10)  # Aguarda antes de tentar novamente

            except Exception as e:
                print(f"Erro na tentativa {attempt + 1}: {e}")
                time.sleep(10)  # Aguarda antes de tentar novamente

# Exemplo de uso
# if __name__ == "__main__":
#     email_service = Email(
#         api_url="https://api.xmailer.com.br/send/",
#         host_smtp="HOST-SMTP",
#         usuario_smtp="USUARIO-SMTP",
#         senha_smtp="SENHA-SMTP",
#         remetente="EMAIL-REMETENTE",
#         nome_remetente="NOME-REMETENTE"
#     )

#     # Simulação de envio para um cliente
#     cliente = ("cliente@mail.com", "João Silva", "Curitiba")
#     email_service.send(cliente)
