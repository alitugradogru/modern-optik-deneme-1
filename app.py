import streamlit as st

# --- 1. AYARLAR & GELİŞMİŞ HAFIZA ---
st.set_page_config(page_title="Modern Optik | Özel Koleksiyon", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []
if 'aktif_sayfa' not in st.session_state:
    st.session_state.aktif_sayfa = "vitrin" # vitrin, markalar, sepet
if 'secili_marka' not in st.session_state:
    st.session_state.secili_marka = "Tümü"

def sayfaya_git(sayfa_adi, marka="Tümü"):
    st.session_state.aktif_sayfa = sayfa_adi
    st.session_state.secili_marka = marka

def sepete_ekle(urun):
    st.session_state.sepet.append(urun)

# --- 2. VERİTABANI (Filtreleme ve Sıralama için geliştirildi) ---
# Fiyatları matematiksel işlem yapabilmek için sayı (integer) olarak tutuyoruz.
URUNLER = [
    {"id": "1", "marka": "Tom Ford", "model": "Graydon TF1213", "cinsiyet": "Erkek", "fiyat": 15053, "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80"},
    {"id": "2", "marka": "Prada", "model": "SPR 17W", "cinsiyet": "Kadın", "fiyat": 14445, "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=800&q=80"},
    {"id": "3", "marka": "Gucci", "model": "GG1505SK 002", "cinsiyet": "Unisex", "fiyat": 20353, "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=800&q=80"},
    {"id": "4", "marka": "Ray-Ban", "model": "Aviator Classic", "cinsiyet": "Unisex", "fiyat": 7500, "resim": "https://images.unsplash.com/photo-1582142407894-ec85a1260a46?auto=format&fit=crop&w=800&q=80"},
    {"id": "5", "marka": "Tom Ford", "model": "Cat Eye", "cinsiyet": "Kadın", "fiyat": 16200, "resim": "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?auto=format&fit=crop&w=800&q=80"}
]

MARKALAR = [
    {"isim": "Tom Ford", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tom_Ford_Logo.svg/512px-Tom_Ford_Logo.svg.png"},
    {"isim": "Prada", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Prada-Logo.svg/512px-Prada-Logo.svg.png"},
    {"isim": "Gucci", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Gucci_logo.svg/512px-Gucci_logo.svg.png"},
    {"isim": "Ray-Ban", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Ray-Ban_logo.svg/512px-Ray-Ban_logo.svg.png"}
]

# --- 3. CSS MİMARİSİ ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');
:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { background-color: #FFFFFF !important; color: #000 !important; font-family: 'Jost', sans-serif; }
header {visibility: hidden;} footer {visibility: hidden;}

.u-isim { font-family: 'Playfair Display', serif; font-size: 1.5rem; text-align: center; margin-top: 15px; color: #000;}
.u-desc { font-size: 0.85rem; text-align: center; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;}
.u-fiyat { font-size: 1.1rem; text-align: center; color: #000; font-weight: 500; margin-top: 15px; margin-bottom: 25px;}

.stButton > button { width: 100%; border-radius: 0px !important; font-weight: 500; letter-spacing: 1px; color: #000 !important; background-color: #fff !important; border: 1px solid #000; padding: 10px; transition: all 0.3s ease; }
.stButton > button:hover { background-color: #000 !important; color: #fff !important; }

/* Menü Butonları İçin Şeffaf Stil */
.menu-btn > .stButton > button { border: none !important; font-weight: 400; letter-spacing: 2px; }
.menu-btn > .stButton > button:hover { background-color: transparent !important; color: #888 !important; }
</style>
""", unsafe_allow_html=True)

# --- 4. DİNAMİK ÜST MENÜ & LOGO ---
# Logoyu merkeze almak için kolon yapısını kuruyoruz
col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns([1, 1, 2, 1, 1], gap="small")

with col_m1:
    st.markdown('<div class="menu-btn">', unsafe_allow_html=True)
    if st.button("TÜM GÖZLÜKLER"):
        sayfaya_git("vitrin", "Tümü")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_m2:
    st.markdown('<div class="menu-btn">', unsafe_allow_html=True)
    if st.button("MARKALAR"):
        sayfaya_git("markalar")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_m3:
    # Müşterinin özel logosu burada çağrılıyor
    try:
        st.image("modern-optik-v2a.png", use_container_width=True)
    except:
        st.error("Logo bulunamadı! Lütfen 'modern-optik-v2a.png' dosyasını GitHub'a yüklediğinizden emin olun.")

with col_m4:
    st.write("") # Ortalamak için boşluk

with col_m5:
    st.markdown('<div class="menu-btn">', unsafe_allow_html=True)
    if st.button("SEPET ({})".format(len(st.session_state.sepet))):
        sayfaya_git("sepet")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='margin-top: 10px; margin-bottom: 40px; border: none; border-bottom: 1px solid #eaeaea;'>", unsafe_allow_html=True)

# --- 5. SAYFA YÖNLENDİRME (ROUTING) ---

if st.session_state.aktif_sayfa == "vitrin":
    # --- VİTRİN / FİLTRELEME SAYFASI ---
    
    baslik = "Tüm Koleksiyon" if st.session_state.secili_marka == "Tümü" else "{} Koleksiyonu".format(st.session_state.secili_marka)
    st.markdown("<h2 style='text-align:center; font-family:\"Playfair Display\", serif;'>{}</h2>".format(baslik), unsafe_allow_html=True)
    st.write("")
    
    # Gelişmiş Filtre ve Sıralama Çubuğu
    col_filtre1, col_filtre2, col_filtre3 = st.columns([1, 1, 2])
    with col_filtre1:
        secili_cinsiyet = st.selectbox("Cinsiyet / Kategori", ["Tümü", "Kadın", "Erkek", "Unisex"])
    with col_filtre2:
        sirala = st.selectbox("Sırala", ["Önerilen", "Fiyat: Düşükten Yükseğe", "Fiyat: Yüksekten Düşüğe"])
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Verileri Filtreleme Algoritması
    gosterilecek_urunler = []
    for u in URUNLER:
        # Marka Filtresi
        if st.session_state.secili_marka != "Tümü" and u["marka"] != st.session_state.secili_marka:
            continue
        # Cinsiyet Filtresi
        if secili_cinsiyet != "Tümü" and u["cinsiyet"] != secili_cinsiyet:
            continue
        gosterilecek_urunler.append(u)
        
    # Sıralama Algoritması
    if sirala == "Fiyat: Düşükten Yükseğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"])
    elif sirala == "Fiyat: Yüksekten Düşüğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"], reverse=True)

    # Ürünleri Ekrana Basma
    if len(gosterilecek_urunler) == 0:
        st.warning("Bu filtrelere uygun ürün bulunamadı.")
    else:
        cols = st.columns(3, gap="large")
        for i, urun in enumerate(gosterilecek_urunler):
            with cols[i % 3]:
                st.image(urun["resim"])
                st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
                st.markdown('<div class="u-desc">{} | {}</div>'.format(urun["model"], urun["cinsiyet"]), unsafe_allow_html=True)
                # Fiyatı nokta ile binlik ayırarak formatlıyoruz (örn: 15.053)
                formatli_fiyat = "{:,}".format(urun["fiyat"]).replace(",", ".")
                st.markdown('<div class="u-fiyat">{} TL</div>'.format(formatli_fiyat), unsafe_allow_html=True)
                
                if st.button("SEPETE EKLE", key="ekle_{}".format(urun['id'])):
                    sepete_ekle(urun)
                    st.toast("{} sepete eklendi!".format(urun['marka']))
                    st.rerun()

elif st.session_state.aktif_sayfa == "markalar":
    # --- MARKALAR SAYFASI ---
    st.markdown("<h2 style='text-align:center; font-family:\"Playfair Display\", serif;'>Markalarımız</h2>", unsafe_allow_html=True)
    st.write("")
    
    cols = st.columns(4, gap="large")
    for i, marka in enumerate(MARKALAR):
        with cols[i % 4]:
            st.image(marka["logo"], use_container_width=True)
            st.write("")
            if st.button("{} Ürünlerini Gör".format(marka["isim"]), key="marka_btn_{}".format(i)):
                sayfaya_git("vitrin", marka["isim"])
                st.rerun()

elif st.session_state.aktif_sayfa == "sepet":
    # --- SEPET SAYFASI ---
    st.markdown("<h2 style='text-align:center; font-family:\"Playfair Display\", serif;'>Alışveriş Çantanız</h2>", unsafe_allow_html=True)
    
    if len(st.session_state.sepet) == 0:
        st.info("Çantanızda henüz ürün bulunmamaktadır.")
    else:
        toplam = 0
        for i, urun in enumerate(st.session_state.sepet):
            c1, c2, c3 = st.columns([1, 4, 1])
            with c1:
                st.image(urun["resim"])
            with c2:
                st.markdown("**{}** - {}".format(urun["marka"], urun["model"]))
            with c3:
                formatli_fiyat = "{:,}".format(urun["fiyat"]).replace(",", ".")
                st.markdown("**{} TL**".format(formatli_fiyat))
                if st.button("Kaldır", key="sil_{}".format(i)):
                    st.session_state.sepet.pop(i)
                    st.rerun()
            toplam += urun["fiyat"]
            st.markdown("---")
            
        formatli_toplam = "{:,}".format(toplam).replace(",", ".")
        st.markdown("<h3 style='text-align:right;'>Genel Toplam: {} TL</h3>".format(formatli_toplam), unsafe_allow_html=True)
