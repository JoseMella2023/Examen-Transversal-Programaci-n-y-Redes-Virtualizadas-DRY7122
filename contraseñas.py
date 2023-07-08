
#	Punto 1 (Importar la gestión de claves y uso de base de datos SQL)

import pyotp, sqlite3, hashlib, uuid


#	Punto 2 (Permitir creación de sitio web utilizando puerto 9500)

from flask import Flask, request

db_name = "Item3.db"

app = Flask(__name__)

@app.route("/")
def index():
	return "Desarrollo Item 3 Exámen Transversal DRY7122.\n"

#	Punto 3 (Almacenar usuarios y contraseñas en hash)

@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
               (USERNAME  TEXT    PRIMARY KEY NOT NULL,
                HASH      TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                  "VALUES ('{0}', '{1}')".format(request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "El usuario ya existe en la base de datos.\n"
    print('username: ', request.form['username'], ' password: ', request.form['password'], ' hash: ', hash_value)
    return "Registro exitoso.\n"


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=9500, ssl_context="adhoc")
