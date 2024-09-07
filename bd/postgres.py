import psycopg2
import os

from dotenv import dotenv_values
current_dir = os.path.dirname(os.path.abspath(__file__))
local_path = rf"{current_dir}/.env"
env_vars = dotenv_values(local_path)


class Dbsession():
    def connection(self):

        conn = psycopg2.connect(
            dbname = env_vars.get("POSTGRES_DB"),
            user = env_vars.get("POSTGRES_USER"),
            password = env_vars.get("POSTGRES_PASSWORD"),
            host = env_vars.get("POSTGRES_HOST"),
            port = env_vars.get("POSTGRES_PORT")
        )
        try:
            return conn
        except Exception as error:
            print(error)
            return error
        
create_conexao = Dbsession()



