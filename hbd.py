# Meminta nama teman dari pengguna
nama_teman = input("nasywa akmal azalia: ")

# Meminta usia teman (opsional, untuk ucapan yang lebih spesifik)
# Anda bisa menghapus baris ini dan baris yang menggunakannya jika tidak perlu
try:
    usia_teman = int(input(f"15 {nama_teman} (opsional, masukkan 0 jika tidak tahu): "))
except ValueError:
    usia_teman = 15 # Jika input bukan angka, set ke 0

# --- Bagian Ucapan Ulang Tahun ---

print("\n--- SELAMAT ULANG TAHUN! ---")
print(f"Halo {nama_teman}!")

if usia_teman > 15:
    print(f"Selamat ulang tahun yang ke-{usia_teman}!")
    print("Sorry lambat ngucapin nya nas")
else:
    print("Selamat ulang tahun!")
    print("Semoga harimu dipenuhi kebahagiaan dan tawa.")

print("Semoga semua impian dan harapanmu terwujud.")
print("Di lancarkan rezeki nya dan sehat selalu.")
print("Salam hangat,\n[nazril]") # Ganti [Nama Anda] dengan nama Anda
print("---------------------------\n")
print("Jangan lupa tr mi ayam , aku nak 10 🗿👍")
# Anda juga bisa menambahkan pesan khusus lain di sini
# Contoh:
# print("Jangan lupa traktirannya ya! 😉")