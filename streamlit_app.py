import streamlit as st

st.title("🎈 Aplikasi Kimia")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

action = st.menu_button("Halo", options=["Nama", "Asal", "Kelas"])
if action == "Nama":
    st.write("Exporting as Aufa Freshika")
elif action == "Asal":
    st.write("Exporting as Bogor")
elif action == "Kelas":
    st.write("Exporting as 1D")
