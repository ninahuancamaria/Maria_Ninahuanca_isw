from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import pymysql
import os

# Cargar variables del .env
load_dotenv()

app = Flask(__name__)

def get_connection():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "maria"),
            password=os.getenv("DB_PASSWORD", "nina2006"),
            database=os.getenv("DB_NAME", "cloudcontacts"),
            port=int(os.getenv("DB_PORT", "3306")),
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=10
        )
        print("✓ Conexión exitosa a la BD")
        return conn
    except Exception as e:
        print("✗ Error de conexión:", e)
        print(f"  Host: {os.getenv('DB_HOST')}")
        print(f"  Usuario: {os.getenv('DB_USER')}")
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_contact", methods=["POST"])
def add_contact():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    telefono = request.form.get("telefono", "").strip()

    if not nombre or not correo:
        return render_template("index.html", mensaje="Error: Nombre y correo son obligatorios", error=True)

    conn = get_connection()
    if conn is None:
        return render_template("index.html", mensaje="Error: No se pudo conectar a la BD", error=True)

    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO contacts (nombre, correo, telefono, fecha_registro)
                     VALUES (%s, %s, %s, NOW())"""
            cursor.execute(sql, (nombre, correo, telefono))
            conn.commit()
        return render_template("index.html", mensaje="✓ Contacto guardado con éxito", error=False)
    except Exception as e:
        return render_template("index.html", mensaje=f"Error al guardar: {e}", error=True)
    finally:
        conn.close()

@app.route("/contacts")
def contacts():
    conn = get_connection()
    if conn is None:
        return "No se pudo conectar a la Base de Datos."

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM contacts ORDER BY fecha_registro DESC")
            data = cursor.fetchall()
        return render_template("contacts.html", contactos=data)
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    print("Iniciando aplicación...")
    app.run(host="0.0.0.0", port=80, debug=True)
