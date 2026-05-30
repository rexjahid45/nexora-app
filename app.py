import streamlit as st
<<<<<<< HEAD

import random

import time

from datetime import datetime, timedelta

st.set_page_config(

    page_title="Nexora AI",

    page_icon="⚡",

    layout="wide"

)

TELEGRAM = "https://t.me/traderjahid99"

AFFILIATE_LINK = "https://example.com"  # ekhane tomar affiliate link dao

PAIRS = {

    "Currencies": [

        "USD/IDR (OTC)", "USD/INR (OTC)", "NZD/USD (OTC)", "USD/PHP (OTC)",

        "AUD/NZD (OTC)", "USD/JPY", "AUD/JPY", "EUR/JPY", "NZD/JPY (OTC)",

        "USD/BRL (OTC)", "AUD/CAD", "AUD/USD", "GBP/USD", "USD/BDT (OTC)",

        "USD/PKR (OTC)", "EUR/CAD", "EUR/GBP", "NZD/CHF (OTC)", "AUD/CHF",

        "GBP/AUD", "USD/ARS (OTC)", "USD/EGP (OTC)", "USD/NGN (OTC)",

        "CAD/JPY", "USD/CAD", "GBP/CAD", "USD/MXN (OTC)", "CAD/CHF (OTC)",

        "USD/CHF", "NZD/CAD (OTC)", "GBP/JPY", "CHF/JPY", "USD/COP (OTC)",

        "EUR/CHF", "USD/DZD (OTC)", "EUR/AUD", "GBP/CHF", "EUR/NZD (OTC)",

        "GBP/NZD (OTC)", "EUR/USD", "USD/ZAR (OTC)"

    ],

    "Stocks / Index": [

        "American Express (OTC)", "FACEBOOK INC (OTC)", "Intel (OTC)",

        "Pfizer Inc (OTC)", "Microsoft (OTC)", "Boeing Company (OTC)",

        "Johnson & Johnson (OTC)", "McDonald’s (OTC)", "S&P/ASX 200",

        "FTSE China A50 Index", "CAC 40", "FTSE 100", "Hong Kong 50",

        "IBEX 35", "Nikkei 225", "EURO STOXX 50"

    ],

    "Crypto": [

        "Avalanche (OTC)", "Binance Coin (OTC)", "Bitcoin (OTC)",

        "Polkadot (OTC)", "Chainlink (OTC)", "Solana (OTC)", "Toncoin (OTC)",

        "Trump (OTC)", "Ripple (OTC)", "Zcash (OTC)", "Litecoin (OTC)",

        "Ethereum (OTC)", "Dash (OTC)", "Axie Infinity (OTC)",

        "Bitcoin Cash (OTC)", "Ethereum Classic (OTC)"

    ],

    "Commodities": ["UKBrent (OTC)", "USCrude (OTC)", "Silver", "Gold"]

}

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "credits" not in st.session_state:

    st.session_state.credits = 5

if "history" not in st.session_state:

    st.session_state.history = []
=======
import json, os, time, random
from datetime import datetime, timedelta
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
>>>>>>> 707136a (Nexora OCR Update)

st.markdown("""

<style>
<<<<<<< HEAD

.stApp {

    background: linear-gradient(135deg, #060814, #111827, #020617);

    color: white;

}

.big-title {

    font-size: 48px;

    font-weight: 900;

    color: #ffffff;

}

.sub {

    color: #93c5fd;

    font-size: 18px;

}

.card {

    background: rgba(15, 23, 42, 0.85);

    padding: 22px;

    border-radius: 22px;

    border: 1px solid rgba(59, 130, 246, 0.35);

    box-shadow: 0 0 25px rgba(37,99,235,0.18);

}

.signal-call {

    color: #22c55e;

    font-size: 42px;

    font-weight: 900;

}

.signal-put {

    color: #ef4444;

    font-size: 42px;

    font-weight: 900;

}

.no-trade {

    color: #f59e0b;

    font-size: 38px;

    font-weight: 900;

}

.support {

    background: linear-gradient(135deg, #0f172a, #1e3a8a);

    padding: 20px;

    border-radius: 20px;

    border: 1px solid #38bdf8;

}

=======
.stApp {background: linear-gradient(135deg,#050816,#0b1020,#111827); color:white;}
h1,h2,h3,p,label {color:white !important;}
.signal-call {color:#00ff99; font-size:48px; font-weight:900;}
.signal-put {color:#ff4d6d; font-size:48px; font-weight:900;}
>>>>>>> 707136a (Nexora OCR Update)
</style>

""", unsafe_allow_html=True)

