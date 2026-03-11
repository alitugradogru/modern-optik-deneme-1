import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(page_title="Modern Optik | Özel Koleksiyon", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

# Hafıza (Sepet)
if 'sepet' not in st.session_state:
    st.session_state.sepet = []

# --- 2. ORGANİK VE DERGİ KONSEPTİ CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');

:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { background-color: #FFFFFF !important; color: #000 !important; font-family: 'Jost', sans-serif; }
header {visibility: hidden;} footer {visibility: hidden;}

/* Zarif Üst Menü */
.navbar { display: flex; justify-content: space-between; align-items: center; padding: 25px 60px; background-color: transparent;}
.nav-brand { font-family: 'Playfair Display', serif; font-size: 1.6rem; letter-spacing: 3px; text-transform: uppercase; font-weight: 500;}
.nav-links { font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase; color: #555; display: flex; gap: 40px;}
.nav-links span:hover { color: #000; cursor: pointer; transition: 0.3s;}

/* Büyük, Temiz Hero Görseli */
.editorial-hero { width: 100%; height: 65vh; object-fit: cover; margin-bottom: 50px;}

/* İnsani Metin Alanı */
.story-section { max-width: 700px; margin: 0 auto 70px auto; text-align: center; }
.story-title { font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 20px; font-weight: 400;}
.story-text { font-size: 1.1rem; color: #444; font-weight: 300; line-height: 1.8;}

/* Ürün Grid - Yapay Kutular Yok */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { background: transparent !important; border: none !important; padding: 20px 10px; }
img { width: 100%; object-fit: contain; mix-blend-mode: multiply; transition: transform 0.8s ease;}
img:hover { transform: scale(1.04); }

.u-isim { font-family: 'Playfair Display', serif; font-size: 1.4rem; text-align: center; margin-top: 20px; color: #000;}
.u-desc { font-size: 0.85rem; text-align: center; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;}
.u-fiyat { font-size: 1.1rem; text-align: center; color: #000; font-weight: 400; margin-top: 15px; margin-bottom: 25px;}

/* Zarif Satın Al Butonu */
.stButton > button { width: 100%; border-radius: 0px !important; font-weight: 300; letter-spacing: 2px; color: #000 !important; background-color: transparent !important; border: 1px solid #000; padding: 12px; transition: all 0.4s ease; }
.stButton > button:hover { background-color: #000 !important; color: #fff !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. MENÜ ---
sepet_yazisi = "SEPET ({})".format(len(st.session_state.sepet))
st.markdown("""
<div class="navbar">
    <div class="nav-links">
        <span>Güneş</span>
        <span>Optik</span>
        <span>Markalar</span>
    </div>
    <div class="nav-brand">MODERN OPTİK</div>
    <div class="nav-links">
        <span>Mağazalarımız</span>
        <span style="font-weight: 500; color: #000;">{}</span>
    </div>
</div>
""".format(sepet_yazisi), unsafe_allow_html=True)

# --- 4. KAPAK FOTOĞRAFI ---
st.markdown('<img class="editorial-hero" src="https://images.unsplash.com/photo-1589642380614-4a8c2147b857?auto=format&fit=crop&w=2000&q=80">', unsafe_allow_html=True)

# --- 5. HİKAYE (İnsani ve Samimi Dil) ---
st.markdown("""
<div class="story-section">
    <div class="story-title">Gözlük Bir Tavırdır</div>
    <div class="story-text">
        Dünyanın en iyi tasarımcılarının elinden çıkan asetat çerçeveler ve kusursuz cam işçiliği... 
        Merkezefendi'deki mağazamızda yıllardır sunduğumuz o özel hissi, şimdi dijital vitrinimize taşıdık. 
        Sadece size en çok yakışanı seçin.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. ÜRÜNLER (Tam Ekran, Rahat Dizilim) ---
LUK_URUNLER = [
    {"id": "1", "marka": "Tom Ford", "model": "Graydon", "fiyat": "15.053", "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80"},
    {"id": "2", "marka": "Prada", "model": "Symbole", "fiyat": "14.445", "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=800&q=80"},
    {"id": "3", "marka": "Gucci", "model": "Oversize", "fiyat": "20.353", "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=800&q=80"}
]

cols = st.columns(3, gap="large")
for i, urun in enumerate(LUK_URUNLER):
    with cols[i % 3]:
        st.image(urun["resim"])
        st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
        st.markdown('<div class="u-desc">{} Modeli</div>'.format(urun["model"]), unsafe_allow_html=True)
        st.markdown('<div class="u-fiyat">{} TL</div>'.format(urun["fiyat"]), unsafe_allow_html=True)
        
        if st.button("SEPETE EKLE", key="btn_{}".format(urun['id'])):
            st.session_state.sepet.append(urun)
            st.rerun()
