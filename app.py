import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(
    page_title="Modern Optik - Premium Konsept",
    page_icon="🕶️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS (LÜKS VE GELİŞMİŞ TASARIM) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap');

:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { 
    background-color: #FAFAFA !important; 
    color: #111 !important; 
    font-family: 'Inter', sans-serif; 
}

/* Standart Streamlit menülerini sakla */
header {visibility: hidden;}
footer {visibility: hidden;}

/* --- ÜST MENÜ (NAVBAR) --- */
.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 50px;
    border-bottom: 1px solid #EAEAEA;
    margin-bottom: 0px;
    background-color: transparent;
}
.top-nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.top-nav-links {
    display: flex;
    gap: 30px;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    font-weight: 400;
    text-transform: uppercase;
    color: #333;
}

/* --- KAHRAMAN ALANI (HERO BANNER) --- */
.hero-section {
    position: relative;
    text-align: center;
    color: white;
    margin-bottom: 60px;
}
.hero-image {
    width: 100%;
    height: 550px;
    object-fit: cover;
    filter: brightness(0.65);
}
.hero-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4.5rem;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 15px;
}
.hero-subtitle {
    font-size: 1.1rem;
    font-weight: 300;
    letter-spacing: 6px;
    text-transform: uppercase;
}

/* --- BÖLÜM BAŞLIKLARI --- */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 15px;
    color: #111;
}
.section-desc {
    text-align: center;
    color: #666;
    margin-bottom: 50px;
    font-weight: 300;
    font-size: 1rem;
    line-height: 1.6;
}

/* --- ÜRÜN KARTLARI --- */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { 
    background: transparent !important; 
    border: none !important; 
    padding: 10px; 
}
img { 
    border-radius: 0px; 
    width: 100%; 
    object-fit: contain; 
    mix-blend-mode: multiply; 
    transition: transform 0.6s ease;
}
img:hover { transform: scale(1.03); }
.urun-isim { font-size: 1.3rem; font-weight: 600; text-align: center; letter-spacing: 1px; margin-top: 15px; margin-bottom: 2px; color: #000; font-family: 'Playfair Display', serif;}
.urun-kategori { font-size: 0.8rem; font-weight: 300; text-align: center; color: #666; text-transform: uppercase; margin-bottom: 15px;}
.urun-fiyat { font-size: 1rem; font-weight: 400; text-align: center; color: #000; margin-bottom: 20px;}

/* Siyah Şık Butonlar */
.stButton > button { 
    width: 100%; 
    border-radius: 0px !important; 
    font-weight: 400; 
    letter-spacing: 2px;
    color: white !important; 
    background-color: #000000 !important; 
    border: 1px solid #000; 
    padding: 12px;
    transition: all 0.3s ease;
}
.stButton > button:hover { 
    background-color: #ffffff !important; 
    color: #000000 !important;
}

/* --- FOOTER --- */
.footer {
    margin-top: 80px;
    padding: 60px 20px;
    background-color: #111;
    color: #fff;
    text-align: center;
}
.footer-text {
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    color: #888;
    line-height: 2;
}
</style>
""", unsafe_allow_html=True)

# --- 3. ÜST MENÜ (NAVBAR) ---
st.markdown("""
<div class="top-nav">
    <div class="top-nav-logo">MODERN OPTİK</div>
    <div class="top-nav-links">
        <span>Koleksiyon</span>
        <span>Güneş Gözlükleri</span>
        <span>Optik</span>
        <span>İletişim</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. KAHRAMAN ALANI (HERO BANNER) ---
st.markdown("""
<div class="hero-section">
    <img class="hero-image" src="https://images.unsplash.com/photo-1589642380614-4a8c2147b857?auto=format&fit=crop&w=1600&q=80">
    <div class="hero-text">
        <div class="hero-title">Vizyonu Yeniden Tanımla</div>
        <div class="hero-subtitle">2026 İlkbahar / Yaz Koleksiyonu</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. MARKAMIZIN HİKAYESİ ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='section-title'>Ustalık ve Zarafet</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-desc'>El yapımı çerçeveler, kusursuz cam kesimleri ve zamansız tasarımlar. Gözlük bir aksesuardan fazlasıdır; karakterinizin en güçlü imzasıdır. Dünyanın en seçkin markaları şimdi tek bir çatı altında, yepyeni bir dijital deneyimle sizlerle buluşuyor.</div>", unsafe_allow_html=True)

# --- 6. VİTRİN ---
st.markdown("<div class='section-title'>Öne Çıkanlar</div>", unsafe_allow_html=True)
st.write("")

LUK_URUNLER = [
    {
        "id": "1", 
        "isim": "TOM FORD", 
        "kategori": "Asetat / Polarize", 
        "fiyat": "14.500 TL", 
        "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "2", 
        "isim": "PERSOL", 
        "kategori": "El Yapımı / İtalya", 
        "fiyat": "11.200 TL", 
        "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "3", 
        "isim": "CARTIER", 
        "kategori": "Altın Kaplama / Çerçevesiz", 
        "fiyat": "42.000 TL", 
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
        
        if st.button("İNCELE", key="btn_{}".format(urun['id'])):
            st.toast("Ürün detay sayfasına yönlendiriliyor: {}".format(urun['isim']))

# --- 7. ALT BİLGİ (FOOTER) ---
st.markdown("""
<div class="footer">
    <div class="top-nav-logo" style="margin-bottom: 20px;">MODERN OPTİK</div>
    <div class="footer-text">
        Bizi Ziyaret Edin<br>
        info@modernoptik.com.tr | +90 555 123 45 67<br>
        © 2026 Tüm Hakları Saklıdır.
    </div>
</div>
""", unsafe_allow_html=True)
