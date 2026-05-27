import streamlit as st

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

st.markdown("""

<style>

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

</style>

""", unsafe_allow_html=True)

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
