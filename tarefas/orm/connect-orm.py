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



with engine.connect() as conn:
    #------------- A -------------
    a = conn.execute(
        atividade_tb.insert().values(descricao='BD - Tarefa ORM', projeto=3, data_inicio='2024-04-22', data_fim='2024-04-23')
    )

    #------------- B -------------
    b = conn.execute(
        projeto_tb.update().values(responsavel=11).where(projeto_tb.c.codigo == 3)
    )
