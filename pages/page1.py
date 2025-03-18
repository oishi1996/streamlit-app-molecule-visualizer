import streamlit as st
import py3Dmol
import io
from PIL import Image

# Py3Dmol ビューを作成
def create_3Dmol_view():
    viewer = py3Dmol.view(width=300, height=300)
    viewer.addModel("CCO", "smi")  # SMILES 形式のエタノール
    viewer.setStyle({"stick": {}})
    viewer.zoomTo()
    return viewer

# Streamlit アプリ
st.title("Py3Dmol PNG Test")

# Py3Dmol ビューを作成
viewer = create_3Dmol_view()

# Py3Dmol を表示
st.text("3D Visualization:")
st.components.v1.html(viewer._make_html(), height=300, width=300)

# 画像を取得
st.text("Checking if PNG output is available...")
try:
    img_data = viewer.png()  # PNG 画像を取得
    if img_data:
        st.success("✅ PNG image successfully retrieved!")
        
        # 画像を表示
        img = Image.open(io.BytesIO(img_data))
        st.image(img, caption="Generated PNG from Py3Dmol")

        # 画像ダウンロード
        st.download_button(
            label="Download 3D Image",
            data=img_data,
            file_name="3D_molecule.png",
            mime="image/png"
        )
    else:
        st.error("❌ PNG image retrieval failed. `viewer.png()` returned None.")
except Exception as e:
    st.error(f"❌ PNG image retrieval error: {e}")
