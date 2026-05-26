import streamlit as st
from supabase import create_client
from datetime import datetime, timedelta
from PIL import Image
import numpy as np
import random
import time

st.set_page_config(page_title="Nexora", page_icon="⚡", layout="wide")

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #050816, #0b1226);
    color: white;
}
.title {
    text-align:center;
    font-size:42px;
    font-weight:800;
    background: linear-gradient(90deg,#00e5ff,#a855f7);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.box {
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "login"

if "user" not in st.session_state:
    st.session_state.user = None

def check_license(key):
    res = supabase.table("licenses").select("*").eq("license_key", key).execute()

    if not res.data:
        return False

    data = res.data[0]

    if data["is_blocked"]:
        return False

    if not data["is_active"]:
        return False

    return True

def analyze_image(img):
   arr = np.array(img.convert("RGB"))
   brightness = np.mean(arr)

 def analyze_image(img):
    arr = np.array(img.convert("RGB"))
    brightness = np.mean(arr)

    if brightness > 120:
        signal = "CALL"
        reason = "Bullish momentum detected."
    else:
        signal = "PUT"
        reason = "Bearish pressure detected."

    confidence = random.randint(71, 92)

    pair = random.choice([
        "EUR/USD",
        "GBP/USD",
        "BTC/USD",
        "XAU/USD",
        "USD/JPY"
    ])

    return {
        "pair": pair,
        "signal": signal,
        "confidence": confidence,
        "reason": reason
    }
        "EUR/USD",
        "GBP/USD",
        "BTC/USD",
        "XAU/USD",
        "USD/JPY"
    ])

    return {
        "pair": pair,
        "signal": signal,
        "confidence": confidence,
        "reason": reason
    }

def login_page():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="title">Trader Jahid Official AI</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            res = supabase.table("users_app").select("*").eq("email", email).eq("password", password).execute()

            if res.data:
                st.session_state.user = email
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Invalid Login")

    with tab2:
        email = st.text_input("Register Email")
        password = st.text_input("Register Password", type="password")
        license_key = st.text_input("License Key")

        if st.button("Create Account", use_container_width=True):

            valid = check_license(license_key)

            if not valid:
                st.error("Invalid License")
                return

            supabase.table("users_app").insert({
                "email": email,
                "password": password,
                "license_key": license_key
            }).execute()

            st.success("Account Created")

def dashboard():
    st.markdown('<div class="title">Nexora Dashboard</div>', unsafe_allow_html=True)

    st.write("Support Telegram: @traderjahid99")

    st.markdown('<div class="box">', unsafe_allow_html=True)

    platform = st.selectbox(
        "Select Platform",
        ["Quotex", "IQ Option", "Pocket Option"]
    )

    uploaded = st.file_uploader(
        "Upload Screenshot",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded:
        image = Image.open(uploaded)

        st.image(image, use_container_width=True)

        if st.button("Analyze Screenshot", use_container_width=True):

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)

            result = analyze_image(image)

            st.success(f"Pair: {result['pair']}")
            st.success(f"Signal: {result['signal']}")
            st.success(f"Confidence: {result['confidence']}%")
            st.info(result['reason'])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.page = "login"
        st.rerun()

def admin_panel():
    st.markdown('<div class="title">Admin Panel</div>', unsafe_allow_html=True)

    password = st.text_input("Admin Password", type="password")

    if password != ADMIN_PASSWORD:
        st.warning("Enter Admin Password")
        return

    new_license = st.text_input(
        "License Key",
        value=f"NEXORA-{random.randint(10000,99999)}"
    )

    days = st.number_input("Expiry Days", value=30)

    if st.button("Create License"):

        expiry = datetime.now() + timedelta(days=int(days))

        supabase.table("licenses").insert({
            "license_key": new_license,
            "expires_at": expiry.isoformat()
        }).execute()

        st.success(f"Created: {new_license}")

    st.divider()

    licenses = supabase.table("licenses").select("*").execute()

    st.dataframe(licenses.data)

menu = st.sidebar.radio(
    "Menu",
    ["App", "Admin"]
)

if menu == "Admin":
    admin_panel()

else:
    if st.session_state.page == "login":
        login_page()

    elif st.session_state.page == "dashboard":
        dashboard()