from sqlalchemy import create_engine, text

# Coloque sua string de conexão aqui
engine = create_engine('postgresql://usuario:senha@localhost:5432/seu_banco')

with engine.connect() as conn:
    conn.execute(text("DELETE FROM alembic_version"))
    conn.commit()
    
print("Tabela limpa!")