<<<<<<< HEAD
def login_page():

    st.markdown('<div class="big-title">⚡ Nexora AI</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub">Premium Market Intelligence by Trader Jahid</div>', unsafe_allow_html=True)

    st.write("")

    with st.container():

        st.markdown('<div class="card">', unsafe_allow_html=True)

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        license_key = st.text_input("License Key")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Login", use_container_width=True):

                if email and password:

                    st.session_state.logged_in = True

                    st.session_state.email = email

                    st.rerun()

                else:

                    st.error("Email and password required.")

        with col2:

            if st.button("Create Account", use_container_width=True):

                if email and password:

                    st.session_state.logged_in = True

                    st.session_state.email = email

                    st.session_state.credits = 5

                    st.success("Account created. 5 free credits added.")

                    st.rerun()

                else:

                    st.error("Email and password required.")

        st.markdown('</div>', unsafe_allow_html=True)

def generate_signal(pair, category):

    market_percent = random.randint(72, 94)

    weak_reasons = [

        "Weak candle pressure",

        "Low market momentum",

        "Sideways market",

        "Unclear support/resistance reaction",

        "False breakout risk"

    ]

    if market_percent < 80 or market_percent > 92:

        return {

            "signal": "NO TRADE",

            "confidence": market_percent,

            "reason": random.choice(weak_reasons),

            "details": "Market filter failed. Signal skipped for safety."

        }

    signal = random.choice(["CALL", "PUT"])

    reasons_call = [

        "Support zone reaction + bullish candle pressure",

        "Breakout confirmation with uptrend momentum",

        "Smart money buy pressure detected",

        "Price action shows higher high structure",

        "Strong bullish rejection from demand zone"

    ]

    reasons_put = [

        "Resistance zone rejection + bearish candle pressure",

        "Breakdown confirmation with downtrend momentum",

        "Smart money sell pressure detected",

        "Price action shows lower low structure",

        "Strong bearish rejection from supply zone"

    ]

    return {

        "signal": signal,

        "confidence": market_percent,

        "reason": random.choice(reasons_call if signal == "CALL" else reasons_put),

        "details": f"{category} market scanned: support/resistance, trend, breakout, candle pressure, price action, SMC."

    }

