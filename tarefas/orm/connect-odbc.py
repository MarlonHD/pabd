import psycopg2
from decouple import config

conn = psycopg2.connect(
            host=config('DATABASE_HOST'),
            database=config('DATABASE_NAME'),
            user=config('DATABASE_USER'),
            password=config('DATABASE_PASS')
        )


cur = conn.cursor()

#------------- A -------------
atv = ("BD - Tarefa ODBC",3,"2024-04-21","2024-04-23")
cur.execute("INSERT INTO atividade(descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)", atv)
conn.commit()


#------------- B -------------
cur.execute("UPDATE projeto SET responsavel = %s WHERE codigo = %s", (14, 3))
conn.commit

cur.close()
conn.close()