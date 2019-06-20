from manager.database.connection import new_connection


def insert(nome, processos):
    db, client = new_connection(nome)

    for processo in processos:
        numero = processo.get('numero')

        if not db.find_one({'numero': numero}):
            db.insert_one(processo)
