def hitung_usia():
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    tahun_sekarang = 2024
    usia = tahun_sekarang - tahun_lahir
    print("Usia Anda saat ini adalah", usia, "tahun")

def hitung_sisa_angsuran():
    total_angsuran = int(input("Masukkan total angsuran: "))
    angsuran_terbayar = int(input("Masukkan jumlah angsuran yang sudah dibayarkan: "))
    sisa_angsuran = total_angsuran - angsuran_terbayar
    print("Sisa tahun angsuran yang harus dibayar adalah", sisa_angsuran, "tahun")

def hitung_bmi():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (m): "))
    bmi = berat_badan / (tinggi_badan ** 2)
    print("BMI Anda adalah", bmi)

while True:
    print("\nMenu Pilihan:")
    print("1. Hitung usia saat ini")
    print("2. Hitung sisa tahun angsuran")
    print("3. Hitung berat badan BMI")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan.upper() == "1":
        hitung_usia()
    elif pilihan.upper() == "2":
        hitung_sisa_angsuran()
    elif pilihan.upper() == "3":
        hitung_bmi()
    elif pilihan.upper() == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")


