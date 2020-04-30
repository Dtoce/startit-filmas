import os
import psycopg2

# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
# Vienkāršam testam var nomainīt šīs vērtības pret konkrētiem lielumiem

ELEPHANT_HOST = os.getenv("ELEPHANT_HOST") # "balarama.db.elephantsql.com"
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME") # "manadb"
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD") # "managaraparole"


def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    dsn = "host={balarama.db.elephantsql.com} dbname={rwqewekt} user={rwqewekt} password={DZmBfUxb47RNJoG_R-jM8GeROdG9ZdDw}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result