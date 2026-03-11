import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(
    page_title="Modern Optik - Premium Konsept",
    page_icon="🕶️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS (LÜKS TASARIM) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');

:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { background-color: #FAFAFA !important; color: #111 !important; font-family: 'Inter', sans-serif; }
header {visibility: hidden;} footer {visibility: hidden;}

/* Navigasyon */
.top-nav { display: flex; justify-content: space-between; align-items: center; padding: 20px 50px; border-bottom: 1px solid #EAEAEA; }
.top-nav-logo { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; }
.top-nav-links { display: flex; gap: 30px; font-size: 0.85rem; letter-spacing: 1.5px; font-weight: 400; text-transform: uppercase; color: #333; }

/* Hero Banner */
.hero-section { position: relative; text-align: center; color: white; margin-bottom: 40px; }
.hero-image { width: 100%; height: 500px; object-fit: cover; filter: brightness(0.65); }
.hero-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; }
.hero-title { font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 10px; }
.hero-subtitle { font-size: 1rem; font-weight: 300; letter-spacing: 5px; text-transform: uppercase; }

/* Başlıklar */
.section-title { font-family: 'Playfair Display', serif; font-size: 2rem; text-align: center; margin-top: 40px; margin-bottom: 15px; color: #111; }
.section-desc { text-align: center; color: #666; margin-bottom: 40px; font-weight: 300; font-size: 1rem; line-height: 1.6; }

/* Markalar Şeridi (12-13 Marka Çözümü) */
.brand-ticker { display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; padding: 30px 0; border-top: 1px solid #eee; border-bottom: 1px solid #eee; margin-bottom: 50px; }
.brand-name { font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.1rem; color: #999; letter-spacing: 3px; text-transform: uppercase; transition: 0.3s;}
.brand-name:hover { color: #000; cursor: pointer; }

/* Güven/İkna Alanı (Satışa İten Kısım) */
.trust-section { display: flex; justify-content: space-around; background-color: #111; color: white; padding: 40px 20px; margin-top: 60px; }
.trust-item { text-align: center; width: 30%; }
.trust-icon { font-size: 2rem; margin-bottom: 15px; }
.trust-title { font-weight: 600; font-size: 1rem; letter-spacing: 1px; margin-bottom: 10px; text-transform: uppercase;}
.trust-desc { font-weight: 300; font-size: 0.85rem; color: #aaa; line-height: 1.5;}

/* Ürünler */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { background: transparent !important; border: none !important; padding: 10px; }
img { width: 100%; object-fit: contain; mix-blend-mode: multiply; transition: transform 0.6s ease;}
img:hover { transform: scale(1.03); }
.urun-isim { font-size: 1.3rem; font-weight: 600; text-align: center; letter-spacing: 1px; margin-top: 15px; margin-bottom: 2px; color: #000; font-family: 'Playfair Display', serif;}
.urun-kategori { font-size: 0.8rem; font-weight: 300; text-align: center; color: #666; text-transform: uppercase; margin-bottom: 15px;}
.urun-fiyat { font-size: 1rem; font-weight: 400; text-align: center; color: #000; margin-bottom: 20px;}
.stButton > button { width: 100%; border-radius: 0px !important; font-weight: 400; letter-spacing: 2px; color: white !important; background-color: #000000 !important; border: 1px solid #000; padding: 12px; transition: all 0.3s ease; }
.stButton > button:hover { background-color: #ffffff !important; color: #000000 !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. ÜST MENÜ ---
st.markdown("""
<div class="top-nav">
    <div class="top-nav-logo">MODERN OPTİK</div>
    <div class="top-nav-links">
        <span>Markalarımız</span>
        <span>Güneş Gözlükleri</span>
        <span>Optik</span>
        <span>Randevu Al</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. HERO BANNER ---
st.markdown("""
<div class="hero-section">
    <img class="hero-image" src="https://images.unsplash.com/photo-1589642380614-4a8c2147b857?auto=format&fit=crop&w=1600&q=80">
    <div class="hero-text">
        <div class="hero-title">Karakterini Seç</div>
        <div class="hero-subtitle">Dünyanın En Seçkin 13 Markası</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. MARKALAR ŞERİDİ (13 Marka Çözümü) ---
st.markdown("""
<div class="brand-ticker">
    <span class="brand-name">Tom Ford</span>
    <span class="brand-name">Persol</span>
    <span class="brand-name">Cartier</span>
    <span class="brand-name">Ray-Ban</span>
    <span class="brand-name">Oliver Peoples</span>
    <span class="brand-name">Prada</span>
    <span class="brand-name">Gentle Monster</span>
</div>
<div class="section-desc" style="margin-top:-20px; font-size:0.8rem;">ve çok daha fazlası... Tüm markaları keşfetmek için menüyü kullanın.</div>
""", unsafe_allow_html=True)

# --- 6. VİTRİN (Sadece En İyiler) ---
st.markdown("<div class='section-title'>Sezonun İkonları</div>", unsafe_allow_html=True)
st.write("")

LUK_URUNLER = [
    {"id": "1", "isim": "TOM FORD", "kategori": "Asetat / Polarize", "fiyat": "14.500 TL", "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"},
    {"id": "2", "isim": "PERSOL", "kategori": "El Yapımı / İtalya", "fiyat": "11.200 TL", "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"},
    {"id": "3", "isim": "CARTIER", "kategori": "Altın Kaplama / Çerçevesiz", "fiyat": "42.000 TL", "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=600&q=80"}
]

cols = st.columns(3, gap="large")
for i, urun in enumerate(LUK_URUNLER):
    with cols[i % 3]:
        st.image(urun["resim"])
        st.markdown(f'<div class="urun-isim">{urun["isim"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="urun-kategori">{urun["kategori"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="urun-fiyat">{urun["fiyat"]}</div>', unsafe_allow_html=True)
        if st.button("SEPETE EKLE", key=f"btn_{urun['id']}"):
            st.toast(f"{urun['isim']} sepetinize eklendi. Güvenli ödeme adımına geçebilirsiniz.")

# --- 7. GÜVEN VE SATIŞA İKNA ALANI ---
st.markdown("""
<div class="trust-section">
    <div class="trust-item">
        <div class="trust-icon">🛡️</div>
        <div class="trust-title">%100 Orijinal Ürün</div>
        <div class="trust-desc">Tüm ürünlerimiz resmi distribütör garantilidir ve orijinallik sertifikası ile gönderilir.</div>
    </div>
    <div class="trust-item">
        <div class="trust-icon">📦</div>
        <div class="trust-title">Sigortalı Kargo</div>
        <div class="trust-desc">Siparişleriniz kargoda hasar veya kaybolma riskine karşı tam sigortalı olarak kapınıza gelir.</div>
    </div>
    <div class="trust-item">
        <div class="trust-icon">🏬</div>
        <div class="trust-title">Mağazada Değişim</div>
        <div class="trust-desc">İnternetten alın, dilerseniz merkez mağazamızda deneyerek 14 gün içinde değiştirin.</div>
    </div>
</div>
""", unsafe_allow_html=True)
