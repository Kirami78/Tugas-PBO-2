# Definisi kelas Mahasiswa
class Mahasiswa:
    # Konstruktor kelas untuk inisialisasi objek
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Metode untuk menampilkan aktivitas belajar
    def kegiatan(self):
        print(f"{self.nama} sedang silat silat ditengah jalan.")
    # Metode untuk menampilkan aktivitas belajar
    def kegiatan2(self):
        print(f"{self.nama} sedang midioin orang silat tengah jalan.")

# Implementasi penggunaan kelas Mahasiswa
mahasiswa1 = Mahasiswa("Yanto", "123456", "Informatika")
mahasiswa2 = Mahasiswa("Syafira", "654321", "Sistem Informasi")

# Menggunakan metode objek
mahasiswa1.kegiatan()  # Output: Budi sedang belajar.
mahasiswa2.kegiatan2()  # Output: Ani sedang belajar.
