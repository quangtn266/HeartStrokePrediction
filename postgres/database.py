from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import config

connection_url = config.get_setting()
print(connection_url)
engine = create_engine(connection_url, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)