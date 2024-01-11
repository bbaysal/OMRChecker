from pathlib import Path
import streamlit as st
import tkinter as tk
from tkinter import filedialog

from src.entry import entry_point

header_container= st.container()
header_container.header(body="OMR Reader", divider="grey")

header_container.write("OMR Checker programına hoşgeldiniz.")
header_container.write(
    "Öncelikle template.json dosyasının ve taranmış dosyaların olduğu klasörü seçiniz.."
)

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(master=root)
    root.destroy()
    return folder_path

st.write(
    "Input"
)

input_folder_path = st.session_state.get("input_folder_path", None)
folder_select_button = st.button("Input Klasör Seç")
if folder_select_button:
    input_folder_path = select_folder()
    st.session_state.input_folder_path = input_folder_path

if input_folder_path:
    st.write("Seçilen klasör:", input_folder_path)

info_container= st.container()

def evaluate_func():
    input_paths = ["inputs"]
    debug = True
    output_dir = "outputs"
    autoAlign = False
    setLayout = False

    config = {
        "input_paths": input_paths,
        "debug": debug,
        "output_dir": output_dir,
        "autoAlign": autoAlign,
        "setLayout": setLayout,
    }
    try:
        entry_point(Path(input_folder_path), config, info_container)
        return True
    except:
        return False

if st.button(label="Değerlendir.", on_click=evaluate_func, type="primary"):
    st.write("Değerlendirme tamamlamıştır.")
