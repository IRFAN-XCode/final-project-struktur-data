# NAMA : IRFAN FATHURROHMAN
# NIM : 24416255201187
# KELAS : IF24E - PROGRAM STUDI TEKNIK INFORMATIKA
# MATKUL : STURKTUR DATA

import csv
import os

kontak = 'kontak.csv'

# Fungsi untuk membaca semua data dari file CSV → ke dalam list of dictionary
def baca_file_csv():
    kontak_list = []
    if not os.path.exists(kontak) or os.stat(kontak).st_size == 0:
        return kontak_list
    with open(kontak, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            kontak_list.append(row)
    return kontak_list

# Fungsi untuk menyimpan list kontak ke file CSV
def save_kontak(kontak_list):
    with open(kontak, mode='w', newline='') as file:
        header = ['Nama', 'Nomor', 'Email']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(kontak_list)

# Menampilkan semua kontak
def tampilkan_kontak():
    kontak_list = baca_file_csv()
    if not kontak_list:
        print("\n Kontak kosong.\n")
    else:
        print("\n=== DAFTAR KONTAK ===")
        print("   Nama - Nomor - Email")
        for i, kontak in enumerate(kontak_list, start=1):
            print(f"{i}. {kontak['Nama']} - {kontak['Nomor']} - {kontak['Email']}")
        print()
# Mencari Kontak
def cari_kontak():
    kontak_list = baca_file_csv()
    if kontak_list:
        cari = input("Masukkan Nama yang dicari: ")
        ditemukan = False  # penanda
        for kontak in kontak_list:
            if kontak['Nama'].lower() == cari.lower():
                print("\nKontak Ditemukan")
                print(f"{kontak['Nama']} - {kontak['Nomor']} - {kontak['Email']}\n")
                ditemukan = True
                break  # keluar dari loop setelah ditemukan
        if not ditemukan:
            print("Kontak tidak ditemukan.\n")
    else:
        print("\nDaftar Kontak Kosong\n")


# Menambah kontak baru
def tambah_kontak():
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor telepon: ")
    email = input("Masukkan Email: ")
    kontak_list = baca_file_csv()

    # Cek duplikat
    for kontak in kontak_list:
        if kontak['Nama'].lower() == nama.lower():
            print("Kontak dengan nama itu sudah ada!\n")
            return

    kontak_list.append({'Nama': nama, 'Nomor': nomor, 'Email' : email})
    save_kontak(kontak_list)
    print("Kontak berhasil ditambahkan.\n")

# Mengubah nomor kontak
def edit_kontak():
    nama = input("Masukkan nama kontak yang ingin diubah: ")
    kontak_list = baca_file_csv()

    for kontak in kontak_list:
        if kontak['Nama'].lower() == nama.lower():
            kontak['Nama'] = input("Masukkan Nama Baru: ")
            kontak['Nomor'] = input("Masukkan nomor baru: ")
            kontak['Email'] = input("Masukkan Email Baru: ")
            save_kontak(kontak_list)
            print("Kontak berhasil diubah.\n")
            return

    print("Kontak tidak ditemukan.\n")

# Menghapus kontak
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    kontak_list = baca_file_csv()

    kontak_baru = [kontak for kontak in kontak_list if kontak['Nama'].lower() != nama.lower()]
    if len(kontak_baru) == len(kontak_list):
        print("Kontak tidak ditemukan.\n")
    else:
        save_kontak(kontak_baru)
        print("Kontak berhasil dihapus.\n")

def main():
    while True:
        print("=== APLIKASI DAFTAR KONTAK ===")
        print("1. Tampilkan Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak")
        print("4. Edit Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_kontak()
        elif pilihan == '2':
            cari_kontak()
        elif pilihan == '3':
            tambah_kontak()
        elif pilihan == '4':
            edit_kontak()
        elif pilihan == '5':
            hapus_kontak()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.\n")
main()