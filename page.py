import streamlit as st
from streamlit_option_menu import option_menu

# 1. Navigasi Sidebar
with st.sidebar:
    selected = option_menu("Perhitungan Digital untuk ANFIS", ['Hitung Kuat Tekan','Hitung Melting Point'], 
       default_index=1)

#Halaman Hitung Kuat Tekan
if (selected == 'Hitung Kuat Tekan') :
    st.title('Perhitungan Kuat Tekan')

    import streamlit as st

    st.subheader('a. Perhitungan Luas Sampel')

    Panjang = st.number_input('Masukkan Panjang Sampel (cm)')
    Lebar = st.number_input('Masukkan Lebar Sampel (cm')

    tombol = st.button('Hitung Luas Sampel')


    if tombol:
        luas_sampel = (Panjang*Lebar)/10000
        st.success(f'Nilai Luas Sampel (m^2) adalah {luas_sampel}')


    import streamlit as st

    st.subheader('b. Perhitungan Gaya Tekan')

    massa = st.number_input('Masukkan Massa Tekan (Kg)')
    gravitasi = st.number_input('Masukkan Percepatan Gravitasi (m^2)')

    tombol = st.button('Hitung Gaya Tekan')

    if tombol:
        gaya_tekan = massa*gravitasi
        st.success(f'Nilai Gaya Tekan (N) adalah {gaya_tekan}')

    import streamlit as st

    st.subheader('c. Perhitungan Kuat Tekan')

    gaya_tekan = st.number_input('Masukkan Gaya Tekan (N)')
    luas_sampel = st.number_input('Masukkan Luas Sampel (m^2)')

    tombol = st.button('Hitung Kuat Tekan')

    if tombol:
        kuat_tekan = gaya_tekan/luas_sampel
        st.success(f'Nilai Kuat Tekan (N/m^2) adalah {kuat_tekan}')

#Halaman Hitung Melting Point
if (selected == 'Hitung Melting Point') :
    st.title('Perhitungan Melting Point')
    
    import streamlit as st
    
    Fmelt = st.slider ('Masukkan Nilai Suhu',0,200)
    Smelt = st.slider ('Masukkan Niai Suhu',0,200)
    
    tombol = st.button ('Hitung Delta F')
    
    if tombol :
        Delta_F = Fmelt-Smelt
        st.success (f'Delta F yang diperoleh = {Delta_F}')
        

                            

   



