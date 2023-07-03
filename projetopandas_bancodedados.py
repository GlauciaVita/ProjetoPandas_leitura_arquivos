import sqlalchemy
import pandas as pd

from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

dados = pd.read_csv(url)

dados.head()

dados.to_sql('Clientes', engine, index=False)
inspector = inspect(engine)
print(inspector.get_table_names())

query = 'SELECT * FROM clientes'
empregados = pd.read_sql(query, engine)
print(empregados)

vertable = empregados.to_sql('empregados', con=engine, index=False)

vertable1 = pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])
print(vertable1)













