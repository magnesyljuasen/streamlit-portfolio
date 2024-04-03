import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_card import card
import base64
from PIL import Image
import numpy as np
import time
import math
import pandas as pd
from streamlit_echarts import st_echarts
import random


class Portfolio:
    def __init__(self) -> None:
        self.SPEECH_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M24 10.935v2.131l-8 3.947v-2.23l5.64-2.783-5.64-2.79v-2.223l8 3.948zm-16 3.848l-5.64-2.783 5.64-2.79v-2.223l-8 3.948v2.131l8 3.947v-2.23zm7.047-10.783h-2.078l-4.011 16h2.073l4.016-16z"/></svg>"""
        self.LINKEDIN_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 8c0 .557-.447 1.008-1 1.008s-1-.45-1-1.008c0-.557.447-1.008 1-1.008s1 .452 1 1.008zm0 2h-2v6h2v-6zm3 0h-2v6h2v-2.861c0-1.722 2.002-1.881 2.002 0v2.861h1.998v-3.359c0-3.284-3.128-3.164-4-1.548v-1.093z"/></svg>"""
        self.FACEBOOK_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 10h-2v2h2v6h3v-6h1.82l.18-2h-2v-.833c0-.478.096-.667.558-.667h1.442v-2.5h-2.404c-1.798 0-2.596.792-2.596 2.308v1.692z"/></svg>"""
        self.MAIL_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 2.02c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm0 12.55l-5.992-4.57h11.983l-5.991 4.57zm0 1.288l-6-4.629v6.771h12v-6.771l-6 4.629z"/></svg>"""
        self.PHONE_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm4.5 17.311l-1.76-3.397-1.032.505c-1.12.543-3.4-3.91-2.305-4.497l1.042-.513-1.747-3.409-1.053.52c-3.601 1.877 2.117 12.991 5.8 11.308l1.055-.517z"/></svg>"""
        self.GITHUB_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm0 6c-3.313 0-6 2.686-6 6 0 2.651 1.719 4.9 4.104 5.693.3.056.396-.13.396-.289v-1.117c-1.669.363-2.017-.707-2.017-.707-.272-.693-.666-.878-.666-.878-.544-.373.041-.365.041-.365.603.042.92.619.92.619.535.917 1.403.652 1.746.499.054-.388.209-.652.381-.802-1.333-.152-2.733-.667-2.733-2.965 0-.655.234-1.19.618-1.61-.062-.153-.268-.764.058-1.59 0 0 .504-.161 1.65.615.479-.133.992-.199 1.502-.202.51.002 1.023.069 1.503.202 1.146-.776 1.648-.615 1.648-.615.327.826.121 1.437.06 1.588.385.42.617.955.617 1.61 0 2.305-1.404 2.812-2.74 2.96.216.186.412.551.412 1.111v1.646c0 .16.096.347.4.288 2.383-.793 4.1-3.041 4.1-5.691 0-3.314-2.687-6-6-6z"/></svg>"""
        self.EDUCATION_SVG = """ <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" fill="#dddddd"><path d="M24 21h-3l1-3h1l1 3zm-12.976-4.543l8.976-4.575v6.118c-1.007 2.041-5.607 3-8.5 3-3.175 0-7.389-.994-8.5-3v-6.614l8.024 5.071zm11.976.543h-1v-7.26l-10.923 5.568-11.077-7 12-5.308 11 6.231v7.769z"/></svg>"""
        self.MUSIC_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M23 0l-15.996 3.585v13.04c-2.979-.589-6.004 1.671-6.004 4.154 0 2.137 1.671 3.221 3.485 3.221 2.155 0 4.512-1.528 4.515-4.638v-10.9l12-2.459v8.624c-2.975-.587-6 1.664-6 4.141 0 2.143 1.715 3.232 3.521 3.232 2.14 0 4.476-1.526 4.479-4.636v-17.364z"/></svg>"""
        self.SPORTS_SVG = """ <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" fill="#dddddd"><path d="M17.422 20.394c-.177-.415-.219-.698-.289-1.118.625-.697 1.189-1.432 1.692-2.204.58-.196 1.271-.438 2.281-.956-.795 1.756-2.08 3.239-3.684 4.278m-8.181 1.212c1.039-.558 1.89-1.193 2.831-1.899 1.012.253 2.079.395 3.194.443l.001.007c.083.435.205.803.362 1.153-1.987.777-4.182.93-6.388.296m-7.24-9.619l1.273 1.217c-.194 1.076-.248 2.069-.234 3.214-.659-1.334-1.04-2.83-1.04-4.418l.001-.013m11.371-9.882l-.758 1.737c-2.139.56-3.384 1.125-5.214 2.107l-2.863-.586c2.128-2.389 5.337-3.74 8.835-3.258m-1.804 11.769c-1.083-.726-1.941-1.464-3.466-2.727l.546-3.576c1.446-.848 2.566-1.239 4.477-1.849.999.687 1.984 1.428 2.934 2.216l-.002.023c-.138 1.739-.42 3.066-.845 4.495-1.196.524-2.41.998-3.644 1.418m-4.758 6.661c-.555-.339-1.072-.728-1.549-1.164-.256-1.921-.361-3.89-.003-5.865l.001-.004 1.716-.745c1.211 1.126 2.346 2.004 3.676 2.928l.063 2.525c-1.323 1.046-2.369 1.738-3.904 2.325m15.108-7.311c-1 .722-1.776 1.225-3.025 1.683l-1.734-2.007c.451-1.449.738-3 .866-4.727l2.499-1.381c1.147 1.872 1.681 4.066 1.394 6.432m-9.918-13.224c-6.623 0-12 5.377-12 12s5.377 12 12 12 12-5.377 12-12-5.377-12-12-12"/></svg>"""
        self.LOCATION_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M12 0c-3.313 0-6 2.687-6 6 0 2.972 2.164 5.433 5 5.91v8.09h2v-8.089c2.836-.477 5-2.938 5-5.91 0-3.314-2.687-6.001-6-6.001zm-.707 4.508c-.549.65-1.423.8-1.953.333s-.516-1.372.034-2.022c.548-.65 1.422-.799 1.952-.333.53.467.515 1.372-.033 2.022zm12.707 19.492h-24l4-8h5v2h-3.764l-2 4h17.527l-2-4h-3.763v-2h5l4 8z"/></svg>"""
        self.GIS_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M23.961 8.429c-.831.982-1.614 1.918-1.961 3.775v6.683l-4 2.479v-9.161c-.206-1.104-.566-1.885-1-2.539v11.475l-4-2.885v-13.069l1.577 1.138c-.339-.701-.577-1.518-.577-2.524l.019-.345-2.019-1.456-5.545 4-6.455-4v18l6.455 4 5.545-4 5.545 4 6.455-4v-11.618l-.039.047zm-17.961 12.936l-4-2.479v-13.294l4 2.479v13.294zm5-3.11l-4 2.885v-13.067l4-2.886v13.068zm9-18.255c-2.1 0-4 1.702-4 3.801 0 3.121 3.188 3.451 4 8.199.812-4.748 4-5.078 4-8.199 0-2.099-1.9-3.801-4-3.801zm0 5.5c-.828 0-1.5-.671-1.5-1.5s.672-1.5 1.5-1.5 1.5.671 1.5 1.5-.672 1.5-1.5 1.5z"/></svg>"""
        self.LIFE_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M20 6.093l-3-3v-2.093h3v5.093zm1 11.349c.813.315 1.732.558 3 .558v2c-3.896 0-5.083-2-8.002-2-3.04 0-4.436 2-8.002 2-3.684 0-4.376-2-7.996-2v-2c1.275 0 2.217.184 3 .438v-4.438h-3l12-12 12 12h-3v5.442zm-11-3.442v3.692c1.327-.403 2.469-1.089 4-1.45v-2.242h-4zm-2.004 8c-3.184 0-3.767-2-7.996-2v2c3.62 0 4.312 2 7.996 2 3.566 0 4.962-2 8.002-2 2.919 0 4.106 2 8.002 2v-2c-3.649 0-4.438-2-8.002-2-3.581 0-4.977 2-8.002 2z"/></svg>"""
        self.CODING_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#dddddd"><path d="M21 3c0-1.657-1.343-3-3-3s-3 1.343-3 3c0 1.323.861 2.433 2.05 2.832.168 4.295-2.021 4.764-4.998 5.391-1.709.36-3.642.775-5.052 2.085v-7.492c1.163-.413 2-1.511 2-2.816 0-1.657-1.343-3-3-3s-3 1.343-3 3c0 1.305.837 2.403 2 2.816v12.367c-1.163.414-2 1.512-2 2.817 0 1.657 1.343 3 3 3s3-1.343 3-3c0-1.295-.824-2.388-1.973-2.808.27-3.922 2.57-4.408 5.437-5.012 3.038-.64 6.774-1.442 6.579-7.377 1.141-.425 1.957-1.514 1.957-2.803zm-16.8 0c0-.993.807-1.8 1.8-1.8s1.8.807 1.8 1.8-.807 1.8-1.8 1.8-1.8-.807-1.8-1.8zm3.6 18c0 .993-.807 1.8-1.8 1.8s-1.8-.807-1.8-1.8.807-1.8 1.8-1.8 1.8.807 1.8 1.8z"/></svg>"""
        
    def set_streamlit_settings(self):
        st.set_page_config(
        page_title="Magne Syljuåsen",
        page_icon="🧍",
        layout="centered",
        initial_sidebar_state="expanded")
        
        with open("src/styles/main.css") as f:
            st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

        st.markdown(
            """
            <style>
            [data-testid="collapsedControl"] svg {
                height: 4rem;
                width: 4rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
    def _render_svg(self, svg, text):
        b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
        html = f'<img src="data:image/svg+xml;base64,%s"/> {text}' % b64
        st.markdown(html, unsafe_allow_html=True)
    
    def _render_click_logos(self, svg, text, link_url, degrees):
        b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
        html = f'<center> <img src="data:image/svg+xml;base64,%s"/> </center>' % b64
        st.markdown(f'<div style="background: repeating-linear-gradient({degrees}deg, transparent, transparent 15px, transparent 10px, #007db3 20px);color:black;border: solid 1px #e5e7eb; border-radius: 15px; text-align: center;padding: 1em;min-height: 60px;display: inline-block;box-sizing: border-box;width: 100%;" {html} <a target="parent"  href="{link_url}">{text}</a> </div>', unsafe_allow_html=True)       
    
    def _github_linkedin(self):
        c1, c2 = st.columns(2)
        with c1:
            self._render_click_logos(svg = self.LINKEDIN_SVG, text = "LinkedIn", link_url = "https://www.linkedin.com/in/magne-sylju%C3%A5sen-35235738/", degrees = 45)
        with c2:
            self._render_click_logos(svg = self.GITHUB_SVG, text = "GitHub", link_url = "https://github.com/magnesyljuasen", degrees = 90)
        
    def __who_am_i(self):
        svg_education = self.SPEECH_SVG
        b64 = base64.b64encode(svg_education.encode('utf-8')).decode("utf-8")
        html = f'''<medium> <img src="data:image/svg+xml;base64,%s"/> 
        Sivilingeniør fra NTNU, og jobber som rådgiver innen grunnvarme i Asplan Viak.
        Er nysgjerrig på teknologi og er optatt av hvordan det kan bidra til å utvikle bærekraftige 
        løsninger samt effektivisere repetetive oppgaver. Jobber i dag mye med energianalyser i Python for å 
        vurdere potensial for energieffektiviseringstiltak i den norske bygningsmassen. </medium> ''' % b64
        st.write(html, unsafe_allow_html=True)
        
    def ring_gauge(self):
        option = {
            "series": [
                {
                    "type": "gauge",
                    "startAngle": 90,
                    "endAngle": -270,
                    "pointer": {"show": False},
                    "progress": {
                        "show": True,
                        "overlap": False,
                        "roundCap": True,
                        "clip": False,
                        "itemStyle": {"borderWidth": 1, "borderColor": "#464646"},
                        },
                    "axisLine": {"lineStyle": {"width": 40}},
                    "splitLine": {"show": False, "distance": 0, "length": 10},
                    "axisTick": {"show": False},
                    "axisLabel": {"show": False, "distance": 50},
                    "data": [
                        {
                            "value": 70,
                            "name": "Python",
                            "title": {"offsetCenter": ["0%", "-30%"]},
                            "detail": {"offsetCenter": ["0%", "-20%"]}
                            },
                        {
                            "value": 80,
                            "name": "Streamlit",
                            "title": {"offsetCenter": ["0%", "0%"]},
                            "detail": {"offsetCenter": ["0%", "10%"]},
                            },
                        {
                            "value": 40,
                            "name": "Pandas",
                            "title": {"offsetCenter": ["0%", "30%"]},
                            "detail": {"offsetCenter": ["0%", "40%"]},
                            },
                        ],
                    "title": {"fontSize": 14},
                    "detail": {
                        "width": 50,
                        "height": 14,
                        "fontSize": 14,
                        "color": "auto",
                        "borderColor": "auto",
                        "borderRadius": 20,
                        "borderWidth": 1,
                        "formatter": "{value}%",
                        },
                    }
                ]
            }
        st_echarts(option, height="300px", key="echarts")
        
        
    def main(self):
        self.set_streamlit_settings()
#        with st.sidebar:
#            self._render_svg(svg = self.MAIL_SVG, text = "msylju@gmail.com")
#            self._render_svg(svg = self.PHONE_SVG, text = "451 925 40")
#            self._render_svg(svg = self.LOCATION_SVG, text = "Trondheim, Norge")
#            self._render_click_logos(svg = self.LINKEDIN_SVG, text = "LinkedIn", link_url = "https://www.linkedin.com/in/magne-sylju%C3%A5sen-35235738/", degrees = 45)
#            self._render_click_logos(svg = self.GITHUB_SVG, text = "GitHub", link_url = "https://github.com/magnesyljuasen", degrees = 90)
        
        st.title("Hei👋 Jeg er Magne Syljuåsen")
        self.__who_am_i()
        #--
        st.header("Prosjekter")
        with st.popover("Bergvarmekalkulatoren", use_container_width=True):
            st.header("Bergvarmekalkulatoren")
            st.write(""" 
                     Bergvarmekalkulatoren er et egenutviklet digitalt verktøy 
                     som gjør det enkelt å få en pekepinn på størrelsen, 
                     lønnsomhet og miljøgevinst for et bergvarmeanlegg (energibrønn med varmepumpe) 
                     til småhus. """)
            st.write("""    
                     Hensikten med tjenesten er å gi huseier/anleggseier et begrep om 
                     nødvendig lengde på energibrønn for å få et velfungerende 
                     anlegg tilpasset husets varmebehov. Tjenesten vil være med 
                     på å øke kompetansen hos kunden, skape mer oppmerksomhet 
                     rundt bergvarme, og anbefale kunder å velge kvalitetssikrete 
                     installatørbedrifter som er en del av NOVAPs godkjenningsordning. """)
            st.markdown(f'<a target="parent" style="font-size: 1.0rem; border-radius: 15px; text-align: left; padding: 0rem; min-height: 60px; display: inline-block; box-sizing: border-box; width: 100%; transition: background-color 0.3s;" href="https://www.varmepumpeinfo.no/bergvarme/kalkulator">Tjenesten er solgt til NOVAP og ligger ute på varmepumpeinfo.no.</a>', unsafe_allow_html=True)
            image = Image.open('src/data/bergvarmekalkulatoren_showcase_2.png')
            st.image(image, use_column_width=True)
        with st.popover("Energy Plan Zero", use_container_width=True):
            st.write("Kommer ...")
            st.markdown(f'<a target="parent" style="font-size: 1.0rem; border-radius: 15px; text-align: left; padding: 0rem; min-height: 60px; display: inline-block; box-sizing: border-box; width: 100%; transition: background-color 0.3s;" href="https://www.av-energiplanlegging.no">Tjenesten er solgt til NOVAP og ligger ute på varmepumpeinfo.no.</a>', unsafe_allow_html=True)
            
        with st.popover("Intern webside for grunnvarmegruppa", use_container_width=True):
            st.write("Kommer ...")
        self.ring_gauge()
        
        st.header("Prosjekter")
        
        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Skills")
            self._render_svg(svg = self.CODING_SVG, text = "Programmerer i Python. Benytter meg mye av Streamlit, Numpy og Pandas. Bruker GitHub, Visual Studio Code og Azure DevOps.")
            self._render_svg(svg = self.GIS_SVG, text = "Jobbet mye med ArcGIS, og i tillegg open-source GIS-tjenester som GeoPandas, Shapely og Folium.")
        with c2:
            st.subheader("Om meg")
            self._render_svg(svg = self.EDUCATION_SVG, text = "Utdannet sivilingeniør innen tekniske geofag fra Norges teknisk-naturvitenskapelige universitet (NTNU)")
            self._render_svg(svg = self.LIFE_SVG, text = "Samboer med Emma.")
            self._render_svg(svg = self.SPORTS_SVG, text = "Har spillt fotball aktivt i 20 år. Driver i dag med fotball på hobbybasis, og er nysgjerrig på andre idretter.")
            self._render_svg(svg = self.MUSIC_SVG, text = "Liker å synge og spille gitar.")
        
        st.write("")
        self._github_linkedin()
        st_lottie("https://lottie.host/65eb2703-6b4a-4b22-a022-e7051369ca74/G6txfabyKf.json")
        
if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.main()