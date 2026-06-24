# Detrox · Yapay Zekâ Komuta Paneli

Detrox dijital dönüşüm platformunun tek dosyalık, kendi içinde tam (self-contained)
patron komuta paneli demosu. Tüm CSS/JS/varlıklar `index.html` içine gömülüdür
(CDN yok → çevrimdışı da açılır). Veriler **temsilidir** (panelde demo rozeti).

## Çalıştırma (yerel)

```bash
pip install -r requirements.txt
python app.py
# http://localhost:8080
```

## Yayın (Railway)

- `Procfile` / `railway.json` ile Nixpacks otomatik kurar ve `gunicorn` ile çalıştırır.
- Sağlık kontrolü: `/healthz`
- **İsteğe bağlı parola koruması:** Railway → Variables bölümüne
  `PANEL_USER` ve `PANEL_PASS` eklenirse panel HTTP Basic Auth ile parola ister.
  İkisi de boşsa panel herkese açıktır.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `index.html` | Komuta paneli (tek dosya, gömülü logo + tüm görünümler) |
| `app.py` | Flask sunucusu (statik servis + opsiyonel Basic Auth) |
| `requirements.txt` | Flask + gunicorn |
| `Procfile` / `railway.json` | Railway/Nixpacks başlatma yapılandırması |
