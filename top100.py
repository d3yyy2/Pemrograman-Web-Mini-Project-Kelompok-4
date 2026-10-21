# Dashboard statis Top 100 YouTube Music Indonesia
# Dataset snapshot chart Mewsek bertanggal 18 Oktober 2026.
# Versi ini tidak memakai kolom jumlah views.
import csv, html
from pathlib import Path

# Untuk mengambil jumlah views video YouTube yang paling relevan, pasang yt-dlp:
# pip install -U yt-dlp
# Pencarian video bersifat perkiraan (video teratas yang cocok), bukan total views
# agregat YouTube Music Charts. Jalankan ulang script dengan internet aktif.

SONGS = [
  [
    "Teh Hijau",
    "Tulus"
  ],
  [
    "Sesi Potret",
    "Ari Lesmana, eńau"
  ],
  [
    "Dunia Yang Nanti",
    "Raim Laode"
  ],
  [
    "Terbelah Jadi Dua",
    "Gloria Jessica, Ade Govinda"
  ],
  [
    "Negoro Angin",
    "Denny Caknan"
  ],
  [
    "Iqro'",
    "Raim Laode"
  ],
  [
    "MMG (My Mine Gueh)",
    "Naykilla"
  ],
  [
    "Kita Lewati Berdua",
    "Overnight"
  ],
  [
    "The One That Got Away",
    "Katy Perry"
  ],
  [
    "Titik Nadir (feat. Monita Tahalea)",
    "Kahitna"
  ],
  [
    "Mutiara",
    "Ipank"
  ],
  [
    "Jangan Paksa Rindu",
    "Ifan Seventeen"
  ],
  [
    "What If I Call",
    "Alex Crichton"
  ],
  [
    "kota ini tak sama tanpamu",
    "Nadhif Basalamah"
  ],
  [
    "Shape of My Heart",
    "Backstreet Boys"
  ],
  [
    "2001x",
    "Adrian Khalif"
  ],
  [
    "Bahagia Lagi",
    "Piche Kota"
  ],
  [
    "Ini Abadi",
    "Perunggu"
  ],
  [
    "Astaga Bercanda",
    "Akbar Chalay, Mingse"
  ],
  [
    "33x",
    "Perunggu"
  ],
  [
    "Great Expectation",
    "SIENNA SPIRO"
  ],
  [
    "Training Season",
    "Dua Lipa"
  ],
  [
    "Sedia Aku Sebelum Hujan",
    "Idgitaf"
  ],
  [
    "Mutiara (Live)",
    "Shinta Gisul"
  ],
  [
    "Penyangkalan",
    "For Revenge"
  ],
  [
    "Menari-nari",
    "Raim Laode"
  ],
  [
    "Salah Apa",
    "Ipank"
  ],
  [
    "Bersenja Gurau",
    "Raim Laode"
  ],
  [
    "Dirantai Digelangi Rindu (feat. Maulana Ardiansyah)",
    "Shinta Gisul"
  ],
  [
    "Risk It All",
    "Bruno Mars"
  ],
  [
    "Dinda (Versi Sped Up)",
    "MASDO"
  ],
  [
    "Terpukau",
    "Astrid Sartiasari"
  ],
  [
    "Nemen (Hiphop Dangdut Version)",
    "NDX A.K.A."
  ],
  [
    "Terbelah Jadi Dua",
    "Yeni Inka"
  ],
  [
    "To Love You More",
    "Céline Dion"
  ],
  [
    "Panas Pela (feat. Vicky Salamor)",
    "Fresly Nikijuluw"
  ],
  [
    "Mutiara (Live)",
    "Difarina Indra Adella, Fendik Adella"
  ],
  [
    "Kaulah Kamuku (feat. Mikha Angelo)",
    "Fatin"
  ],
  [
    "Negoro Angin",
    "Silvy Kumalasari"
  ],
  [
    "Helikopter Turun Ke Padang",
    "Ajeng Febria"
  ],
  [
    "Memori Sekuntum Rindu",
    "Spoon"
  ],
  [
    "1000X",
    "Ghea Indrawari"
  ],
  [
    "Ambon Manise",
    "Toton Caribo, Jacson Seran, Novia Bachmid"
  ],
  [
    "ICONIC HEART",
    "Hearts2Hearts"
  ],
  [
    "Cinderella (feat. Ty Dolla $ign)",
    "Mac Miller"
  ],
  [
    "Die For You (Remix)",
    "The Weeknd, Ariana Grande"
  ],
  [
    "Berapa Kali Kita Akan Saling Memaafkan",
    "Pamungkas"
  ],
  [
    "Amnesia",
    "Al Ghazali"
  ],
  [
    "One Of The Girls",
    "The Weeknd, JENNIE & Lily Rose Depp"
  ],
  [
    "SALAH APA",
    "Laila Ayu, Simpatik Music, Irwan D'Academy"
  ],
  [
    "the cure",
    "Olivia Rodrigo"
  ],
  [
    "Cinta Terlarang",
    "The Virgin"
  ],
  [
    "To the Bone",
    "Pamungkas"
  ],
  [
    "Just Give Me a Reason (feat. Nate Ruess)",
    "P!nk"
  ],
  [
    "Dirantai Digelangi Rindu",
    "Exists"
  ],
  [
    "Laut Kidul (feat. Yesa Oktavia)",
    "Yeni Inka"
  ],
  [
    "Dear God",
    "Avenged Sevenfold"
  ],
  [
    "Sekian, Terima Kasih",
    "Lealona, The Jeblogs"
  ],
  [
    "Percuma",
    "Mahalini"
  ],
  [
    "DIRANTAI DIGELANGI RINDU",
    "Laila Ayu, Simpatik Music"
  ],
  [
    "Siapa Di Hatimu",
    "Rahmat Ekamatra"
  ],
  [
    "BAD",
    "ATEEZ"
  ],
  [
    "Die On This Hill",
    "SIENNA SPIRO"
  ],
  [
    "Heaven",
    "Bryan Adams"
  ],
  [
    "Tak Semudah Hompimpa",
    "Nabila Taqiyyah"
  ],
  [
    "Dirantai Digelangi Rindu (feat. Yesa Oktavia)",
    "Yeni Inka"
  ],
  [
    "So Far Away",
    "Avenged Sevenfold"
  ],
  [
    "Helikopter Turun Ke Padang",
    "Sabrinaaa"
  ],
  [
    "Merry Christmas, Please Don't Call",
    "Bleachers"
  ],
  [
    "Wonderwall",
    "Oasis"
  ],
  [
    "MUTIARA (Live)",
    "Laila Ayu, Irwan Krisdiyanto, Simpatik Music"
  ],
  [
    "Demi Cinta",
    "Kerispatih"
  ],
  [
    "Tulang dan Nadi",
    "Tiara Andini"
  ],
  [
    "Adu Pandang",
    "Rizky Febian"
  ],
  [
    "MUTIARA (Ska Reggae Version)(Live)",
    "Maulana Ardiansyah"
  ],
  [
    "Pure",
    "SIENNA SPIRO"
  ],
  [
    "Mutiara",
    "Ajeng Febria"
  ],
  [
    "Masing Masing",
    "Ernie Zakri, Ade Govinda"
  ],
  [
    "Sedikit Lebih Lama",
    "Piche Kota"
  ],
  [
    "Ain't In LA",
    "ADÉLA"
  ],
  [
    "Rindiani",
    "Slam"
  ],
  [
    "Laskar Cinta Chapter One",
    "Dewa 19"
  ],
  [
    "Negoro Angin",
    "Niken Salindry"
  ],
  [
    "Lemon Tang",
    "Hearts2Hearts"
  ],
  [
    "Creep",
    "Radiohead"
  ],
  [
    "hate that i made you love me",
    "Ariana Grande"
  ],
  [
    "One More Night",
    "Maroon 5"
  ],
  [
    "Gadis Manis Kalimantan",
    "DUO ZIZI (Rizi & Zira)"
  ],
  [
    "Save Your Tears",
    "The Weeknd"
  ],
  [
    "Ku Tak Bisa",
    "Slank"
  ],
  [
    "Sial",
    "Mahalini"
  ],
  [
    "Those Eyes",
    "New West"
  ],
  [
    "Wish You Were Here",
    "Neck Deep"
  ],
  [
    "Bounce & Pa Bkb",
    "Vian DTM"
  ],
  [
    "Aishiteru 3",
    "Zivilia"
  ],
  [
    "ONCOM GONDRONG",
    "Ade Astrid"
  ],
  [
    "Timeless",
    "The Weeknd, Playboi Carti"
  ],
  [
    "Sign of the Times",
    "Harry Styles"
  ],
  [
    "Dirantai Digelangi Rindu",
    "Ajeng Febria"
  ],
  [
    "Moth To A Flame",
    "Swedish House Mafia & The Weeknd"
  ]
]

