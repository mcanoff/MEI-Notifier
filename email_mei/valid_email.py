def is_valid_email(email):
    """
    Verifica se um endereço de e-mail é válido.

    Parâmetros:
        email (str): Endereço de e-mail a ser validado.

    Retorna:
        bool: True se o e-mail for válido, False caso contrário.
    """
    try:
        email = str(email).strip()
        return '@' in email and '.' in email
    except:
        return False