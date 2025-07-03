# from PIL import Image
# import img2pdf
# import os
#
# def images_to_pdf(image_paths, pdf_path):
#     pdf_bytes = img2pdf.convert([Image.open(img).filename for img in image_paths])
#     with open(pdf_path, "wb") as file:
#         file.write(pdf_bytes)
#
# image_files = os.listdir("patram")
# images_to_pdf(image_files, "output.pdf")


import streamlit as st
from PIL import Image
import img2pdf
import os
from io import BytesIO

st.set_page_config(page_title="Image to PDF Converter", page_icon="📄")

st.title("🖼️ Image to PDF Converter")
st.write("Upload your images below to convert them into a single PDF.")

uploaded_files = st.file_uploader("Choose image files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.write("### Uploaded Images:")
    images = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        images.append(image)
        st.image(image, caption=uploaded_file.name, use_column_width=True)

    if st.button("Convert to PDF"):
        image_bytes_list = []
        for img in images:
            img_io = BytesIO()
            rgb_img = img.convert("RGB")  # Ensure it's in RGB mode
            rgb_img.save(img_io, format='JPEG')
            img_io.seek(0)
            image_bytes_list.append(img_io.read())

        pdf_bytes = img2pdf.convert(image_bytes_list)
        st.success("✅ PDF generated successfully!")

        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="converted_output.pdf",
            mime="application/pdf"
        )
