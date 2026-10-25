# Cara Menimpa Repo Lama dengan Kode Ini

1. Ekstrak ZIP ini ke satu folder, lalu buka terminal **di dalam folder itu**.

2. Jalankan perintah berikut (ganti `USERNAME/REPO` dengan milikmu):

   ```bash
   git init -b main
   git add .
   git commit -m "Timpa dengan website komunitas"
   git remote add origin https://github.com/USERNAME/REPO.git
   git push --force origin main
   ```

   > Kalau repo lama sudah punya remote, cek dulu dengan `git remote -v`.
   > Kalau sudah ada, ganti alamatnya:
   > `git remote set-url origin https://github.com/USERNAME/REPO.git`

3. Kalau branch utama repo lamamu bernama `master`, ganti `main` → `master`
   di perintah `git init` dan `git push`.

**Catatan:** `--force` menimpa seluruh isi **dan riwayat** repo lama dengan
kode ini. Kalau masih ingin menyimpan versi lama, buat backup dulu
(unduh ZIP repo lama dari GitHub).

## Menjalankan setelah di-repo

- Klik dua kali `index.html`, atau
- `python3 -m http.server 8080` lalu buka `http://localhost:8080`

## Kalau mau dipakai di GitHub Pages

1. Push ke branch `main` seperti di atas.
2. Buka repo → **Settings → Pages** → Source: `Deploy from a branch` →
   Branch: `main` / folder `/ (root)` → Save.
3. Website tampil di `https://USERNAME.github.io/REPO/`
