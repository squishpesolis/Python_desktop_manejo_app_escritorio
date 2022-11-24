class ConfigurationDataBase:
    def __init__(self, db_server_name: str, db_name: str,db_user: str,db_password: str,env: str) -> None:
        self.db_server_name = db_server_name
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.env = env