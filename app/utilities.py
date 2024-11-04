import base64
import streamlit as st 

def render_click_logos(svg, text, link_url):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<center> <img src="data:image/svg+xml;base64,%s"/> </center>' % b64
    st.markdown(f'''<div style="background: #FAF9F6;
                color: #36454f;
                text-color : #36454f;
                border: solid 1px #36454f; 
                border-radius: 40px; 
                text-align: center;
                padding: 1em;
                margin-top: 1em;
                margin-bottom: 1em;
                min-height: 60px;
                display: inline-block;
                box-sizing: border-box;
                width: 100%;" 
                {html} <a target="parent" href="{link_url}">{text}</a> </div>''', unsafe_allow_html=True) 