from sqlalchemy import URL, create_engine
from data.config import Config


def create_new_engine():
    config = Config()
    url_object = URL.create(
        drivername=f'{config.database.dialect}+{config.database.engine}',
        username=config.database.username,
        password=config.database.password,
        host=config.database.host,
        database=config.database.database,
    )
    engine = create_engine(url_object, echo=True)
    return engine