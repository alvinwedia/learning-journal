eskripsi Materi: Binary & Executable
1. Definisi Dasar
Binary (Biner) adalah representasi data paling dasar yang dipahami oleh prosesor (CPU), yang terdiri dari deretan angka 0 dan 1. Dalam konteks Reverse Engineering, istilah "Binary" sering merujuk pada Machine Code (kode mesin), yaitu instruksi spesifik arsitektur CPU (seperti x86 atau ARM) yang dieksekusi langsung oleh perangkat keras.
Executable adalah sebuah file hasil kompilasi yang memiliki format struktur tertentu sehingga dapat dimuat oleh Sistem Operasi (Operating System) ke dalam memori untuk dijalankan sebagai program.
2. Proses Terbentuknya Executable
Untuk menjadi sebuah file executable, kode sumber (source code) melalui beberapa tahapan:
Preprocessing: Penanganan direktif (seperti #include atau #define).
Compiling: Mengubah kode sumber menjadi bahasa Assembly.
Assembling: Mengubah bahasa Assembly menjadi kode mesin dalam bentuk object file (.obj atau .o).
Linking: Tahap akhir di mana beberapa object file dan library digabungkan menjadi satu kesatuan file executable tunggal.
3. Format File Executable Populer
Setiap sistem operasi memiliki standar struktur file executable yang berbeda (Magic Header):
PE (Portable Executable): Digunakan oleh Windows (Ekstensi .exe, .dll, .sys). Header-nya dimulai dengan karakter MZ.
ELF (Executable and Linkable Format): Digunakan oleh Linux dan sistem berbasis Unix. Header-nya dimulai dengan byte 0x7F 45 4C 46 (.ELF).
Mach-O: Digunakan oleh macOS dan iOS.
4. Struktur Internal Executable
Secara umum, sebuah file executable dibagi menjadi beberapa bagian utama (Sections):
Header: Berisi metadata tentang file (arsitektur CPU, alamat awal instruksi/Entry Point, jumlah section).
.text Section: Berisi instruksi kode mesin yang akan dieksekusi oleh CPU.
.data Section: Berisi variabel global atau statis yang sudah diinisialisasi.
.rsrc Section: Berisi sumber daya tambahan seperti ikon, gambar, atau menu (pada Windows).
5. Konsep Penting: Endianness
Dalam membaca binary, mahasiswa harus memahami bagaimana data disimpan di memori:
Little Endian: Byte dengan nilai terkecil (Least Significant Byte) disimpan di alamat memori terendah. (Contoh: x86/x64).
Big Endian: Byte dengan nilai terbesar (Most Significant Byte) disimpan di alamat memori terendah. (Contoh: Mainframe, beberapa arsitektur RISC).
6. Relevansi dalam Reverse Engineering
Reverse Engineering adalah proses membalikkan file executable (binary) kembali ke bentuk yang dapat dipahami manusia. Karena kode sumber asli biasanya tidak tersedia, praktisi menggunakan alat bantu:
Disassembler: Mengubah binary menjadi bahasa Assembly (Contoh: IDA Pro, Ghidra).
Decompiler: Mencoba mengubah binary kembali ke bahasa tingkat tinggi seperti C/C++ (Contoh: Hex-Rays).
Hex Editor: Digunakan untuk melihat dan memodifikasi file dalam bentuk mentah hexadecimal (Contoh: HxD).
