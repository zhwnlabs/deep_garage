# Website Komunitas — Satu Halaman

Website komunitas bertema gelap, satu halaman, responsif (desktop & mobile).
Dibuat murni dengan **HTML + CSS + JavaScript** — tanpa library, tanpa build,
tanpa server khusus.

## Cara menjalankan

Pilih salah satu:

1. **Paling gampang:** klik dua kali file `index.html` — terbuka di browser.
2. **Lewat server lokal** (kalau nanti pakai gambar/video dari file sendiri):

   ```bash
   # pakai Python
   python3 -m http.server 8080

   # atau pakai Node
   npx serve .
   ```

   Lalu buka `http://localhost:8080` di browser.

## Cara ganti isi (nama, link, gambar)

Semua teks, link, dan gambar ada di **satu tempat**: objek `CONFIG`
di bagian atas `<script>` (cari komentar `KONFIGURASI UTAMA`).
Tidak perlu menyentuh kode di bawahnya.

```js
const CONFIG = {
  name: "Nama Komunitas",        // nama komunitas
  memberCount: "1.240",          // jumlah member
  bannerUrl: "",                 // URL foto banner (kosong = placeholder abu-abu)
  profileUrl: "",                // URL foto profil bulat
  about: "..." ,                 // paragraf deskripsi komunitas
  links: {
    discord: "https://discord.gg/xxxx",   // tab Discord
    tiktok:  "https://tiktok.com/@xxxx",  // tab TikTok
    news:    "#news"                      // tab News (anchor / URL)
  },
  edits: [                       // 6 kartu Best Edit
    { title: "Judul Edit", editor: "Nama Editor", thumb: "", url: "https://..." },
    // ... 5 lagi
  ]
};
```

### Ganti gambar

Isi `bannerUrl`, `profileUrl`, dan `thumb` pada tiap kartu dengan URL gambar
milikmu, contoh: `"https://situs-saya.com/banner.jpg"`.

Kalau dibiarkan kosong (`""`), website otomatis membuat **placeholder abu-abu**
(berupa SVG, jadi tetap rapi walau offline). Kamu juga bisa menaruh file gambar
di folder yang sama lalu menulis `"banner.jpg"` — asal file-nya ikut di repo.

## Isi halaman

- **Navigasi sticky** di atas: Home (tab aktif, ada garis bawah), Discord,
  TikTok, News. Discord & TikTok dibuka di tab baru.
- **Banner** lebar penuh, tinggi ±320px (250px di mobile).
- **Foto profil bulat** menimpa sebagian bawah banner, nama komunitas di
  sampingnya (di bawah di mobile), jumlah member, tombol **Join** (ke Discord).
- **Deskripsi** singkat tentang komunitas.
- **Best Edit**: grid 3 kolom di desktop, 2 kolom di tablet, 1 kolom di mobile —
  tiap kartu berisi thumbnail, tombol putar, judul edit, nama editor, tombol
  **Lihat**.

## Struktur file

```
index.html      <- seluruh website (HTML + CSS + JS + CONFIG)
README.md       <- panduan ini
CARA-PUSH.md    <- cara menimpa repo GitHub
```

## Warna

Tema gelap diatur di blok `:root` paling atas `<style>`:
`--bg: #0a0a0a`, `--bg-2: #121212`, `--card: #1c1c1c`, `--border: #2a2a2a`,
`--text: #e5e5e5`, `--text-2: #d4d4d4`. Ganti di sana untuk mengubah nuansa
seluruh halaman sekaligus.