# Genre bersifat kategorisasi umum/perkiraan berdasarkan lagu dan artis;
# beberapa lagu dapat masuk ke lebih dari satu genre.
def tentukan_genre(title, artist):
    a = artist.lower()
    t = title.lower()
    if any(x in a for x in ["hearts2hearts", "ateez"]): return "K-pop"
    if any(x in a for x in ["ndx a.k.a.", "vian dtm", "naykilla", "akbar chalay", "mingse"]): return "Hip-hop / Dangdut" if "dangdut" in t or "ndx" in a else "Hip-hop / Pop"
    if any(x in a for x in ["denny caknan", "shinta gisul", "ipank", "silvy kumalasari", "ajeng febria", "difarina indra", "fendik adella", "laila ayu", "irwan d'", "yeni inka", "fresly nikijuluw", "sabrinaaa", "maulana ardiansyah", "niken salindry", "ade astrid", "duo zizi", "vian dtm"]): return "Dangdut / Koplo"
    if any(x in a for x in ["avenged sevenfold", "for revenge", "oasis", "radiohead", "neck deep", "slank", "dewa 19", "perunggu", "maroon 5", "bleachers"]): return "Rock / Alternative"
    if any(x in a for x in ["swedish house mafia"]): return "EDM / Dance"
    if any(x in a for x in ["the weeknd", "playboi carti", "mac miller", "adrian khalif", "ariana grande"]): return "R&B / Pop"
    if any(x in a for x in ["katy perry", "dua lipa", "bruno mars", "céline dion", "backstreet boys", "p!nk", "olivia rodrigo", "harry styles", "bryan adams", "sienna spiro", "adéla", "new west"]): return "Pop Internasional"
    if any(x in a for x in ["raim laode", "tulus", "gloria jessica", "ade govinda", "kahitna", "ifan seventeen", "nadhif basalamah", "piche kota", "overnight", "idgitaf", "fatin", "astrid sartiasari", "ghea indrawari", "pamungkas", "mahalini", "the virgin", "tak semudah", "nabila taqiyyah", "tiara andini", "rizky febian", "ernie zakri", "zivilia", "kerispatih", "slam", "exists"]): return "Pop Indonesia"
    if any(x in a for x in ["toton caribo", "jacson seran", "novia bachmid"]): return "Pop Timur"
    if any(x in a for x in ["masdo", "spoon"]): return "Pop / Rock Melayu"
    if any(x in a for x in ["alex crichton"]): return "Pop / Indie"
    return "Pop / Belum diverifikasi"

