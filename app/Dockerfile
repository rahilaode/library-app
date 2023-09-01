# Gunakan image Python sebagai dasar
FROM python:3.8

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke direktori kerja
COPY . .

# Install dependensi
RUN pip install -r requirements.txt

# Expose port yang digunakan oleh server
EXPOSE 5000

# Command untuk menjalankan aplikasi
CMD ["flask", "run", "--host=0.0.0.0"]
