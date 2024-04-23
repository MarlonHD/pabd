from decouple import config
from sqlalchemy import MetaData, Table, create_engine

engine = create_engine(
		url="postgresql://{}:{}@{}:{}/{}".format(
			config("DATABASE_USER"),
			config("DATABASE_PASS"), 
			config("DATABASE_HOST"), 
			config("DATABASE_PORT"), 
			config("DATABASE_NAME")
		)
	)

metadata = MetaData()
metadata.reflect(bind=engine)

projeto_tb = Table('projeto', metadata, autoload_with=engine)
atividade_tb = Table('atividade', metadata, autoload_with=engine)

