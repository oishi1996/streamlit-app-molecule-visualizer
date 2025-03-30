import streamlit as st
import io
from rdkit import Chem
from rdkit.Chem import Draw

# 2D画像を保存する関数
def save_2D_image(mol):
    img = Draw.MolToImage(mol, size=(300, 300))  # RDKit の 2D 画像
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

# 入力
smiles = st.text_input("Enter a SMILES string:", "CCO")

if smiles:
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        # **2D画像のダウンロード機能**
        img_data = save_2D_image(mol)
        st.download_button(
            label="Download 2D Image",
            data=img_data,
            file_name="molecule_2D.png",
            mime="image/png"
        )
        st.image(img_data, caption="2D Molecular Structure")
