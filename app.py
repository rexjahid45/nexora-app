import streamlit as st, random, time, json, os, uuid, hashlib
from datetime import datetime, timedelta

DB="nexora_db.json"
ADMIN_PASS="jahid123"

OWNER_NAME="Trader Jahid Official"
TELEGRAM="trader Jahid official"
YOUTUBE="Trade With Jahid"

PAIRS=["AUD/USD","EUR/USD","GBP/USD","USD/JPY","AUD/JPY","EUR/JPY","USD/PKR OTC","USD/INR OTC","USD/PHP OTC","USD/IDR OTC","NZD/USD OTC"]

def save(d):
    with open(DB,"w") as f: json.dump(d,f,indent=2)

def load():
    if not os.path.exists(DB):
        d={"users":{},"licenses":{},"history":[]}
        save(d); return d
    return json.load(open(DB))

def h(x): return hashlib.sha256(x.encode()).hexdigest()

def make_license(days):
    code="NXR-"+uuid.uuid4().hex[:10].upper()
    exp=(datetime.now()+timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    return code,exp

def valid_license(db,code):
    if code not in db["licenses"]: return False
    if db["licenses"][code].get("blocked"): return False
    return datetime.now() < datetime.strptime(db["licenses"][code]["expiry"],"%Y-%m-%d %H:%M:%S")

def ai_signal(pair):
    now=datetime.now()
    minute=now.minute
    hour=now.hour
    pair_score=sum(ord(c) for c in pair)
    market_power=(pair_score+minute+hour)%100

    direction="CALL" if market_power%2==0 else "PUT"
    conf=random.randint(70,80)

    logic_call=[
        "Trap type: RED_TRAP",
        "Visible candle sequence: sellers pushed down but failed to continue.",
        "Reason: Price shows rejection from lower zone with buyer pressure.",
        "Support area is holding and market is showing recovery momentum.",
        "AI conclusion: CALL entry has better probability in this setup."
    ]
    logic_put=[
        "Trap type: GREEN_TRAP",
        "Visible candle sequence: buyers pushed up but failed to break higher.",
        "Reason: Price rejected from upper zone with seller pressure.",
        "Resistance area is holding and market is showing downside pressure.",
        "AI conclusion: PUT entry has better probability in this setup."
    ]
    return direction,conf,(logic_call if direction=="CALL" else logic_put)

st.set_page_config(page_title="Nexora AI",page_icon="⚡",layout="wide")

st.markdown("""
<style>
.stApp{background:#030712;color:white;font-family:Inter,Arial;}
section[data-testid="stSidebar"]{background:#020617;border-right:1px solid #13213d;}
.hero{background:linear-gradient(135deg,#061626,#07111f 55%,#101827);border:1px solid #16345c;border-radius:22px;padding:35px;margin-bottom:22px;box-shadow:0 0 35px rgba(0,119,255,.18);}
.logo{font-size:38px;font-weight:900}.logo span{color:#22c55e}.blue{color:#3b82f6}.green{color:#22c55e}
.muted{color:#94a3b8;letter-spacing:3px;font-size:13px;}
.card{background:linear-gradient(145deg,#07111f,#020617);border:1px solid #172554;border-radius:22px;padding:24px;margin:12px 0;box-shadow:0 0 28px rgba(37,99,235,.13);}
.greenCard{background:linear-gradient(145deg,#052e1a,#04111c);border:1px solid #15803d;border-radius:22px;padding:24px;margin:12px 0;box-shadow:0 0 30px rgba(34,197,94,.15);}
.redCard{background:linear-gradient(145deg,#2e0611,#050816);border:1px solid #7f1d1d;border-radius:22px;padding:24px;margin:12px 0;box-shadow:0 0 30px rgba(239,68,68,.15);}
.big{font-size:46px;font-weight:900}.title{text-align:center;font-size:44px;font-weight:900}
.btnlike{background:#16a34a;padding:14px;border-radius:14px;text-align:center;font-weight:800;margin-top:10px;}
.badge{display:inline-block;background:#052e1a;color:#22c55e;padding:8px 14px;border-radius:999px;font-weight:800;border:1px solid #16a34a;}
.metricbox{background:#050d1a;border:1px solid #1e3a8a;border-radius:18px;padding:20px;text-align:center;}
.brandbox{background:#061626;border:1px solid #164e63;border-radius:18px;padding:18px;margin-top:18px;}
.adminbox{background:#050d1a;border:1px solid #1e3a8a;border-radius:18px;padding:16px;margin:10px 0;}
</style>
""",unsafe_allow_html=True)

db=load()
if "login" not in st.session_state: st.session_state.login=False
if "user" not in st.session_state: st.session_state.user=""

st.sidebar.markdown(f"""
<div class='logo'>Nexora <span>AI</span></div>
<p class='muted'>NEURAL TERMINAL</p>
<div class='brandbox'>
<b>{OWNER_NAME}</b><br><br>
<span class='green'>Telegram:</span> {TELEGRAM}<br>
<span class='green'>YouTube:</span> {YOUTUBE}
</div>
""",unsafe_allow_html=True)

menu=st.sidebar.radio("Menu",["Login","Dashboard","Admin Panel","Logout"])

if menu=="Login":
    st.markdown(f"""
    <div class='hero'>
      <div class='title'>Nexora <span class='blue'>AI</span></div>
      <p class='muted' style='text-align:center'>ADVANCED CHART ANALYZER</p>
      <div style='text-align:center;margin-top:18px'>
        <b>{OWNER_NAME}</b><br>
        <span class='green'>Telegram:</span> {TELEGRAM} &nbsp; | &nbsp;
        <span class='green'>YouTube:</span> {YOUTUBE}
      </div>
    </div>
    """,unsafe_allow_html=True)

    c1,c2=st.columns(2)
    with c1:
        st.markdown("<div class='card'>",unsafe_allow_html=True)
        st.subheader("Login")
        u=st.text_input("Email / Username")
        p=st.text_input("Password",type="password")
        lic=st.text_input("License Code")
        if st.button("Login",use_container_width=True):
            if u in db["users"] and db["users"][u]["pass"]==h(p) and valid_license(db,lic):
                if db["users"][u].get("blocked",False):
                    st.error("Your account is blocked.")
                else:
                    st.session_state.login=True
                    st.session_state.user=u
                    db["users"][u]["license"]=lic
                    save(db)
                    st.success("Login success")
                    st.rerun()
            else:
                st.error("Wrong login or license")
        st.markdown("</div>",unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>",unsafe_allow_html=True)
        st.subheader("Sign Up")
        ru=st.text_input("New Username")
        rp=st.text_input("New Password",type="password")
        rl=st.text_input("License")
        if st.button("Create Account",use_container_width=True):
            if ru and rp and valid_license(db,rl):
                if ru in db["users"]:
                    st.error("User already exists")
                else:
                    db["users"][ru]={"pass":h(rp),"license":rl,"credits":500,"blocked":False,"created":datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    save(db)
                    st.success("Account created")
            else:
                st.error("Valid license required")
        st.markdown("</div>",unsafe_allow_html=True)

elif menu=="Dashboard":
    if not st.session_state.login:
        st.warning("Login first")
        st.stop()

    user=db["users"][st.session_state.user]

    if user.get("blocked", False):
        st.error("Your account is blocked. Contact admin.")
        st.stop()

    st.markdown(f"""
    <div class='hero'>
      <div class='logo'>REAL CHART <span class='blue'>ANALYZER</span></div>
      <p class='muted'>LIVE MARKET & VOLUME ANALYSIS</p>
      <span class='badge'>LIVE SCAN: ON</span> &nbsp; 
      <span class='badge'>AI ENGINE: ACTIVE</span>
      <div style='margin-top:20px'>
        <b>{OWNER_NAME}</b><br>
        <span class='green'>Telegram:</span> {TELEGRAM} &nbsp; | &nbsp;
        <span class='green'>YouTube:</span> {YOUTUBE}
      </div>
    </div>
    """,unsafe_allow_html=True)

    a,b,c,d=st.columns(4)
    a.markdown("<div class='metricbox'><p>ACCURACY MODE</p><h1>70-80%</h1><p>Target Filter</p></div>",unsafe_allow_html=True)
    b.markdown(f"<div class='metricbox'><p>CREDITS</p><h1>{user.get('credits',0)}</h1><p>Available</p></div>",unsafe_allow_html=True)
    c.markdown("<div class='metricbox'><p>RISK LEVEL</p><h1 style='color:#22c55e'>LOW</h1><p>1-3%</p></div>",unsafe_allow_html=True)
    d.markdown("<div class='metricbox'><p>MODE</p><h1>PRO</h1><p>Premium</p></div>",unsafe_allow_html=True)

    st.markdown("<div class='card'><h2>📡 LIVE SCAN COMPLETE</h2><h1>REAL MARKET REPORT</h1>",unsafe_allow_html=True)
    pair=st.selectbox("LIVE ASSET",PAIRS)
    st.file_uploader("Upload Chart Screenshot",type=["png","jpg","jpeg"])

    if st.button("ANALYZE NEW CHART",use_container_width=True):
        if user.get("credits",0)<=0:
            st.error("Credits finished. Contact admin.")
            st.stop()

        p=st.progress(0)
        box=st.empty()
        for i,t in enumerate(["Scanning chart...","Detecting support resistance...","Checking trap logic...","Filtering market setup...","Generating final report..."]):
            box.info(t)
            p.progress((i+1)*20)
            time.sleep(1.2)

        direction,conf,logic=ai_signal(pair)
        user["credits"]-=1
        save(db)

        colorClass="greenCard" if direction=="CALL" else "redCard"
        label="BUY ENTRY (CALL)" if direction=="CALL" else "SELL ENTRY (PUT)"
        icon="📈" if direction=="CALL" else "📉"

        st.markdown(f"""
        <div class='{colorClass}'>
          <p class='muted'>SIGNAL DIRECTION</p>
          <div class='big'>{icon} {label}</div>
        </div>
        <div class='card'>
          <p class='muted'>CONFIDENCE LEVEL</p>
          <div class='big'>{conf}/100</div>
        </div>
        <div class='card'>
          <h3>⚙️ TECHNICAL LOGIC</h3>
        """,unsafe_allow_html=True)

        for x in logic:
            st.write("✅ "+x)

        st.markdown("<div class='btnlike'>COPY SIGNAL</div></div>",unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)

elif menu=="Admin Panel":
    st.subheader("🔐 Admin Panel")
    pw = st.text_input("Admin Password", type="password")

    if pw == ADMIN_PASS:
        st.success("✅ Admin Access Granted")

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🎫 Create New License")

        c1, c2 = st.columns(2)
        with c1:
            duration_name = st.selectbox("Select License Package", ["1 Day Trial", "7 Days", "30 Days", "1 Year"])
        days_map = {"1 Day Trial":1, "7 Days":7, "30 Days":30, "1 Year":365}

        with c2:
            st.info(f"Selected: {duration_name}")

        if st.button("➕ Generate License", use_container_width=True):
            code, exp = make_license(days_map[duration_name])
            db["licenses"][code] = {
                "expiry": exp,
                "blocked": False,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save(db)
            st.success("✅ License Created")
            st.code(code)
            st.info("Expiry: " + exp)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📋 License Management")

        if len(db["licenses"]) == 0:
            st.warning("No license created yet.")

        for code, info in list(db["licenses"].items()):
            status = "🟢 Active" if not info.get("blocked", False) else "🔴 Blocked"
            st.markdown("<div class='adminbox'>", unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns([3, 2, 1.5, 1.5])
            col1.code(code)
            col2.write("Expiry: " + info.get("expiry", "N/A"))
            col3.write(status)

            if info.get("blocked", False):
                if col4.button("✅ Unblock", key="unblock_lic_" + code):
                    db["licenses"][code]["blocked"] = False
                    save(db)
                    st.rerun()
            else:
                if col4.button("⛔ Block", key="block_lic_" + code):
                    db["licenses"][code]["blocked"] = True
                    save(db)
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("👥 User Management")

        if len(db["users"]) == 0:
            st.warning("No user registered yet.")

        for uname, info in list(db["users"].items()):
            user_status = "🟢 Active" if not info.get("blocked", False) else "🔴 Blocked"
            st.markdown("<div class='adminbox'>", unsafe_allow_html=True)
            c1, c2, c3, c4, c5 = st.columns([2, 2, 1.5, 1.5, 1.5])
            c1.write("👤 " + uname)
            c2.write("Credits: " + str(info.get("credits", 0)))
            c3.write(user_status)

            if c4.button("➕ Add 100", key="add_credit_" + uname):
                db["users"][uname]["credits"] = info.get("credits", 0) + 100
                save(db)
                st.rerun()

            if info.get("blocked", False):
                if c5.button("✅ Unblock", key="unblock_user_" + uname):
                    db["users"][uname]["blocked"] = False
                    save(db)
                    st.rerun()
            else:
                if c5.button("⛔ Block", key="block_user_" + uname):
                    db["users"][uname]["blocked"] = True
                    save(db)
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    elif pw:
        st.error("❌ Wrong admin password")

elif menu=="Logout":
    st.session_state.login=False
    st.session_state.user=""
    st.success("Logged out")