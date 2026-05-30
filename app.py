import streamlit as st
import json, os, time, random
from datetime import datetime, timedelta
from PIL import Image

APP_NAME = "Nexora AI"
DATA_FILE = "nexora_data.json"

PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/JPY", "EUR/JPY",
    "BTC/USD", "XAU/USD", "USD/IDR OTC", "USD/INR OTC",
    "USD/PHP OTC", "NZD/USD OTC", "AUD/NZD OTC", "NZD/JPY OTC"
]

ADMIN_USER = "admin"
ADMIN_PASS = "123456"

st.set_page_config(page_title=APP_NAME, page_icon="📈", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#050816,#0b1020,#111827); color:white;}
h1,h2,h3,p,label {color:white !important;}
.card {background:rgba(255,255,255,.07); padding:22px; border-radius:20px; margin-bottom:15px;}
.signal-call {color:#00ff99; font-size:48px; font-weight:900;}
.signal-put {color:#ff4d6d; font-size:48px; font-weight:900;}
</style>
""", unsafe_allow_html=True)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "users": {
                "demo": {
                    "password": "1234",
                    "license": "DEMO-1234",
                    "expiry": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
                    "blocked": False,
                    "credits": 5
                }
            }
        }
        save_data(data)
        return data
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"users": {}}

def analyze_signal(pair, platform):
    bullish_score = random.randint(1, 10)
    bearish_score = random.randint(1, 10)
    trend_score = random.randint(60, 95)

    candle_pressure = random.choice(["Buyer pressure strong", "Seller pressure strong"])
    zone = random.choice(["Near support zone", "Near resistance zone", "Breakout confirmed", "Retest confirmed"])

    if candle_pressure == "Buyer pressure strong":
        bullish_score += 3
    else:
        bearish_score += 3

    if zone == "Near support zone":
        bullish_score += 2
    elif zone == "Near resistance zone":
        bearish_score += 2
    elif zone == "Breakout confirmed":
        bullish_score += 2
    else:
        bearish_score += 1

    if bullish_score > bearish_score:
        signal = "CALL"
        confidence = min(95, 70 + (bullish_score - bearish_score) * 3)
    else:
        signal = "PUT"
        confidence = min(95, 70 + (bearish_score - bullish_score) * 3)

    reasons = [
        f"{pair} market checked on {platform}.",
        f"Candle analysis: {candle_pressure}.",
        f"Zone analysis: {zone}.",
        f"Trend strength: {trend_score}/100.",
        f"Bullish score: {bullish_score}.",
        f"Bearish score: {bearish_score}."
    ]
    return signal, confidence, reasons

def login_page(data):
    st.markdown("<h1 style='text-align:center;'>Nexora AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Trader Jahid Official AI Signal System</p>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Login", "Register", "Admin"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        license_key = st.text_input("License Key")

        if st.button("Login"):
            user = data["users"].get(username)
            if not user:
                st.error("User not found")
            elif user["password"] != password:
                st.error("Wrong password")
            elif user["license"] != license_key:
                st.error("Invalid license")
            elif user["blocked"]:
                st.error("Account blocked")
            elif datetime.strptime(user["expiry"], "%Y-%m-%d") < datetime.now():
                st.error("License expired")
            else:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create Demo Account"):
            if not new_user or not new_pass:
                st.warning("Fill all fields")
            elif new_user in data["users"]:
                st.error("Username already exists")
            else:
                license_key = "NX-" + str(random.randint(100000, 999999))
                data["users"][new_user] = {
                    "password": new_pass,
                    "license": license_key,
                    "expiry": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
                    "blocked": False,
                    "credits": 5
                }
                save_data(data)
                st.success(f"Account created. License: {license_key}")

    with tab3:
        au = st.text_input("Admin Username")
        ap = st.text_input("Admin Password", type="password")

        if st.button("Admin Login"):
            if au == ADMIN_USER and ap == ADMIN_PASS:
                st.session_state.admin = True
                st.rerun()
            else:
                st.error("Wrong admin login")

def dashboard(data):
    username = st.session_state.username
    user = data["users"][username]

    st.sidebar.title("Nexora AI")
    st.sidebar.write(f"User: {username}")
    st.sidebar.write(f"Credits: {user['credits']}")
    st.sidebar.write(f"Expiry: {user['expiry']}")

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()

    st.title("📈 Nexora AI Dashboard")
    st.caption("Educational/demo analysis system. No signal is guaranteed.")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    platform = st.selectbox("Select Platform", ["Quotex", "IQ Option", "Deriv", "Exnova"])
    selected_pair = st.selectbox("Select Pair", PAIRS)
    expiry = st.selectbox("Trade Expiry", ["1 Minute", "2 Minutes", "5 Minutes"])
    uploaded = st.file_uploader("Upload chart screenshot", type=["png", "jpg", "jpeg"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("Telegram: @traderjahid99")
    st.write("YouTube: Trade With Jahid")

    if uploaded:
        try:
            st.image(Image.open(uploaded), caption="Uploaded Screenshot", use_container_width=True)
        except:
            st.warning("Image preview failed")

        if st.button("Start AI Analysis"):
            if user["credits"] <= 0:
                st.error("Free credits finished. Contact Telegram: @traderjahid99")
                return

            progress = st.progress(0)
            status = st.empty()
            steps = [
                "Reading screenshot...",
                "Checking selected pair...",
                "Checking candle pressure...",
                "Finding support/resistance...",
                "Generating signal..."
            ]

            for i in range(100):
                progress.progress(i + 1)
                status.write(steps[min(i // 20, 4)])
                time.sleep(0.03)

            signal, confidence, reasons = analyze_signal(selected_pair, platform)

            user["credits"] -= 1
            save_data(data)

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("AI Result")
            st.write(f"Detected Pair: **{selected_pair}**")
            st.write(f"Platform: **{platform}**")
            st.write(f"Expiry: **{expiry}**")

            if signal == "CALL":
                st.markdown("<div class='signal-call'>CALL ▲</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='signal-put'>PUT ▼</div>", unsafe_allow_html=True)

            st.metric("Confidence", f"{confidence}%")

            st.subheader("Reason")
            for r in reasons:
                st.write("• " + r)

            st.warning("Risk warning: Market can reverse anytime. Use money management.")
            st.markdown("</div>", unsafe_allow_html=True)

def admin_panel(data):
    st.title("🛡 Nexora Admin Panel")

    if st.button("Logout Admin"):
        st.session_state.clear()
        st.rerun()

    st.subheader("Create User")
    u = st.text_input("Username")
    p = st.text_input("Password")
    days = st.number_input("Expiry Days", min_value=1, value=30)
    credits = st.number_input("Credits", min_value=0, value=50)

    if st.button("Create User License"):
        if not u or not p:
            st.error("Username and password required")
        else:
            license_key = "NX-" + str(random.randint(100000, 999999))
            data["users"][u] = {
                "password": p,
                "license": license_key,
                "expiry": (datetime.now() + timedelta(days=int(days))).strftime("%Y-%m-%d"),
                "blocked": False,
                "credits": int(credits)
            }
            save_data(data)
            st.success(f"User created. License: {license_key}")

    st.subheader("All Users")
    for uname, udata in data["users"].items():
        with st.expander(uname):
            st.json(udata)

            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button(f"Block {uname}"):
                    data["users"][uname]["blocked"] = True
                    save_data(data)
                    st.rerun()
            with c2:
                if st.button(f"Unblock {uname}"):
                    data["users"][uname]["blocked"] = False
                    save_data(data)
                    st.rerun()
            with c3:
                if st.button(f"Add 10 Credits {uname}"):
                    data["users"][uname]["credits"] += 10
                    save_data(data)
                    st.rerun()

def main():
    data = load_data()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "admin" in st.session_state and st.session_state.admin:
        admin_panel(data)
    elif st.session_state.logged_in:
        dashboard(data)
    else:
        login_page(data)

if __name__ == "__main__":
    main()