from search.database.connection import new_connection


def insert(nome, processos):
    db, _ = new_connection(nome)

    for processo in processos:

        if not db.find_one({'numero': processo}):
            db.insert_one(processo)
