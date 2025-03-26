import os
from dotenv import load_dotenv

class Config:
    """Configuración base común a todos los entornos."""
    # Versión de la aplicación
    VERSION = "1.0.0"

    # Configuración de la base de datos
    load_dotenv()    
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "contactos_db")
    DB_USER = os.getenv("DB_USER")
    DB_HOST = os.getenv("DB_HOST")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_config(env=None):
    return Config

