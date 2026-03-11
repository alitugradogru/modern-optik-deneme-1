import streamlit as st
import datetime

# --- 1. AYARLAR & HAFIZA ---
st.set_page_config(page_title="Modern Optik - Premium", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []

# --- 2. LÜKS CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500;600&display=swap');
:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { background-color: #FAFAFA !important; color: #111 !important; font-family: 'Inter', sans-serif; }
header {visibility: hidden;} footer {visibility: hidden;}

.top-nav { display: flex; justify-content: space-between; align-items: center; padding: 20px 50px; border-bottom: 1px solid #EAEAEA; }
.top-nav-logo { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; }
.top-nav-links { display: flex; gap: 30px; font-size: 0.85rem; letter-spacing: 1.5px; font-weight: 400; text-transform: uppercase; color: #333; }
.hero-section { position: relative; text-align: center; color: white; margin-bottom: 40px; }
.hero-image { width: 100%; height: 400px; object-fit: cover; filter: brightness(0.65); }
.hero-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; }
.hero-title { font-family: 'Playfair Display', serif; font-size: 3.5rem; margin-bottom: 10px; }
.section-title { font-family: 'Playfair Display', serif; font-size: 2rem; text-align: center; margin-top: 20px; margin-bottom: 30px; color: #111; }

.side-panel { background-color: white; padding: 20px; border: 1px solid #eaeaea; margin-top: 10px; margin-bottom: 20px;}
.panel-title { font-family: 'Playfair Display', serif; font-size: 1.3rem; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 15px; font-weight: 600;}
.sepet-satir { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.9rem; border-bottom: 1px dashed #eee; padding-bottom: 5px;}
.sepet-toplam { display: flex; justify-content: space-between; font-weight: bold; font-size: 1.1rem; margin-top: 15px; padding-top: 10px; }

[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { background: transparent !important; border: none !important; padding: 10px; }
img { width: 100%; object-fit: contain; mix-blend-mode: multiply; transition: transform 0.6s ease;}
img:hover { transform: scale(1.03); }
.urun-isim { font-size: 1.2rem; font-weight: 600; text-align: center; letter-spacing: 1px; margin-top: 15px; color: #000; font-family: 'Playfair Display', serif;}
.urun-kategori { font-size: 0.8rem; font-weight: 300; text-align: center; color: #666; text-transform: uppercase; margin-bottom: 10px;}
.urun-fiyat { font-size: 1rem; font-weight: 400; text-align: center; color: #000; margin-bottom: 15px;}
.stButton > button { width: 100%; border-radius: 0px !important; font-weight: 400; letter-spacing: 1px; color: white !important; background-color: #111 !important; border: 1px solid #111; padding: 10px; transition: all 0.3s ease; }
.stButton > button:hover { background-color: #fff !important; color: #111 !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. ÜST MENÜ ---
st.markdown("""
<div class="top-nav">
    <div class="top-nav-logo">MODERN OPTİK</div>
    <div class="top-nav-links">
        <span>Güneş Gözlükleri</span>
        <span>Optik</span>
        <span style="font-weight:bold; color:black;">Sepetim ({})</span>
    </div>
</div>
""".format(len(st.session_state.sepet)), unsafe_allow_html=True)

# --- 4. HERO BANNER ---
st.markdown("""
<div class="hero-section">
    <img class="hero-image" src="https://images.unsplash.com/photo-1589642380614-4a8c2147b857?auto=format&fit=crop&w=1600&q=80">
    <div class="hero-text">
        <div class="hero-title">Vizyonunuzu Kişiselleştirin</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. İKİLİ KOLON (SOL: İŞLEMLER, SAĞ: VİTRİN) ---
col_sol, col_sag = st.columns([1.2, 2.8], gap="large")

with col_sol:
    # --- SEPET MODÜLÜ ---
    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-title'>🛒 Alışveriş Çantası</div>", unsafe_allow_html=True)
    
    if len(st.session_state.sepet) == 0:
        st.info("Çantanız boş.")
    else:
        toplam_tutar = 0
        for i, urun in enumerate(st.session_state.sepet):
            st.markdown(
                "<div class='sepet-satir'><span>{}</span><span>{} TL</span></div>".format(urun['marka'], urun['fiyat']), 
                unsafe_allow_html=True
            )
            toplam_tutar += float(urun['fiyat'].replace(".", "").replace(",", "."))
            
            if st.button("Çıkar", key="sil_{}".format(i)):
                st.session_state.sepet.pop(i)
                st.rerun()

        st.markdown(
            "<div class='sepet-toplam'><span>Ara Toplam:</span><span>{:,.0f} TL</span></div>".format(toplam_tutar).replace(",", "."), 
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("GÜVENLİ ÖDEME", key="odeme_btn"):
            st.success("Ödeme altyapısına bağlanılıyor...")
            st.session_state.sepet = []
    st.markdown("</div>", unsafe_allow_html=True)

    # --- VIP RANDEVU MODÜLÜ (YENİ EKLENDİ!) ---
    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-title'>🗓️ VIP Mağaza Randevusu</div>", unsafe_allow_html=True)
    st.write("Özel stil danışmanlığı ve detaylı göz ölçümü için Merkez mağazamızdan randevu alın.")
    
    with st.form("randevu_formu"):
        isim = st.text_input("Adınız Soyadınız")
        tarih = st.date_input("Randevu Tarihi", min_value=datetime.date.today())
        saat = st.selectbox("Saat Seçimi", ["10:00", "11:30", "14:00", "16:00", "18:00"])
        randevu_kaydet = st.form_submit_button("RANDEVU OLUŞTUR")
        
        if randevu_kaydet:
            if isim:
                st.success("Sayın {}, {} tarihi saat {} için VIP randevunuz onaylandı!".format(isim, tarih.strftime("%d.%m.%Y"), saat))
            else:
                st.error("Lütfen adınızı giriniz.")
    st.markdown("</div>", unsafe_allow_html=True)

with col_sag:
    # --- VİTRİN MODÜLÜ ---
    st.markdown("<div class='section-title'>Özel Seçki</div>", unsafe_allow_html=True)
    
    LUK_URUNLER = [
        {"id": "1", "marka": "TOM FORD", "kategori": "Graydon TF1213", "fiyat": "15.053", "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"},
        {"id": "2", "marka": "PRADA", "kategori": "SPR 17W", "fiyat": "14.445", "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"},
        {"id": "3", "marka": "GUCCI", "kategori": "GG1505SK", "fiyat": "20.353", "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=600&q=80"}
    ]

    cols = st.columns(3, gap="medium")
    for i, urun in enumerate(LUK_URUNLER):
        with cols[i % 3]:
            st.image(urun["resim"])
            st.markdown('<div class="urun-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
            st.markdown('<div class="urun-kategori">{}</div>'.format(urun["kategori"]), unsafe_allow_html=True)
            st.markdown('<div class="urun-fiyat">{} TL</div>'.format(urun["fiyat"]), unsafe_allow_html=True)
            
            if st.button("SEPETE EKLE", key="btn_{}".format(urun['id'])):
                st.session_state.sepet.append(urun)
                st.rerun()
