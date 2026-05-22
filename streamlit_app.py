import streamlit as st

st.title("🎈 Aplikasi Perkenalan Diri")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

action = st.menu_button("Halo", options=["Nama", "Asal", "Kelas"])
if action == "Nama":
    st.write("Aufa Freshika")
elif action == "Asal":
    st.write("Bogor")
elif action == "Kelas":
    st.write("1D")
