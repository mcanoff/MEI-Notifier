def is_valid_email(email):
    try:
        email = str(email).strip()
        return '@' in email and '.' in email
    except:
        return False