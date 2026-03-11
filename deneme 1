import streamlit as st

# --- 1. AYARLAR ---
st.set_page_config(
    page_title="Lüks Optik Konsepti",
    page_icon="🕶️",
    layout="wide",
    initial_sidebar_state="collapsed" # Lüks sitelerde menü başta kapalı olur, kalabalık yapmaz.
)

# --- 2. LÜKS ÜRÜN VERİTABANI ---
# Fotoğraflar stüdyo çekimi, arka planları temiz. Fiyatlar premium.
LUK_URUNLER = [
    {
        "id": "1", 
        "isim": "NOIR ECLIPSE", 
        "kategori": "Titanyum / El Yapımı", 
        "fiyat": "12.500 TL", 
        "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "2", 
        "isim": "AURA TORTOISE", 
        "kategori": "Asetat / Polarize", 
        "fiyat": "9.800 TL", 
        "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "3", 
        "isim": "LUMINA CLASSIC", 
        "kategori": "24K Altın Kaplama / Optik", 
        "fiyat": "18.200 TL", 
        "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=600&q=80"
    }
]

# --- 3. TASARIM (MİNİMALİST LÜKS CSS) ---
st.markdown("""
<style>
/* Font ve Arkaplan */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { 
    background-color: #FAFAFA !important; /* Çok uçuk bir gri/beyaz, tam stüdyo rengi */
    color: #111111 !important; 
    font-family: 'Inter', sans-serif; 
}

/* Gereksiz her şeyi gizle (Header, Footer, Menü çizgileri) */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Başlık Tipi */
h1 { font-weight: 300; letter-spacing: 4px; text-align: center; color: #000 !important; text-transform: uppercase; font-size: 2.5rem; margin-bottom: 50px;}

/* Ürün Kartları - SIFIR ÇERÇEVE, SADECE BOŞLUK */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { 
    background: transparent !important; 
    border: none !important; 
    padding: 10px; 
}

/* Ürün Fotoğrafları */
img { 
    border-radius: 0px; /* Lüks sitelerde köşeler genelde keskindir */
    width: 100%; 
    object-fit: contain; 
    mix-blend-mode: multiply; /* Beyaz arkaplanlı fotoları siteye yedirir */
    transition: transform 0.6s ease;
}
img:hover {
    transform: scale(1.03); /* Üstüne gelince zarifçe büyür */
}

/* Ürün Yazıları */
.urun-isim { font-size: 1.1rem; font-weight: 600; text-align: center; letter-spacing: 1px; margin-top: 15px; margin-bottom: 2px; color: #000;}
.urun-kategori { font-size: 0.8rem; font-weight: 300; text-align: center; color: #666; text-transform: uppercase; margin-bottom: 15px;}
.urun-fiyat { font-size: 0.95rem; font-weight: 400; text-align: center; color: #000; margin-bottom: 20px;}

/* Siyah Şık Butonlar */
.stButton > button { 
    width: 100%; 
    border-radius: 0px !important; /* Keskin köşeli lüks buton */
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
</style>
""", unsafe_allow_html=True)

# --- 4. VİTRİN DİZİLİMİ ---

st.markdown("<h1>Yeni Koleksiyon</h1>", unsafe_allow_html=True)
st.write("") # Boşluk candır
st.write("")

# 3'lü zarif ızgara (Grid) yapısı
cols = st.columns(3, gap="large")

for i, urun in enumerate(LUK_URUNLER):
    with cols[i % 3]:
        # Resmi göster
        st.image(urun["resim"])
        
        # HTML ile yazıları tam istediğimiz incelikte ayarlıyoruz
        st.markdown(f'<div class="urun-isim">{urun["isim"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="urun-kategori">{urun["kategori"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="urun-fiyat">{urun["fiyat"]}</div>', unsafe_allow_html=True)
        
        # Buton
        if st.button("KEŞFET", key=f"btn_{urun['id']}"):
            st.toast(f"Ürün detayına gidiliyor: {urun['isim']}")

# Alt kısım (Footer niyetine zarif bir kapanış)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #888; letter-spacing: 1px;'>© 2026 EXCLUSIVE EYEWEAR STUDIO</p>", unsafe_allow_html=True)
