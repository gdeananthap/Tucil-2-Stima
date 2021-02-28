# Tucil 2
Tugas Kecil 2 IF2211 Strategi Algoritma Semester II tahun 2020/2021
Aplikasi sederhana yang dapat menyusun rencana pengambilan kuliah, dengan memanfaatkan algoritma *Decrease and Conquer*. Penyusunan Rencana Kuliah diimplementasikan dengan menggunakan pendekatan *Topological Sorting*. 

Adapun penjelasan algoritma Decrease and Conquer dengan pendekatan Topological Sorting yang digunakan pada aplikasi ini adalah sebagai berikut:
1.	Dari graf berarah semua mata kuliah yang menyatakan hubungan prerequisite antar mata kuliah, hitung semua derajat-masuk pada setiap simpul (mata kuliah). 
2.	*Decrease*: Pilih simpul (mata kuliah) yang memiliki derajat-masuk 0 dan hilangkan simpul tersebut pada graf dan kurangi derajat-masuk dari setiap simpul (mata kuliah) lainnya yang terhubung dengan simpul tersebut. 
3.	*Conquer*: Ulangi langkah 1 dan 2 dengan simpul (mata kuliah) yang tersisa pada graf (DAG) hingga semua simpul pada graf terpilih.

## Requirements
- [Python 3](https://www.python.org/downloads/)

## How To Use
1. Buat file teks yang berisi daftar mata kuliah beserta prasyarat yang harus diambil seorang mahasiswa sebelum mengambil mata kuliah tersebut. Pastikan daftar mata kuliah dan prasyarat yang harus diambil dapat direpresentasikan sebagai DAG (*Directed Acyclic Graph*). Daftar mata kuliah tersebut dituliskan dalam suatu file teks dengan format:
```bash
<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.
.
.
.
```
2. Simpan file teks tersebut ke folder test.
3. Jalankan program 13519026.py pada folder src.
```bash
cd src
py 13519026.py
```
4. Masukkan nama mahasiswa dan file teks
5. Program akan menampilkan susunan rencana kuliah mahasiswa selama 1-N semester pada layar *command line interface* (CLI) dengan 1<=N<=8 tergantung mata kuliah yang disediakan pada file teks yang dibuat. Jika ternyata dibutuhkan lebih dari 8 semester untuk mengambil semua mata kuliah yang disediakan pada file teks yang dibuat, maka hanya akan ditampilkan rencana kuliah selama 8 semester.

## Author
Gde Anantha Priharsena - 13519026