from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Konfigurasi PostgreSQL
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

conn = psycopg2.connect(
    database = db_name, 
    user = db_user, 
    password = db_password, 
    host = db_host, 
    port = db_port
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/peminjaman", methods=["GET", "POST"])
def peminjaman():
    if request.method == "POST":
        nama_peminjam = request.form["nama_peminjam"]
        judul_buku = request.form["judul_buku"]
        tanggal_peminjaman = request.form["tanggal_peminjaman"]

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO peminjaman_buku (nama_peminjam, judul_buku, tanggal_peminjaman) VALUES (%s, %s, %s)",
            (nama_peminjam, judul_buku, tanggal_peminjaman),
        )
        conn.commit()
        cursor.close()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peminjaman_buku")
    peminjaman_buku = cursor.fetchall()
    cursor.close()
    return render_template("peminjaman.html", peminjaman_buku = peminjaman_buku)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)