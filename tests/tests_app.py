import requests
import pytest

def test_index():
    url = "http://localhost:5000/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Selamat Datang di Perpustakaan" in response.text

def test_peminjaman():
    url = "http://localhost:5000/peminjaman"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Form Peminjaman Buku" in response.text

def test_peminjaman_submission():
    url = "http://localhost:5000/peminjaman"
    data = {
        "nama_peminjam": "John Doe",
        "judul_buku": "DevOps 101",
        "tanggal_peminjaman": "2023-08-31"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200