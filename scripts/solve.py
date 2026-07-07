# Script untuk membuat template jurnal mingguan secara otomatis
# Jalankan dengan: python buat_jurnal.py <nomor_minggu>

import sys
import os
from datetime import date

def buat_template(minggu):
    tanggal_sekarang = date.today().strftime("%d %B %Y")
    nama_file = f"../docs/minggu-{minggu.zfill(2)}.md"
    
    isi_template = f"""# 📝 Jurnal Minggu {minggu}: [Isi Topik Di Sini]

**Tanggal:** {tanggal_sekarang}

## 🧠 Apa yang Saya Pelajari Minggu Ini?
* ...

## 🚧 Kendala yang Dihadapi
* ...

## 💡 Solusi & Eksplorasi
* ...

## 🎯 Target Minggu Depan
* ...
"""
    
    # Membuat file dan menulis template
    with open(nama_file, "w") as file:
        file.write(isi_template)
    print(f"✅ Template jurnal untuk minggu {minggu} berhasil dibuat di {nama_file}!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan perintah: python buat_jurnal.py <angka_minggu>")
    else:
        buat_template(sys.argv[1])
