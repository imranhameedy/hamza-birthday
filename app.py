import streamlit as st

st.set_page_config(page_title="Happy Birthday Hamza 🎂", page_icon="🎂", layout="centered")

# --------- CSS: notebook look + balloons background ----------
st.markdown("""
<style>
.stApp{
  background: radial-gradient(circle at top, #fff7ea 0%, #fff 35%, #f7fbff 100%);
}
.block-container{ max-width: 900px; position:relative; z-index:2; }

.balloon {
  position: fixed; bottom: -120px;
  width: 55px; height: 70px; border-radius: 50% 50% 45% 45%;
  opacity: 0.40;
  animation: floatUp linear infinite;
  z-index: 0;
}
.balloon:after {
  content:""; position:absolute; left: 50%; top: 66px;
  width: 2px; height: 90px; background: rgba(0,0,0,0.12);
}
@keyframes floatUp { from { transform: translateY(0); } to { transform: translateY(-120vh); } }

.note {
  background: rgba(255,255,255,0.88);
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 22px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.08);
  overflow: hidden;
}
.note-head{
  padding: 16px 18px;
  background: linear-gradient(90deg, rgba(255,205,178,0.55), rgba(189,224,254,0.55));
  display:flex; justify-content:space-between; align-items:center;
}
.note-title{ font-size: 22px; font-weight: 800; margin:0; }
.note-page{ font-size: 14px; opacity:0.75; }
.note-body{ padding: 18px; }
.caption{ font-size: 14px; opacity:0.72; }

.bigtitle{
  text-align:center;
  font-size: 52px;
  font-weight: 900;
  margin: 14px 0 4px 0;
}
.sub{
  text-align:center;
  font-size: 18px;
  opacity:0.85;
  margin: 0 0 18px 0;
}

.polaroid{
  background:white;
  border-radius: 18px;
  padding: 14px;
  box-shadow: 0 12px 26px rgba(0,0,0,0.12);
  border: 1px solid rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# Balloons (CSS only, no images)
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

# ----------------------------
# Background music (browser may require a user click to start)
# ----------------------------
if "music_on" not in st.session_state:
    st.session_state.music_on = False

colm1, colm2 = st.columns([1, 5])
with colm1:
    if st.button("▶️ Play", use_container_width=True):
        st.session_state.music_on = True
with colm2:
    if st.button("⏹ Stop", use_container_width=True):
        st.session_state.music_on = False

if st.session_state.music_on:
    st.audio("assets/birthday-music.mp3", format="audio/mp3", loop=True)
    st.caption("If it doesn’t start, click Play again (autoplay is blocked by some browsers).")

main_message = [
    "Hamza, one of the most precious gifts Allah gave me in 2025 was you and your friendship.",
    "Meri pyaari bro, happy birthday! I wish you a life full of happiness and joy ahead.",
    "May Allah fulfill all your wishes and bless you with success in everything you do.",
    "And yes… I’m still waiting to hear your engagement news soon 😂",
]

cake_text = "I wish I were in Afghanistan so we could celebrate together and cut the cake in person. But for now, accept this virtual cake from me 🎂"

# Page order you requested
pages = [
    {"type": "image", "title": "Memory #1", "src": "assets/hamza1.jpg"},
    {"type": "image", "title": "Memory #2", "src": "assets/hamza2.jpg"},
    {"type": "image", "title": "Memory #3", "src": "assets/hamza3.jpg"},
    {"type": "image", "title": "Memory #4", "src": "assets/hamza4.jpg"},
    {"type": "image", "title": "Memory #5", "src": "assets/hamza5.jpg"},
    {"type": "text",  "title": "Birthday Letter", "lines": main_message},
    {"type": "text",  "title": "One More Thing", "lines": [cake_text]},
    {"type": "gif",   "title": "Final Surprise", "src": "assets/Birthday-animated.gif"},
]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# Header
st.markdown(f"<div class='bigtitle'>Happy Birthday, {friend_name} 🎉</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>A tiny flipbook made in Python — just for you 😄</div>", unsafe_allow_html=True)

# Navigation
col_prev, col_mid, col_next = st.columns([1, 2, 1])

with col_prev:
    if st.button("⬅️ Prev", use_container_width=True, disabled=(st.session_state.page_index == 0)):
        st.session_state.page_index -= 1
        st.rerun()

with col_mid:
    st.markdown(f"<div style='text-align:center; font-weight:700; opacity:0.75;'>Flip the notebook pages</div>", unsafe_allow_html=True)

with col_next:
    if st.button("Next ➡️", use_container_width=True, disabled=(st.session_state.page_index == len(pages) - 1)):
        st.session_state.page_index += 1
        st.rerun()

# Current page
p = pages[st.session_state.page_index]
page_no = st.session_state.page_index + 1
total = len(pages)

st.markdown("<div class='note'>", unsafe_allow_html=True)
st.markdown(f"""
  <div class="note-head">
    <div class="note-title">{p["title"]}</div>
    <div class="note-page">Page {page_no} / {total}</div>
  </div>
""", unsafe_allow_html=True)

st.markdown("<div class='note-body'>", unsafe_allow_html=True)

if p["type"] in ("image", "gif"):
    st.markdown("<div class='polaroid'>", unsafe_allow_html=True)
    st.image(p["src"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='caption'>Tip: click Next to flip to the next page.</div>", unsafe_allow_html=True)

elif p["type"] == "text":
    for line in p["lines"]:
        st.write(line)
    st.markdown("<br><div class='caption'>— from your bro 🤍</div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

st.caption("Share this link with Hamza. (He can flip through the pages on his phone too.)")
