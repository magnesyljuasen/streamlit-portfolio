import streamlit as st

##36454f
##faf9f6
##ffd3cb
##6e7f80
##a9d0c8


### App start ###
st.set_page_config(
    page_title="Magne Syljuåsen",
    page_icon="src/img/logo-hand.png",
    layout="wide",
    initial_sidebar_state="collapsed"
    )

with open("src/styles/main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

main_body_logo = "src/img/logo-hand.png"
sidebar_logo = "src/img/logo-hand.png"

st.logo(sidebar_logo, icon_image=main_body_logo, size='large')

frontpage = st.Page("frontpage.py", title="Forside", icon=":material/book:", default=True)
  
pg = st.navigation([frontpage])

pg.run()