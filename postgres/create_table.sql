CREATE TABLE peminjaman_buku (
    id SERIAL PRIMARY KEY,
    nama_peminjam VARCHAR(255) NOT NULL,
    judul_buku VARCHAR(255) NOT NULL,
    tanggal_peminjaman DATE NOT NULL
);