OUT_HTML = "dashboard_top100_youtube_music_tanpa_views.html"
OUT_CSV = "top100_youtube_music_indonesia_tanpa_views.csv"

# Validasi: tepat 100 peringkat, dari 1 sampai 100.
assert len(SONGS) == 100, f"Dataset harus 100 lagu, sekarang {len(SONGS)}"
rows = [{"peringkat": i, "judul_lagu": title, "artis": artist,
         "genre": tentukan_genre(title, artist),
         "sumber_chart": "https://mewsek.com/charts/youtube-music/id"} for i, (title, artist) in enumerate(SONGS, 1)]

with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader(); writer.writerows(rows)

trs = "\n".join(f'<tr><td><span class="rank">{r["peringkat"]:02d}</span></td><td><b>{html.escape(r["judul_lagu"])}</b></td><td>{html.escape(r["artis"])}</td><td>{html.escape(r["genre"])}</td><td><a target="_blank" href="https://music.youtube.com/search?q={(r["judul_lagu"] + " " + r["artis"]).replace(" ", "+")}">Putar ↗</a></td></tr>' for r in rows)
page = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>NADA — YouTube Music Top 100 Indonesia</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;color:#17352d;background:linear-gradient(135deg,#eaf8e8,#f8f6e9 48%,#d7f3e7);min-height:100vh}}.wrap{{max-width:1240px;margin:auto;padding:30px 20px 60px}}.top{{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:22px}}.brand{{font-weight:900;letter-spacing:2px;color:#176b4d}}.pill{{border-radius:99px;background:#d5f3b7;padding:9px 14px;color:#245d3e;font-size:12px;font-weight:800}}.hero{{padding:38px;border-radius:28px;color:white;background:linear-gradient(115deg,#103d31,#13845f 52%,#9acb43);box-shadow:0 20px 50px #124c3526;position:relative;overflow:hidden}}.hero:after{{content:'♫';position:absolute;right:30px;top:-38px;font-size:190px;color:#ffffff17}}.eyebrow{{text-transform:uppercase;letter-spacing:3px;font-size:12px;color:#d8f8c5;font-weight:800}}h1{{font-size:clamp(36px,6vw,68px);line-height:1.02;margin:16px 0}}.hero p{{max-width:620px;color:#e1f7e9;font-size:16px;line-height:1.7}}.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0 24px}}.stat{{border:1px solid #cce8d5;background:#ffffffc9;border-radius:20px;padding:20px;box-shadow:0 8px 28px #174e2b0b}}.stat span{{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#638477}}.stat strong{{display:block;font-size:34px;color:#176b4d;margin:8px 0 2px}}.panel{{background:#fffdf8;border:1px solid #dce9d9;border-radius:24px;padding:22px;box-shadow:0 12px 36px #174e2b0c}}.panel-head{{display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap}}h2{{margin:0;color:#163d30}}.sub{{color:#6c857a;margin:7px 0 18px}}input{{width:min(100%,390px);padding:13px 15px;border:1px solid #c9dfd0;border-radius:12px;font-size:14px;outline-color:#48a777}}.table-wrap{{overflow:auto;border-radius:14px;border:1px solid #e0e9df}}table{{width:100%;border-collapse:collapse;min-width:800px}}thead{{background:linear-gradient(90deg,#174b39,#24875f);color:white}}th{{text-align:left;padding:14px;font-size:12px;text-transform:uppercase;letter-spacing:.8px}}td{{padding:13px 14px;border-bottom:1px solid #edf1e9;color:#435c50;font-size:14px}}tbody tr:nth-child(even){{background:#f4f9f0}}tbody tr:hover{{background:#e4f5d7}}.rank{{display:inline-grid;place-items:center;width:36px;height:36px;border-radius:12px;background:#e0f3d2;color:#246746;font-weight:900}}tbody tr:nth-child(-n+3) .rank{{background:linear-gradient(135deg,#1c805b,#b1df62);color:white}}td b{{color:#193e30}}a{{color:#19835d;font-weight:800;text-decoration:none;white-space:nowrap}}a:hover{{text-decoration:underline}}footer{{padding:22px 4px;color:#638477;font-size:12px;line-height:1.7}}@media(max-width:650px){{.wrap{{padding:16px 12px 40px}}.hero{{padding:25px}}.stats{{grid-template-columns:1fr}}.stat{{padding:15px}}.stat strong{{font-size:28px}}.panel{{padding:14px}}.hero:after{{right:-20px;font-size:130px}}}}
</style></head><body><main class="wrap"><div class="top"><div class="brand">♫ NADA / CHARTS</div><div class="pill">TOP 100 · INDONESIA</div></div><section class="hero"><div class="eyebrow">YouTube Music · Chart Snapshot 18 Oktober 2026</div><h1>Indonesia,<br>on repeat.</h1><p>Eksplorasi 100 lagu teratas YouTube Music Indonesia. Cari judul, artis, atau genre musik, lalu buka pencarian lagu langsung di YouTube Music.</p></section><section class="stats"><div class="stat"><span>Total lagu</span><strong>100</strong><small>100 peringkat tersedia</small></div><div class="stat"><span>#1 chart</span><strong style="font-size:25px">Teh Hijau</strong><small>Tulus</small></div><div class="stat"><span>Posisi chart</span><strong>01–100</strong><small>Snapshot chart 18 Oktober 2026</small></div></section><section class="panel"><div class="panel-head"><div><h2>Chart Explorer</h2><div class="sub">Daftar lengkap 100 lagu · urut berdasarkan peringkat sumber</div></div><input id="q" placeholder="Cari judul, artis, atau genre…" aria-label="Cari lagu"></div><div class="table-wrap"><table><thead><tr><th>Rank</th><th>Judul Lagu</th><th>Artis</th><th>Genre (perkiraan)</th><th>Dengarkan</th></tr></thead><tbody id="songs">{trs}</tbody></table></div><footer>Sumber: <a href="https://mewsek.com/charts/youtube-music/id" target="_blank">Mewsek — YouTube Music Indonesia Chart</a>. Snapshot yang digunakan bertanggal 18 Oktober 2026. Data ini merupakan snapshot chart dan bukan jaminan peringkat saat ini. Genre merupakan kategorisasi umum/perkiraan dan dapat tumpang tindih.</footer></section></main><script>const q=document.getElementById('q');q.addEventListener('input',()=>{{const v=q.value.toLocaleLowerCase('id-ID');document.querySelectorAll('#songs tr').forEach(r=>r.style.display=r.innerText.toLocaleLowerCase('id-ID').includes(v)?'':'none')}})</script></body></html>'''
Path(OUT_HTML).write_text(page, encoding="utf-8")
print(f"Berhasil: {len(rows)} lagu, peringkat {rows[0]['peringkat']} sampai {rows[-1]['peringkat']}.")
print(f"File HTML: {OUT_HTML}")
print(f"File CSV : {OUT_CSV}")
