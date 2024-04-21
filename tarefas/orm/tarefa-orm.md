## Resumo ODBC
O ODBC (Open Database Connectivity) é uma API padronizada da indústria que permite que aplicativos acessem e manipulem dados em diferentes bancos de dados utilizando a linguagem de consulta estruturada - SQL. O ODBC funciona como uma camada de abstração entre o aplicativo e o banco de dados subjacente, ele possibilita que desenvolvedores escrevam código independente do banco de dados específico.

Para utilizar o ODBC em Python, o primeiro passo é estabelecer uma conexão com o banco de dados através do método `pyodbc.connect()`, fornecendo os detalhes de conexão necessários. Em seguida, cria-se um cursor para executar consultas SQL e manipular os resultados conforme necessário. Após a conclusão das operações desejadas, é importante confirmar as alterações e, por fim, fechar tanto a conexão quanto o cursor para liberar recursos do sistema.


## Resumo ORM
ORM (Object-Relational Mapping) é uma técnica que permite manipular bancos de dados relacionais usando objetos de programação em vez de consultas SQL diretas. No contexto do Python, a biblioteca SQLAlchemy simplifica essa interação, permitindo definir modelos de dados como classes Python e manipular o banco de dados por meio desses modelos. SQLAlchemy automatiza a tradução entre objetos Python e instruções SQL necessárias para operar nos dados armazenados, simplificando o desenvolvimento de aplicativos, aumentando a portabilidade do código e reduzindo a necessidade de escrever SQL manualmente.
