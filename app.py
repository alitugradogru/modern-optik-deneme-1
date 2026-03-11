import streamlit as st

# --- 1. AYARLAR & HAFIZA ---
st.set_page_config(page_title="Modern Optik", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []
if 'aktif_sayfa' not in st.session_state:
    st.session_state.aktif_sayfa = "ana_sayfa" 
if 'secili_marka' not in st.session_state:
    st.session_state.secili_marka = "Tümü"

def sayfaya_git(sayfa_adi, marka="Tümü"):
    st.session_state.aktif_sayfa = sayfa_adi
    st.session_state.secili_marka = marka

def sepete_ekle(urun):
    st.session_state.sepet.append(urun)

# --- 2. VERİTABANI ---
URUNLER = [
    {"id": "1", "marka": "Tom Ford", "model": "Graydon TF1213", "cinsiyet": "Erkek", "fiyat": 15053, "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"},
    {"id": "2", "marka": "Prada", "model": "SPR 17W", "cinsiyet": "Kadın", "fiyat": 14445, "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=600&q=80"},
    {"id": "3", "marka": "Gucci", "model": "GG1505SK", "cinsiyet": "Unisex", "fiyat": 20353, "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=600&q=80"},
    {"id": "4", "marka": "Vogue", "model": "Cat Eye 5582", "cinsiyet": "Kadın", "fiyat": 2205, "resim": "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?auto=format&fit=crop&w=600&q=80"},
    {"id": "5", "marka": "Ray-Ban", "model": "Aviator Classic", "cinsiyet": "Unisex", "fiyat": 7500, "resim": "https://images.unsplash.com/photo-1582142407894-ec85a1260a46?auto=format&fit=crop&w=600&q=80"},
    {"id": "6", "marka": "Prada", "model": "SPR 52Y", "cinsiyet": "Erkek", "fiyat": 17100, "resim": "https://images.unsplash.com/photo-1556306535-0f09a536f0ab?auto=format&fit=crop&w=600&q=80"}
]

MARKALAR = [
    {"isim": "Tom Ford", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tom_Ford_Logo.svg/512px-Tom_Ford_Logo.svg.png"},
    {"isim": "Prada", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Prada-Logo.svg/512px-Prada-Logo.svg.png"},
    {"isim": "Gucci", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Gucci_logo.svg/512px-Gucci_logo.svg.png"},
    {"isim": "Vogue", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Vogue_logo.svg/512px-Vogue_logo.svg.png"},
    {"isim": "Ray-Ban", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Ray-Ban_logo.svg/512px-Ray-Ban_logo.svg.png"}
]

# --- 3. CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&display=swap');
.block-container { padding-top: 2rem !important; max-width: 1200px !important; }
header {visibility: hidden;}

.u-isim { font-family: 'Jost', sans-serif; font-size: 1.1rem; text-align: center; margin-top: 15px; color: #000; font-weight: 600;}
.u-desc { font-family: 'Jost', sans-serif; font-size: 0.85rem; text-align: center; color: #666; margin-top: 5px;}
.u-fiyat { font-family: 'Jost', sans-serif; font-size: 1.2rem; text-align: center; color: #000; font-weight: 600; margin-top: 10px; margin-bottom: 20px;}
img { transition: transform 0.3s ease; } img:hover { transform: scale(1.02); }

/* BÜYÜTME (FULLSCREEN) İKONUNU KÖKÜNDEN YOK ETME KOMUTU */
button[title="View fullscreen"] { display: none !important; }
[data-testid="StyledFullScreenButton"] { display: none !important; }

/* Menü Butonları Tıklanabilir Şeffaf Stil */
.stButton > button { background-color: transparent !important; border: none !important; color: #000 !important; font-size: 1rem !important; font-weight: 600 !important; font-family: 'Jost', sans-serif; }
.stButton > button:hover { opacity: 0.6; }
button[kind="primary"] { background-color: #000 !important; color: #fff !important; width: 100%; font-weight: 600 !important;}
button[kind="primary"]:hover { opacity: 0.8; }
</style>
""", unsafe_allow_html=True)

# --- 4. ÜST MENÜ VE LOGO ---
col_logo, col_bosluk, col_btn0, col_btn1, col_btn2, col_btn3 = st.columns([2.5, 0.5, 1.5, 1.5, 1.5, 1.5], vertical_alignment="center")

with col_logo:
    try:
        st.image("modern-optik-v2a.png", width=180)
    except:
        st.error("Logoyu yükleyiniz.")

with col_btn0:
    if st.button("ANA SAYFA", use_container_width=True):
        sayfaya_git("ana_sayfa")
        st.rerun()
with col_btn1:
    if st.button("TÜM GÖZLÜKLER", use_container_width=True): 
        sayfaya_git("vitrin", "Tümü")
        st.rerun()
with col_btn2:
    if st.button("MARKALAR", use_container_width=True): 
        sayfaya_git("markalar")
        st.rerun()
with col_btn3:
    if st.button("SEPET ({})".format(len(st.session_state.sepet)), use_container_width=True): 
        sayfaya_git("sepet")
        st.rerun()

st.markdown("""
<div style="background-color: #000; color: #fff; text-align: center; padding: 10px 0; margin-top: 5px; margin-bottom: 30px; font-family: 'Jost', sans-serif; font-size: 14px;">
    İlk Siparişinize Özel Sepette %10 İndirim
</div>
""", unsafe_allow_html=True)

# --- 5. SAYFA MİMARİSİ ---

if st.session_state.aktif_sayfa == "ana_sayfa":
    st.markdown('<img src="https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=1200&q=80" style="width:100%; height:400px; object-fit:cover; margin-bottom:40px;">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-family: \"Jost\", sans-serif;'>Trend Ürünler</h3><br>", unsafe_allow_html=True)
    
    cols = st.columns(3, gap="large")
    for i, urun in enumerate(URUNLER[:3]):
        with cols[i % 3]:
            st.image(urun["resim"])
            st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
            st.markdown('<div class="u-desc">{} | {}</div>'.format(urun["model"], urun["cinsiyet"]), unsafe_allow_html=True)
            st.markdown('<div class="u-fiyat">{:,} TL</div>'.format(urun["fiyat"]).replace(",", "."), unsafe_allow_html=True)
            if st.button("SEPETE EKLE", key="ana_ekle_{}".format(urun['id']), type="primary", use_container_width=True):
                sepete_ekle(urun)
                st.toast("{} sepete eklendi!".format(urun['marka']))
                st.rerun()

elif st.session_state.aktif_sayfa == "vitrin":
    baslik = "Tüm Gözlükler" if st.session_state.secili_marka == "Tümü" else "{} Koleksiyonu".format(st.session_state.secili_marka)
    st.markdown("<h3 style='text-align:center;'>{}</h3><br>".format(baslik), unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        secili_cinsiyet = st.selectbox("Cinsiyet", ["Tümü", "Kadın", "Erkek", "Unisex"])
    with col_f2:
        sirala = st.selectbox("Sırala", ["Önerilen", "Fiyat: Düşükten Yükseğe", "Fiyat: Yüksekten Düşüğe"])
    
    st.markdown("<hr>", unsafe_allow_html=True)

    gosterilecek_urunler = []
    for u in URUNLER:
        if st.session_state.secili_marka != "Tümü" and u["marka"] != st.session_state.secili_marka:
            continue
        if secili_cinsiyet != "Tümü" and u["cinsiyet"] != secili_cinsiyet:
            continue
        gosterilecek_urunler.append(u)
        
    if sirala == "Fiyat: Düşükten Yükseğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"])
    elif sirala == "Fiyat: Yüksekten Düşüğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"], reverse=True)

    if len(gosterilecek_urunler) == 0:
        st.warning("Seçili filtrelere uygun ürün bulunmamaktadır.")
    else:
        cols = st.columns(3, gap="large")
        for i, urun in enumerate(gosterilecek_urunler):
            with cols[i % 3]:
                st.image(urun["resim"])
                st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
                st.markdown('<div class="u-desc">{} | {}</div>'.format(urun["model"], urun["cinsiyet"]), unsafe_allow_html=True)
                st.markdown('<div class="u-fiyat">{:,} TL</div>'.format(urun["fiyat"]).replace(",", "."), unsafe_allow_html=True)
                
                if st.button("SEPETE EKLE", key="vitrin_ekle_{}".format(urun['id']), type="primary", use_container_width=True):
                    sepete_ekle(urun)
                    st.toast("{} sepete eklendi!".format(urun['marka']))
                    st.rerun()

elif st.session_state.aktif_sayfa == "markalar":
    st.markdown("<h3 style='text-align:center;'>Markalarımız</h3><br>", unsafe_allow_html=True)
    cols = st.columns(4, gap="large")
    for i, marka in enumerate(MARKALAR):
        with cols[i % 4]:
            st.image(marka["logo"], use_container_width=True)
            if st.button("{} Ürünleri".format(marka["isim"]), key="m_btn_{}".format(i), use_container_width=True):
                sayfaya_git("vitrin", marka["isim"])
                st.rerun()

elif st.session_state.aktif_sayfa == "sepet":
    st.markdown("<h3 style='text-align:center;'>Sepetim</h3><br>", unsafe_allow_html=True)
    if len(st.session_state.sepet) == 0:
        st.info("Sepetinizde ürün bulunmamaktadır.")
    else:
        toplam = 0
        for i, urun in enumerate(st.session_state.sepet):
            c1, c2, c3 = st.columns([1, 4, 1])
            with c1: st.image(urun["resim"])
            with c2: st.markdown("**{}** - {}".format(urun["marka"], urun["model"]))
            with c3:
                st.markdown("**{:,} TL**".format(urun["fiyat"]).replace(",", "."))
                if st.button("Çıkar", key="sil_{}".format(i)):
                    st.session_state.sepet.pop(i)
                    st.rerun()
            toplam += urun["fiyat"]
            st.markdown("---")
        st.markdown("<h3 style='text-align:right;'>Genel Toplam: {:,} TL</h3>".format(toplam).replace(",", "."), unsafe_allow_html=True)
