📝 Pengenalan Assembly & Arsitektur CPU

🧠 Apa yang Saya Pelajari Minggu Ini?

Mempelajari perbedaan fundamental antara bahasa C dan Java, serta mengapa keduanya sangat penting di dunia Reverse Engineering (RE).

Kenapa C Penting? C adalah bahasa yang sangat dekat dengan hardware (low-level). Saat di-compile, kode C langsung berubah menjadi bahasa mesin (native binary seperti .exe). Kebanyakan sistem operasi dan malware ditulis dalam bahasa C/C++. Memahami C berarti memahami bagaimana memori komputer dialokasikan secara manual.

Kenapa Java Penting? Berbeda dengan C, Java di-compile menjadi bytecode (file .class) yang berjalan di atas Java Virtual Machine (JVM). Di RE, membedah aplikasi Java ternyata jauh berbeda pendekatannya dibandingkan membedah aplikasi C.

🚧 Kendala yang Dihadapi

Saat belajar C, saya sangat pusing memahami konsep Pointer dan manual memory management (menggunakan malloc dan free). Di Java, ada Garbage Collector yang otomatis membersihkan memori, tapi saat mencoba menulis kode di C, saya sering kali mendapatkan error "Segmentation Fault" (program crash) karena pointer saya menunjuk ke alamat memori yang salah/tidak valid.

Saya juga sempat kebingungan membayangkan bagaimana kode teks C yang saya tulis bisa dimengerti oleh CPU.

💡 Solusi & Eksplorasi

Untuk mengatasi kebingungan soal pointer C, saya akhirnya menggambar kotak-kotak memori di atas kertas untuk mengilustrasikan alamat memori (memory address).

Saya juga melakukan eksperimen kecil: Saya meng-compile program "Hello World" yang sama menggunakan C dan Java. Saat saya buka file hasilnya di text editor, file .class (Java) masih menyisakan teks-teks nama fungsi yang bisa dibaca, sedangkan file .exe (C) isinya murni karakter acak (binary gibberish). Dari sini saya sadar, membedah program buatan C akan jauh lebih rumit dari Java karena struktur kodenya sudah hancur lebur menjadi bahasa mesin.
