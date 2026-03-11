import streamlit as st

# --- 1. AYARLAR & HAFIZA ---
st.set_page_config(page_title="Modern Optik", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []
if 'aktif_sayfa' not in st.session_state:
    st.session_state.aktif_sayfa = "vitrin"
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

# --- 3. CSS (FOTOĞRAFTAKİ DİZAYNIN BİREBİR KLONU) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Playfair+Display:wght@400;700&display=swap');
.block-container { padding-top: 1rem !important; max-width: 1400px !important; }
header {visibility: hidden;} footer {visibility: hidden;}

/* Menü Butonları (Fotoğraftaki İnce Yazılar) */
button[kind="secondary"] { border: none !important; background: transparent !important; color: #000 !important; font-family: 'Jost', sans-serif; font-weight: 500 !important; font-size: 12px !important; padding: 0 !important; box-shadow: none !important; letter-spacing: 0.5px; }
button[kind="secondary"]:hover { color: #888 !important; }

/* Sepete Ekle Butonları */
button[kind="primary"] { background-color: #000 !important; color: #fff !important; border-radius: 3px !important; border: none !important; width: 100%; font-weight: 600 !important; font-family: 'Jost', sans-serif;}
button[kind="primary"]:hover { background-color: #333 !important; }

/* Arama Çubuğu */
div[data-baseweb="input"] { border-radius: 0px !important; border: 1px solid #ddd !important; }

/* Ürün Yazıları */
.u-isim { font-family: 'Jost', sans-serif; font-size: 1.1rem; text-align: center; margin-top: 15px; color: #000; font-weight: 600;}
.u-desc { font-family: 'Jost', sans-serif; font-size: 0.85rem; text-align: center; color: #666; margin-top: 5px;}
.u-fiyat { font-family: 'Jost', sans-serif; font-size: 1.2rem; text-align: center; color: #000; font-weight: 600; margin-top: 10px; margin-bottom: 20px;}
img { transition: transform 0.5s ease; } img:hover { transform: scale(1.03); }
</style>
""", unsafe_allow_html=True)

# --- 4. BİREBİR KLONLANMIŞ ÜST MENÜ ---
col_logo, col_menu, col_arama = st.columns([2.5, 7, 2.5], vertical_alignment="center")

with col_logo:
    try:
        st.image("modern-optik-v2a.png", width=160)
    except:
        st.error("Logoyu yükleyiniz.")

with col_menu:
    m1, m2, m3, m4, m5, m6, m7, m8 = st.columns(8)
    with m1: st.button("KAMPANYALAR", type="secondary")
    with m2: st.button("KADIN", type="secondary")
    with m3: st.button("ERKEK", type="secondary")
    with m4: st.button("ÇOCUK", type="secondary")
    with m5: st.button("UNISEX", type="secondary")
    with m6: 
        if st.button("TÜMÜ", type="secondary"): sayfaya_git("vitrin", "Tümü")
    with m7: 
        if st.button("MARKALAR", type="secondary"): sayfaya_git("markalar")
    with m8: 
        if st.button("SEPET ({})".format(len(st.session_state.sepet)), type="secondary"): sayfaya_git("sepet")

with col_arama:
    st.text_input("Arama", placeholder="Arama...", label_visibility="collapsed")

# --- 5. SİYAH İNDİRİM ŞERİDİ (Fotoğraftaki Gibi) ---
st.markdown("""
<div style="background-color: #000; color: #fff; text-align: center; padding: 12px 0; margin-top: 10px; margin-bottom: 0px; font-family: 'Jost', sans-serif; font-size: 15px; font-weight: 500;">
    İlk Siparişinize Özel Sepette %10 İndirim
</div>
""", unsafe_allow_html=True)

# --- 6. DİNAMİK İÇERİK (SAYFALAR) ---

if st.session_state.aktif_sayfa == "vitrin":
    
    # Sadece ana sayfada veya "Tümü" seçiliyse Vogue afişi çıksın
    if st.session_state.secili_marka == "Tümü":
        st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px; background-color: #c4b9a9; height: 500px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
            <img src="https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=2000&q=80" style="position: absolute; width: 100%; height: 100%; object-fit: cover; opacity: 0.6;">
            <h1 style="position: relative; color: white; font-family: 'Playfair Display', serif; font-size: 8vw; font-weight: bold; letter-spacing: 15px; margin: 0; text-shadow: 2px 2px 10px rgba(0,0,0,0.2);">VOGUE</h1>
            <div style="position: absolute; top: 50%; left: 30px; transform: translateY(-50%); background: white; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); cursor: pointer; color: black; font-weight: bold; font-size: 20px;">❮</div>
            <div style="position: absolute; top: 50%; right: 30px; transform: translateY(-50%); background: white; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); cursor: pointer; color: black; font-weight: bold; font-size: 20px;">❯</div>
            <div style="position: absolute; bottom: 30px; right: 30px; background: #25D366; color: white; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 32px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); cursor: pointer;">
                <svg style="width:30px;height:30px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 15 3.8 13.46 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67M8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7 8.5 7 9.71C7 10.93 7.89 12.1 8 12.27C8.14 12.44 9.76 14.94 12.25 16C12.84 16.27 13.3 16.42 13.66 16.53C14.25 16.72 14.79 16.69 15.22 16.63C15.7 16.56 16.68 16.03 16.89 15.45C17.1 14.87 17.1 14.38 17.04 14.27C16.97 14.17 16.81 14.11 16.56 13.96C16.31 13.81 15.08 13.2 14.85 13.11C14.62 13 14.46 12.96 14.3 13.2C14.15 13.45 13.7 14.03 13.56 14.2C13.42 14.37 13.28 14.39 13.03 14.24C12.78 14.09 11.96 13.82 10.97 12.95C10.19 12.26 9.67 11.43 9.52 11.18C9.37 10.93 9.5 10.8 9.63 10.67C9.74 10.56 9.88 10.38 10.03 10.22C10.18 10.05 10.23 9.94 10.33 9.74C10.43 9.54 10.38 9.37 10.31 9.24C10.23 9.11 9.67 7.75 9.44 7.18C9.21 6.64 8.98 6.71 8.82 6.71C8.67 6.71 8.5 6.71 8.53 7.33Z"/></svg>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    baslik = "Trend Ürünler" if st.session_state.secili_marka == "Tümü" else "{} Ürünleri".format(st.session_state.secili_marka)
    st.markdown("<h3 style='font-family: \"Jost\", sans-serif; font-weight: 600; margin-bottom: 20px;'>{}</h3>".format(baslik), unsafe_allow_html=True)
    
    # --- FİLTRELEME & SIRALAMA MODÜLÜ ---
    col_filtre1, col_filtre2, col_filtre3 = st.columns([1.5, 1.5, 5])
    with col_filtre1:
        secili_cinsiyet = st.selectbox("Cinsiyet", ["Tümü", "Kadın", "Erkek", "Unisex"])
    with col_filtre2:
        sirala = st.selectbox("Sırala", ["Önerilen", "Fiyat: Düşükten Yükseğe", "Fiyat: Yüksekten Düşüğe"])
    
    st.markdown("<hr style='border: none; border-bottom: 1px solid #eaeaea; margin-top: 10px; margin-bottom: 30px;'>", unsafe_allow_html=True)

    # Verileri Filtreleme
    gosterilecek_urunler = []
    for u in URUNLER:
        if st.session_state.secili_marka != "Tümü" and u["marka"] != st.session_state.secili_marka:
            continue
        if secili_cinsiyet != "Tümü" and u["cinsiyet"] != secili_cinsiyet:
            continue
        gosterilecek_urunler.append(u)
        
    # Verileri Sıralama
    if sirala == "Fiyat: Düşükten Yükseğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"])
    elif sirala == "Fiyat: Yüksekten Düşüğe":
        gosterilecek_urunler.sort(key=lambda x: x["fiyat"], reverse=True)

    # Ürünleri Sergileme
    if len(gosterilecek_urunler) == 0:
        st.warning("Seçili filtrelere uygun ürün bulunmamaktadır.")
    else:
        cols = st.columns(4, gap="large")
        for i, urun in enumerate(gosterilecek_urunler):
            with cols[i % 4]:
                st.image(urun["resim"])
                st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
                st.markdown('<div class="u-desc">{} | {}</div>'.format(urun["model"], urun["cinsiyet"]), unsafe_allow_html=True)
                st.markdown('<div class="u-fiyat">{:,} TL</div>'.format(urun["fiyat"]).replace(",", "."), unsafe_allow_html=True)
                
                # Siyah ve güçlü buton
                if st.button("SEPETE EKLE", key="ekle_{}".format(urun['id']), type="primary"):
                    sepete_ekle(urun)
                    st.toast("{} sepete eklendi!".format(urun['marka']))
                    st.rerun()

elif st.session_state.aktif_sayfa == "markalar":
    st.markdown("<h2 style='text-align:center; font-family: \"Playfair Display\", serif; margin-top: 50px; margin-bottom: 40px;'>Markalarımız</h2>", unsafe_allow_html=True)
    
    cols = st.columns(4, gap="large")
    for i, marka in enumerate(MARKALAR):
        with cols[i % 4]:
            st.image(marka["logo"], use_container_width=True)
            st.write("")
            if st.button("{} Koleksiyonu".format(marka["isim"]), key="marka_btn_{}".format(i)):
                # Markaya tıklandığında vitrin sayfasına yönlendirip, seçili markayı o marka yapıyor!
                sayfaya_git("vitrin", marka["isim"])
                st.rerun()

elif st.session_state.aktif_sayfa == "sepet":
    st.markdown("<h2 style='text-align:center; font-family: \"Playfair Display\", serif; margin-top: 50px; margin-bottom: 40px;'>Sepetim</h2>", unsafe_allow_html=True)
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
