import os
from functools import lru_cache
from pydantic import BaseSettings

_VERSION_ = "0.1.0"

###multiple databases-1
class ISettings(BaseSettings):
    db_engine: str = "mysql+pymysql"
    db_host: str = ""
    db_user: str = "root"
    db_password: str = ""
    db_port: int = 3306
    db_database: str = ""

    debug: bool = True

    kakao_rest_key = ""

    @property
    def db_dsn(self):
        dsn = f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"
        return dsn    

class DevelopmentSettings(ISettings):
    pass

class ProductionSettings(ISettings):
    debug = False


###multiple databases-2
class ISettings2(BaseSettings):
    db_engine: str = "mysql+pymysql"
    db_host: str = ""
    db_user: str = "admin"
    db_password: str = ""
    db_port: int = 3306
    db_database: str = ""

    debug: bool = True

    kakao_rest_key = ""

    @property
    def db_dsn(self):
        dsn = f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"
        return dsn    

class DevelopmentSettings2(ISettings2):
    pass

class ProductionSettings2(ISettings2):
    debug = False


@lru_cache()
def get_settings():
    config = os.environ.get("FASTAPI_CONFIG", "default")
    configs = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
        "default": DevelopmentSettings,
    }

    return configs.get(config, DevelopmentSettings)()

@lru_cache()
def get_settings2():
    config = os.environ.get("FASTAPI_CONFIG", "default")
    configs = {
        "development": DevelopmentSettings2,
        "production": ProductionSettings2,
        "default": DevelopmentSettings2,
    }

    return configs.get(config, DevelopmentSettings2)()
