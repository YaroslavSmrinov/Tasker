from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv()


class ConfigApp(BaseSettings):
    app_name = os.getenv('APP_NAME')
    db_url = os.getenv('SQLALCHEMY_DB_URL')

    class Meta:
        path_to_env: str = '../.env'

main_settings = ConfigApp()
