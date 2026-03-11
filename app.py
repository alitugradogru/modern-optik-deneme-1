import streamlit as st

# --- 1. AYARLAR & HAFIZA ---
st.set_page_config(page_title="Modern Optik | Özel Koleksiyon", page_icon="🕶️", layout="wide", initial_sidebar_state="collapsed")

if 'sepet' not in st.session_state:
    st.session_state.sepet = []
if 'aktif_sayfa' not in st.session_state:
    st.session_state.aktif_sayfa = "vitrin"

def sayfaya_git(sayfa_adi):
    st.session_state.aktif_sayfa = sayfa_adi

def sepete_ekle(urun):
    st.session_state.sepet.append(urun)

def sepetten_cikar(index):
    st.session_state.sepet.pop(index)

# --- 2. GERÇEK SİTE MİMARİSİ (CSS) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');

:root { color-scheme: light; }
[data-testid="stAppViewContainer"], .stApp { background-color: #FFFFFF !important; color: #000 !important; font-family: 'Jost', sans-serif; }
header {visibility: hidden;} footer {visibility: hidden;}

.navbar { display: flex; justify-content: space-between; align-items: center; padding: 25px 60px; border-bottom: 1px solid #f0f0f0; margin-bottom: 40px;}
.nav-brand { font-family: 'Playfair Display', serif; font-size: 1.8rem; letter-spacing: 4px; text-transform: uppercase; font-weight: 500;}
.nav-links { font-size: 0.9rem; letter-spacing: 1px; text-transform: uppercase; color: #555; display: flex; gap: 30px; align-items: center;}

[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] { background: transparent !important; border: none !important; padding: 10px; }
img { width: 100%; object-fit: contain; mix-blend-mode: multiply; transition: transform 0.6s ease;}
img:hover { transform: scale(1.02); }

.u-isim { font-family: 'Playfair Display', serif; font-size: 1.5rem; text-align: center; margin-top: 15px; color: #000;}
.u-desc { font-size: 0.85rem; text-align: center; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;}
.u-fiyat { font-size: 1.1rem; text-align: center; color: #000; font-weight: 400; margin-top: 15px; margin-bottom: 25px;}

.stButton > button { width: 100%; border-radius: 0px !important; font-weight: 400; letter-spacing: 2px; color: #000 !important; background-color: transparent !important; border: 1px solid #000; padding: 12px; transition: all 0.3s ease; }
.stButton > button:hover { background-color: #000 !important; color: #fff !important; }

.sepet-baslik { font-family: 'Playfair Display', serif; font-size: 2.5rem; text-align: center; margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 20px;}
.sepet-ozet-kutu { background-color: #FAFAFA; padding: 40px; border: 1px solid #EAEAEA; }
.ozet-satir { display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 1.1rem; color: #555;}
.ozet-toplam { display: flex; justify-content: space-between; font-size: 1.4rem; font-weight: 500; color: #000; border-top: 2px solid #000; padding-top: 20px; margin-top: 20px; margin-bottom: 30px;}
</style>
""", unsafe_allow_html=True)

# --- 3. ÜST MENÜ (NAVBAR) ---
col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
with col_nav1:
    if st.button("VİTRİNE DÖN"):
        sayfaya_git("vitrin")
        st.rerun()
with col_nav2:
    st.markdown('<div class="nav-brand" style="text-align:center;">MODERN OPTİK</div>', unsafe_allow_html=True)
with col_nav3:
    buton_metni = "SEPETE GİT ({})".format(len(st.session_state.sepet))
    if st.button(buton_metni):
        sayfaya_git("sepet")
        st.rerun()

st.markdown("<hr style='margin-top: -15px; margin-bottom: 40px; border: none; border-bottom: 1px solid #eaeaea;'>", unsafe_allow_html=True)

# --- 4. SAYFA YÖNLENDİRİCİSİ ---
if st.session_state.aktif_sayfa == "vitrin":
    st.markdown('<img src="https://images.unsplash.com/photo-1589642380614-4a8c2147b857?auto=format&fit=crop&w=2000&q=80" style="width:100%; height:50vh; object-fit:cover; margin-bottom:50px;">', unsafe_allow_html=True)
    
    LUK_URUNLER = [
        {"id": "1", "marka": "Tom Ford", "model": "Graydon TF1213", "fiyat": "15.053", "resim": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=800&q=80"},
        {"id": "2", "marka": "Prada", "model": "SPR 17W", "fiyat": "14.445", "resim": "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=800&q=80"},
        {"id": "3", "marka": "Gucci", "model": "GG1505SK 002", "fiyat": "20.353", "resim": "https://images.unsplash.com/photo-1509695507497-903c140c43b0?auto=format&fit=crop&w=800&q=80"}
    ]

    cols = st.columns(3, gap="large")
    for i, urun in enumerate(LUK_URUNLER):
        with cols[i % 3]:
            st.image(urun["resim"])
            st.markdown('<div class="u-isim">{}</div>'.format(urun["marka"]), unsafe_allow_html=True)
            st.markdown('<div class="u-desc">{}</div>'.format(urun["model"]), unsafe_allow_html=True)
            st.markdown('<div class="u-fiyat">{} TL</div>'.format(urun["fiyat"]), unsafe_allow_html=True)
            
            if st.button("SEPETE EKLE", key="ekle_{}".format(urun['id'])):
                sepete_ekle(urun)
                st.toast("{} sepete eklendi!".format(urun['marka']))
                st.rerun()

elif st.session_state.aktif_sayfa == "sepet":
    st.markdown('<div class="sepet-baslik">Alışveriş Çantanız</div>', unsafe_allow_html=True)
    
    if len(st.session_state.sepet) == 0:
        st.info("Çantanızda henüz ürün bulunmamaktadır.")
        st.write("")
        if st.button("ALIŞVERİŞE DEVAM ET"):
            sayfaya_git("vitrin")
            st.rerun()
    else:
        col_urunler, col_ozet = st.columns([2, 1], gap="large")
        
        toplam_tutar = 0
        with col_urunler:
            for i, urun in enumerate(st.session_state.sepet):
                c1, c2, c3 = st.columns([1, 3, 1])
                with c1:
                    st.image(urun["resim"])
                with c2:
                    st.markdown("### {}".format(urun["marka"]))
                    st.markdown(urun["model"])
                with c3:
                    st.markdown("**{} TL**".format(urun["fiyat"]))
                    if st.button("Kaldır", key="sil_{}".format(i)):
                        sepetten_cikar(i)
                        st.rerun()
                st.markdown("---")
                toplam_tutar += float(urun['fiyat'].replace(".", "").replace(",", "."))
                
        with col_ozet:
            st.markdown('<div class="sepet-ozet-kutu">', unsafe_allow_html=True)
            st.markdown("### Sipariş Özeti")
            st.write("")
            st.markdown('<div class="ozet-satir"><span>Ara Toplam</span><span>{:,.0f} TL</span></div>'.format(toplam_tutar).replace(",", "."), unsafe_allow_html=True)
            st.markdown('<div class="ozet-satir"><span>Kargo (Sigortalı)</span><span>Ücretsiz</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="ozet-toplam"><span>Genel Toplam</span><span>{:,.0f} TL</span></div>'.format(toplam_tutar).replace(",", "."), unsafe_allow_html=True)
            
            if st.button("GÜVENLİ ÖDEMEYİ TAMAMLA"):
                st.success("Tebrikler! Müşteri bu aşamada kredi kartı ekranına yönlendirilecektir.")
                st.session_state.sepet = []
            st.markdown('</div>', unsafe_allow_html=True)
