
import mysql.connector
import bcrypt


host="localhost"
user="evo"
password="1234"
database="forumevo"

table="users"

def hashPassword(password):
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashedPassword 

def checkPassword(password, hashedPassword):
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword)


def signUp(name, email, password):
    try:
        data_base = mysql.connector.connect(host=host, user=user, password=password, database=database) 
        cursor = data_base.cursor()

        # Inserindo um novo cliente
        sql = f"INSERT INTO {table} (nome, email, senha) VALUES (%s, %s, %s)"
        val = (name, email, hashPassword(password))
        cursor.execute(sql, val)

        data_base.commit()

        print(cursor.rowcount, "record inserted.")

        data_base.close()
        return True
    except:
        return False

def login(email, password):

    data_base = mysql.connector.connect(host=host, user=user, password=password, database=database) 
    cursor = data_base.cursor()
    
    sql = f"SELECT senha FROM users WHERE email = '{email}';"
    
    cursor.execute(sql)

    # Obtendo os resultados
    myresult = cursor.fetchall()

    passwordStoredHash = myresult[0][0]

    if checkPassword(password=password, hashedPassword=passwordStoredHash.encode('utf-8')):
        print('as senhas batem')
        return True
    else:
        print('as senhas NÂO batem')
        return False