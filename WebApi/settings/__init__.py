import os

def get_secret(secret_name, backup=None):
    return os.getenv(secret_name, backup)

if get_secret('PIPELINE') == 'production':
    from .production import *
else:
    from .development import *