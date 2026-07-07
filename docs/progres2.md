📝 Jurnal Minggu 2: Anatomi Binary & Executable

🧠 Apa yang Saya Pelajari Minggu Ini?

Definisi Dasar: Saya belajar membedakan antara Binary (kode mesin murni berisi 0 dan 1 yang dieksekusi CPU) dan Executable (file hasil kompilasi berstruktur khusus yang dimuat oleh Sistem Operasi).

Proses Kompilasi: Ternyata kode sumber yang kita tulis tidak langsung jadi .exe. Ada 4 tahap: Preprocessing, Compiling (menjadi Assembly), Assembling (menjadi object file .obj), dan terakhir Linking (menggabungkan library menjadi executable tunggal).

Format & Struktur File: Saya mempelajari format PE (Portable Executable) untuk Windows yang selalu diawali dengan Magic Header "MZ", serta format ELF untuk Linux. Sebuah executable dibagi menjadi beberapa section, seperti .text untuk kode mesin, dan .data untuk variabel.

🚧 Kendala yang Dihadapi

Sesuai saran materi kelas, saya mencoba membuka file .exe sederhana menggunakan Hex Editor (HxD) untuk melihat bentuk mentahnya. Saya berhasil menemukan header "MZ". Namun, saat saya mencoba mencari sebuah nilai variabel integer (misalnya angka 1000 atau dalam hexadecimal adalah 0x000003E8) di bagian .data section, saya kebingungan. Saya mencari teks 00 00 03 E8 tapi tidak ketemu sama sekali, padahal saya yakin nilai itu ada di dalam program.

💡 Solusi & Eksplorasi

Setelah membaca ulang modul bagian "Konsep Penting: Endianness", saya baru menyadari jebakannya. Komputer dengan arsitektur x86/x64 tempat saya bekerja menggunakan sistem Little Endian.

Dalam Little Endian, Byte dengan nilai terkecil (Least Significant Byte) akan disimpan di alamat memori terendah. Jadi, memori tidak menyimpannya sebagai 00 00 03 E8, melainkan dibaca terbalik per-byte menjadi E8 03 00 00. Setelah saya mencari susunan terbalik tersebut di Hex Editor, barulah nilainya ketemu! Ini adalah konsep fundamental yang sangat penting a
