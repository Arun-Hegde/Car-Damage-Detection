import streamlit as st
from model_helper import predict
from PIL import Image
import time

# Page setup
st.set_page_config(page_title="Vehicle Damage Detection", page_icon="🚘", layout="centered")

# --- Custom Dark Theme Styling ---
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stApp {
            background-color: #0E1117;
            color: #E0E0E0;
        }
        h1, h2, h3, h4 {
            color: #00BFFF;
        }
        .css-1cpxqw2, .css-12oz5g7 {
            color: #E0E0E0 !important;
        }
        .uploaded-image {
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.4);
            margin-top: 10px;
        }
        .prediction-box {
            background-color: #1A1F25;
            padding: 15px;
            border-radius: 12px;
            border-left: 5px solid #00BFFF;
            box-shadow: 0px 0px 15px rgba(0, 191, 255, 0.3);
            margin-top: 20px;
        }
        .stFileUploader label {
            color: #FAFAFA !important;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #00BFFF;
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #009ACD;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='text-align:center;'>🚘 Vehicle Damage Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#CCCCCC;'>Upload a vehicle image to detect and classify damage using AI.</p>", unsafe_allow_html=True)

# --- File Upload ---
uploaded_file = st.file_uploader("📁 Upload a Vehicle Image", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True, output_format="auto")

    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🔍 Analyzing image... please wait"):
        time.sleep(1)  # Optional delay for user experience
        prediction = predict(image_path)

    # --- Display Prediction ---
    st.markdown(f"""
        <div class="prediction-box">
            <h4>🧠 Predicted Class:</h4>
            <h2 style='color:#00BFFF;'>{prediction}</h2>
        </div>
    """, unsafe_allow_html=True)

else:
    st.info("👆 Please upload a JPG or PNG image to start detection.")
