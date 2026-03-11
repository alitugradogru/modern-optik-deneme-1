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

/* Markalar Şeridi */
.brand-ticker { display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; padding: 30px 0; border-top: 1px solid #eee; border-bottom: 1px solid #eee; margin-bottom: 50px; }
.brand-name { font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.1rem; color: #999; letter-spacing: 3px; text-transform: uppercase; transition: 0.3s;}
.brand-name:hover { color: #000; cursor: pointer; }

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
        <div class="hero-subtitle">Dünyanın En Seçkin Markaları</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. MARKALAR ŞERİDİ ---
st.markdown("""
<div class="brand-ticker">
    <span class="brand-name">Tom Ford</span>
    <span class="brand-name">Prada</span>
    <span class="brand-name">Gucci</span>
    <span class="brand-name">Ray-Ban</span>
    <span class="brand-name">Vogue</span>
    <span class="brand-name">Miu Miu</span>
</div>
""", unsafe_allow_html=True)

# --- 6. VİTRİN (Gerçek Modern Optik Ürünleri) ---
st.markdown("<div class='section-title'>Sezonun İkonları</div>", unsafe_allow_html=True)
st.write("")

LUK_URUNLER = [
    {
        "id": "1", 
        "isim": "TOM FORD", 
        "kategori": "Graydon TF1213", 
        "fiyat": "15.053 TL", 
        "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "2", 
        "isim": "PRADA", 
        "kategori": "SPR 17W", 
        "fiyat": "14.445 TL", 
        "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "3", 
        "isim": "GUCCI", 
        "kategori": "GG1505SK 002", 
        "fiyat": "20.353 TL", 
        "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=600&q=80"
    }
]

cols = st.columns(3, gap="large")
for i, urun in enumerate(LUK_URUNLER):
    with cols[i % 3]:
        st.image(urun["resim"])
        st.markdown('<div class="urun-isim">{}</div>'.format(urun["isim"]), unsafe_allow_html=True)
        st.markdown('<div class="urun-kategori">{}</div>'.format(urun["kategori"]), unsafe_allow_html=True)
        st.markdown('<div class="urun-fiyat">{}</div>'.format(urun["fiyat"]), unsafe_allow_html=True)
        if st.button("SEPETE EKLE", key="btn_{}".format(urun['id'])):
            st.toast("{} sepetinize eklendi. Güvenli ödeme adımına geçebilirsiniz.".format(urun['isim']))
