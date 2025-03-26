import os
from dotenv import load_dotenv

class Config:
    """Configuración base común a todos los entornos."""
    # Versión de la aplicación
    VERSION = "1.0.0"

    # Configuración de la base de datos
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "contactos_db")
    secret_config = load_dotenv()

def get_config(env=None):
    return Config

