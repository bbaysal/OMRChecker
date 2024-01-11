from pathlib import Path
import streamlit as st

from src.entry import entry_point

st.header(body="OMR Reader", divider="grey")
st.write("OMR Checker programına hoşgeldiniz.")
st.write(
    "Öncelikle template.json dosyasının ve taranmış dosyaların olduğu klasörü seçiniz.."
)

input_folder_path = st.text_input("Input Klasörünü Belirleyiniz:")
output_folder_path = st.text_input("Output Klasörünü Belirleyiniz:")

def evaluate_func():
    input_paths = ["inputs"]
    debug = True
    output_dir = output_folder_path
    autoAlign = False
    setLayout = False

    config = {
        "input_paths": input_paths,
        "debug": debug,
        "output_dir": output_dir,
        "autoAlign": autoAlign,
        "setLayout": setLayout,
    }
    entry_point(Path(input_folder_path), config)

if st.button(label="Değerlendir.", on_click=evaluate_func, type="primary"):
    st.write("Değerlendirme tamamlamıştır.")
