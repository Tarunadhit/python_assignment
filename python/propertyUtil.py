class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "DESKTOP-SRA8EHN\SQLEXPRESS"
        database_name = "SISDB"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"


def getPropertyString():
    return None