def dashboard():

    st.markdown('<div class="big-title">Nexora AI Dashboard</div>', unsafe_allow_html=True)

    st.markdown(f"Logged in: **{st.session_state.get('email','user')}**")

    st.write("")

    c1, c2, c3 = st.columns(3)

    c1.metric("Credits", st.session_state.credits)

    c2.metric("License", "Active")

    c3.metric("Expiry", "30 Days")

    if st.session_state.credits <= 0:

        st.error("Your free credits are finished.")

        st.link_button("Get More Credits", AFFILIATE_LINK, use_container_width=True)

        st.link_button("Contact Admin on Telegram", TELEGRAM, use_container_width=True)

        return

    st.markdown("### 📊 Market Analysis")

    platform = st.selectbox("Platform", ["Quotex", "IQ Option", "Deriv"])

    category = st.selectbox("Market Category", list(PAIRS.keys()))

    pair = st.selectbox("Select Pair", PAIRS[category])

    image = st.file_uploader("Upload screenshot taken within 25–30 seconds", type=["png", "jpg", "jpeg"])

    if st.button("Analyze Screenshot", use_container_width=True):

        if image is None:

            st.warning("Please upload a screenshot first.")

            return

        with st.spinner("AI scanning support/resistance, candle pressure, trend and SMC..."):

            time.sleep(random.randint(7, 10))

        result = generate_signal(pair, category)

        st.session_state.credits -= 1

        st.markdown('<div class="card">', unsafe_allow_html=True)

        if result["signal"] == "CALL":

            st.markdown('<div class="signal-call">CALL ⬆️</div>', unsafe_allow_html=True)

        elif result["signal"] == "PUT":

            st.markdown('<div class="signal-put">PUT ⬇️</div>', unsafe_allow_html=True)

        else:

            st.markdown('<div class="no-trade">NO TRADE ⚠️</div>', unsafe_allow_html=True)

        st.write(f"**Pair:** {pair}")

        st.write(f"**Platform:** {platform}")

        st.write(f"**Market Strength:** {result['confidence']}%")

        st.write(f"**Reason:** {result['reason']}")

        st.write(f"**Details:** {result['details']}")

        st.warning("Risk note: No signal is guaranteed. If loss happens, use maximum 1-step MTG only with proper risk management.")

        st.markdown('</div>', unsafe_allow_html=True)

        st.session_state.history.insert(0, {

            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),

            "pair": pair,

            "signal": result["signal"],

            "confidence": result["confidence"]

        })

    st.markdown("### 🧾 Signal History")

    if st.session_state.history:

        st.dataframe(st.session_state.history, use_container_width=True)

    else:

        st.info("No signal history yet.")

    st.markdown("### 💬 Support")

    st.markdown('<div class="support">', unsafe_allow_html=True)

    st.write("Need support or more credits?")

    st.link_button("Telegram @traderjahid99", TELEGRAM, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

if st.session_state.logged_in:

    dashboard()

else:

    login_page()
=======

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

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def detect_pair(uploaded_file, selected_pair):
    try:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image).upper()

        clean_text = (
            text.replace("/", "")
            .replace("-", "")
            .replace("_", "")
            .replace(" ", "")
            .replace("|", "")
            .replace(".", "")
            .replace("OTC", "")
        )

        if "USDPHP" in clean_text or "USDPH" in clean_text or "USDP" in clean_text:
            return "USD/PHP OTC", text[:500]

        pair_map = {
            "USDIDR": "USD/IDR OTC",
            "USDINR": "USD/INR OTC",
            "NZDUSD": "NZD/USD OTC",
            "AUDNZD": "AUD/NZD OTC",
            "NZDJPY": "NZD/JPY OTC",
            "XAUUSD": "XAU/USD",
            "BTCUSD": "BTC/USD",
            "GBPUSD": "GBP/USD",
            "EURUSD": "EUR/USD",
            "USDJPY": "USD/JPY",
            "AUDJPY": "AUD/JPY",
            "EURJPY": "EUR/JPY",
        }

        for key, value in pair_map.items():
            if key in clean_text:
                return value, text[:500]

        return selected_pair, text[:500]

    except Exception as e:
        return selected_pair, f"OCR failed: {e}"


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
            else:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create Demo Account"):
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

    platform = st.selectbox("Select Platform", ["Quotex", "IQ Option", "Deriv", "Exnova"])
    selected_pair = st.selectbox("Manual Pair Backup", PAIRS)
    expiry = st.selectbox("Trade Expiry", ["1 Minute", "2 Minutes", "5 Minutes"])
    uploaded = st.file_uploader("Upload chart screenshot", type=["png", "jpg", "jpeg"])

    st.write("Telegram: @traderjahid99")
    st.write("YouTube: Trade With Jahid")

    if uploaded:
        st.image(Image.open(uploaded), caption="Uploaded Screenshot", use_container_width=True)

        if st.button("Start AI Analysis"):
            if user["credits"] <= 0:
                st.error("Free credits finished. Contact Telegram: @traderjahid99")
                return

            progress = st.progress(0)
            status = st.empty()

            steps = [
                "Reading screenshot...",
                "Running OCR pair detection...",
                "Checking candle pressure...",
                "Finding support/resistance...",
                "Generating signal..."
            ]

            for i in range(100):
                progress.progress(i + 1)
                status.write(steps[min(i // 20, 4)])
                time.sleep(0.03)

            uploaded.seek(0)
            detected_pair, ocr_text = detect_pair(uploaded, selected_pair)
            signal, confidence, reasons = analyze_signal(detected_pair, platform)

            user["credits"] -= 1
            save_data(data)

            st.subheader("AI Result")
            st.write(f"Detected Pair: **{detected_pair}**")
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

            with st.expander("OCR Text Preview"):
                st.text(ocr_text)

            st.warning("Risk warning: Market can reverse anytime. Use money management.")


def admin_panel(data):
    st.title("🛡 Nexora Admin Panel")

    if st.button("Logout Admin"):
        st.session_state.clear()
        st.rerun()

    st.subheader("All Users")
    for uname, udata in data["users"].items():
        with st.expander(uname):
            st.json(udata)

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
>>>>>>> 707136a (Nexora OCR Update)
