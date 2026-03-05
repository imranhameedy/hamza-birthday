import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Hamza 🎂", page_icon="🎂", layout="centered")

# ----------------------------
# Theme / CSS (animation + balloons + modal)
# ----------------------------
st.markdown("""
<style>
/* page background */
.stApp {
  background: radial-gradient(circle at top, #fff7ea 0%, #fff 35%, #f7fbff 100%);
}

/* center container look */
.card {
  background: rgba(255,255,255,0.85);
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 22px;
  padding: 22px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.08);
}

/* animated title */
.title-wrap { text-align:center; margin-top: 10px; }
.title {
  font-size: 54px;
  font-weight: 900;
  letter-spacing: -1px;
  margin: 0;
}
.title span {
  display:inline-block;
  transform: translateY(14px);
  opacity: 0;
  animation: pop 0.6s forwards;
  animation-delay: var(--d);
}
@keyframes pop {
  to { transform: translateY(0); opacity: 1; }
}
.subtitle {
  text-align:center;
  font-size: 18px;
  opacity: 0.8;
  margin-top: 8px;
}

/* balloons (pure CSS) */
.balloon {
  position: fixed;
  bottom: -120px;
  width: 55px;
  height: 70px;
  border-radius: 50% 50% 45% 45%;
  opacity: 0.55;
  filter: blur(0.2px);
  animation: floatUp linear infinite;
  z-index: 0;
}
.balloon:after {
  content:"";
  position:absolute;
  left: 50%;
  top: 66px;
  width: 2px;
  height: 90px;
  background: rgba(0,0,0,0.12);
}
@keyframes floatUp {
  from { transform: translateY(0); }
  to { transform: translateY(-120vh); }
}

/* modal */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.35);
  z-index: 1000;
  display:flex;
  align-items:center;
  justify-content:center;
  padding: 18px;
}
.modal {
  width: min(720px, 92vw);
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 20px 60px rgba(0,0,0,0.25);
  border: 1px solid rgba(0,0,0,0.08);
  overflow:hidden;
}
.modal-header {
  padding: 16px 18px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  background: linear-gradient(90deg, rgba(255,205,178,0.5), rgba(189,224,254,0.5));
}
.modal-header h3 { margin:0; font-size:18px; }
.modal-body { padding: 18px; font-size: 18px; line-height: 1.6; }
.pill {
  display:inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(0,255,140,0.14);
  border: 1px solid rgba(0,255,140,0.28);
  font-weight: 700;
}

/* keep content above balloons */
.block-container { position: relative; z-index: 2; max-width: 900px; }
</style>
""", unsafe_allow_html=True)

# Add balloons (no images)
st.markdown("""
<div class="balloon" style="left:6%; background:#ff6b6b; animation-duration: 14s;"></div>
<div class="balloon" style="left:16%; background:#ffd166; animation-duration: 18s;"></div>
<div class="balloon" style="left:28%; background:#06d6a0; animation-duration: 16s;"></div>
<div class="balloon" style="left:40%; background:#4dabf7; animation-duration: 20s;"></div>
<div class="balloon" style="left:52%; background:#b197fc; animation-duration: 17s;"></div>
<div class="balloon" style="left:64%; background:#ff8fab; animation-duration: 19s;"></div>
<div class="balloon" style="left:76%; background:#8ce99a; animation-duration: 15s;"></div>
<div class="balloon" style="left:88%; background:#ffa94d; animation-duration: 21s;"></div>
""", unsafe_allow_html=True)

friend_name = "Hamza"

message_lines = [
    "Hamza, one of the most precious gifts Allah gave me in 2025 was you and your friendship.",
    "Meri pyaari bro, happy birthday! I wish you a life full of happiness and joy ahead.",
    "May Allah fulfill all your wishes and bless you with success in everything you do.",
    "And yes… I’m still waiting to hear your engagement news soon 😂",
]

# ----------------------------
# State
# ----------------------------
if "show_letter" not in st.session_state:
    st.session_state.show_letter = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 9)

# ----------------------------
# Header card
# ----------------------------
letters = list(f"Happy Birthday, {friend_name} 🎉")
spans = []
for i, ch in enumerate(letters):
    delay = 0.06 * i
    if ch == " ":
        spans.append("&nbsp;")
    else:
        spans.append(f'<span style="--d:{delay:.2f}s">{ch}</span>')

st.markdown(f"""
<div class="card">
  <div class="title-wrap">
    <div class="title">{''.join(spans)}</div>
    <div class="subtitle">A tiny website made in Python — because you're a programmer 😄</div>
    <div style="margin-top:12px" class="pill">Status: Build ✅ | Bugs: Maybe 😈</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
c1, c2 = st.columns(2)

with c1:
    if st.button("💌 Open the birthday letter", use_container_width=True):
        st.session_state.show_letter = True

with c2:
    if st.button("🔄 Reset game", use_container_width=True):
        st.session_state.score = 0
        st.session_state.target = random.randint(1, 9)
        st.toast("Game reset. Go hunt bugs 🐛")

# ----------------------------
# Modal letter (popup)
# ----------------------------
if st.session_state.show_letter:
    letter_html = "<br><br>".join(message_lines) + "<br><br><b>May Allah bless you always. آمين 🤍</b>"
    st.markdown(f"""
    <div class="modal-backdrop">
      <div class="modal">
        <div class="modal-header">
          <h3>To: {friend_name} 💙</h3>
          <div style="font-size:14px; opacity:0.85;">Click “Close letter” below</div>
        </div>
        <div class="modal-body">
          {letter_html}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Close button outside HTML so it actually works
    if st.button("❌ Close letter"):
        st.session_state.show_letter = False
        st.rerun()

st.write("")

# ----------------------------
# Mini Game
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🐛 Mini Game: Bug Hunt")
st.write("Click the bug with the **same number** as the target. Get **5 points** to unlock the final surprise.")

target = st.session_state.target
st.markdown(f"**Target bug number:** `{target}`")

bugs = list(range(1, 10))
random.shuffle(bugs)

grid = st.columns(3)
clicked = None
for i, n in enumerate(bugs):
    with grid[i % 3]:
        if st.button(f"🐛 Bug {n}", key=f"bug_{n}", use_container_width=True):
            clicked = n

if clicked is not None:
    if clicked == target:
        st.session_state.score += 1
        st.toast("Nice! Bug squashed ✅")
    else:
        st.toast("Wrong bug 😈 Try again.")
    st.session_state.target = random.randint(1, 9)

st.write(f"**Score:** {st.session_state.score} / 5")

if st.session_state.score >= 5:
    st.success("Unlocked 🎉")
    st.markdown("### Final Surprise 😄")
    st.markdown("""
- Clean builds ✅  
- Big wins ✅  
- Engagement news… loading… **any day now** 😂
""")
    st.snow()

st.markdown("</div>", unsafe_allow_html=True)
