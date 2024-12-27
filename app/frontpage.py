import streamlit as st
from utilities import render_click_logos, render_svg
from streamlit_carousel import carousel
import pandas as pd

#https://www.svgrepo.com/
GITHUB_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#36454f"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm0 6c-3.313 0-6 2.686-6 6 0 2.651 1.719 4.9 4.104 5.693.3.056.396-.13.396-.289v-1.117c-1.669.363-2.017-.707-2.017-.707-.272-.693-.666-.878-.666-.878-.544-.373.041-.365.041-.365.603.042.92.619.92.619.535.917 1.403.652 1.746.499.054-.388.209-.652.381-.802-1.333-.152-2.733-.667-2.733-2.965 0-.655.234-1.19.618-1.61-.062-.153-.268-.764.058-1.59 0 0 .504-.161 1.65.615.479-.133.992-.199 1.502-.202.51.002 1.023.069 1.503.202 1.146-.776 1.648-.615 1.648-.615.327.826.121 1.437.06 1.588.385.42.617.955.617 1.61 0 2.305-1.404 2.812-2.74 2.96.216.186.412.551.412 1.111v1.646c0 .16.096.347.4.288 2.383-.793 4.1-3.041 4.1-5.691 0-3.314-2.687-6-6-6z"/></svg>"""
LINKEDIN_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#36454f"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 8c0 .557-.447 1.008-1 1.008s-1-.45-1-1.008c0-.557.447-1.008 1-1.008s1 .452 1 1.008zm0 2h-2v6h2v-6zm3 0h-2v6h2v-2.861c0-1.722 2.002-1.881 2.002 0v2.861h1.998v-3.359c0-3.284-3.128-3.164-4-1.548v-1.093z"/></svg>"""
CODING_SVG = """ <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#36454f"><path d="M21 3c0-1.657-1.343-3-3-3s-3 1.343-3 3c0 1.323.861 2.433 2.05 2.832.168 4.295-2.021 4.764-4.998 5.391-1.709.36-3.642.775-5.052 2.085v-7.492c1.163-.413 2-1.511 2-2.816 0-1.657-1.343-3-3-3s-3 1.343-3 3c0 1.305.837 2.403 2 2.816v12.367c-1.163.414-2 1.512-2 2.817 0 1.657 1.343 3 3 3s3-1.343 3-3c0-1.295-.824-2.388-1.973-2.808.27-3.922 2.57-4.408 5.437-5.012 3.038-.64 6.774-1.442 6.579-7.377 1.141-.425 1.957-1.514 1.957-2.803zm-16.8 0c0-.993.807-1.8 1.8-1.8s1.8.807 1.8 1.8-.807 1.8-1.8 1.8-1.8-.807-1.8-1.8zm3.6 18c0 .993-.807 1.8-1.8 1.8s-1.8-.807-1.8-1.8.807-1.8 1.8-1.8 1.8.807 1.8 1.8z"/></svg>"""
SOURCE_SVG = """<svg width="30px" height="30px" viewBox="0 0 76.00 76.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" baseProfile="full" enable-background="new 0 0 76.00 76.00" xml:space="preserve" fill="#36454f"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill="#36454f" fill-opacity="1" stroke-width="0.00076" stroke-linejoin="round" d="M 25.3333,20.5833C 23.5844,20.5833 22.1667,22.0011 22.1667,23.75C 22.1667,25.4989 23.5844,26.9167 25.3333,26.9167C 27.0822,26.9167 28.5,25.4989 28.5,23.75C 28.5,22.0011 27.0822,20.5833 25.3333,20.5833 Z M 25.3333,15.8334C 29.7056,15.8334 33.2499,19.3778 33.2499,23.75C 33.2499,26.9964 31.296,29.7863 28.5,31.008L 28.5,44.9921C 31.296,46.2137 33.25,49.0037 33.25,52.25C 33.25,56.6223 29.7056,60.1667 25.3333,60.1667C 20.9611,60.1667 17.4167,56.6223 17.4167,52.25C 17.4167,49.0037 19.3706,46.2137 22.1666,44.9921L 22.1666,31.008C 19.3706,29.7863 17.4166,26.9964 17.4166,23.75C 17.4166,19.3778 20.9611,15.8334 25.3333,15.8334 Z M 25.3333,49.0834C 23.5844,49.0834 22.1667,50.5011 22.1667,52.25C 22.1667,53.9989 23.5844,55.4167 25.3333,55.4167C 27.0822,55.4167 28.5,53.9989 28.5,52.25C 28.5,50.5011 27.0822,49.0834 25.3333,49.0834 Z M 42.75,26.9167L 42.75,31.6667L 34.8333,23.75L 42.7499,15.8334L 42.7499,20.5834L 47.5,20.5834C 50.9978,20.5834 53.8333,23.4189 53.8333,26.9167L 53.8333,44.9921C 56.6293,46.2137 58.5833,49.0037 58.5833,52.25C 58.5833,56.6223 55.0389,60.1667 50.6666,60.1667C 46.2944,60.1667 42.75,56.6223 42.75,52.25C 42.75,49.0037 44.7039,46.2137 47.5,44.9921L 47.5,30.0833C 47.5,28.3344 46.0822,26.9167 44.3333,26.9167L 42.75,26.9167 Z M 50.6666,49.0834C 48.9177,49.0834 47.5,50.5011 47.5,52.25C 47.5,53.9989 48.9177,55.4167 50.6666,55.4167C 52.4155,55.4167 53.8333,53.9989 53.8333,52.25C 53.8333,50.5011 52.4155,49.0834 50.6666,49.0834 Z "></path> </g></svg>"""
ARCGIS_SVG = """<svg width="30px" height="30px" viewBox="-6 -6 36.00 36.00" xmlns="http://www.w3.org/2000/svg" fill="#36454f" stroke="#36454f" stroke-width="0.00024000000000000003" transform="rotate(0)matrix(1, 0, 0, 1, 0, 0)"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M24 12a4.99 4.99 0 0 1-2.15 4.101l-.85-.495v-.163a3.974 3.974 0 0 0-1.377-7.377l-.79-.124-.052-.798a5.293 5.293 0 0 0-10.214-1.57L8.17 6.59l-.977-.483A2.277 2.277 0 0 0 6.19 5.87a2.18 2.18 0 0 0-1.167.339 2.206 2.206 0 0 0-.98 1.395l-.113.505-.476.2A4 4 0 0 0 5 16h2v1H5a5 5 0 0 1-1.934-9.611 3.21 3.21 0 0 1 1.422-2.025 3.17 3.17 0 0 1 1.702-.493 3.269 3.269 0 0 1 1.446.34 6.293 6.293 0 0 1 12.143 1.867A4.988 4.988 0 0 1 24 12zm-5.437 7.5l-4.016 2.342-4.015-2.342.587-.342-.993-.579-1.578.92 6 3.501 6-3.5-1.579-.92-.992.578zm1.985-3l-1.579-.92-.992.578.586.342-4.016 2.342-4.015-2.342.587-.342-.993-.579-1.578.921 6 3.5zm-12-3l6-3.5 6 3.5-6 3.5zm6 2.342l4.015-2.342-4.016-2.343-4.015 2.343z"></path><path fill="none" d="M0 0h24v24H0z"></path></g></svg>"""
GIS_SVG = """<svg width="30px" height="30px" viewBox="-2.4 -2.4 28.80 28.80" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M11 16C11 16.5523 11.4477 17 12 17C12.5523 17 13 16.5523 13 16H11ZM8.21567 14.3922C8.75496 14.2731 9.09558 13.7394 8.97647 13.2001C8.85735 12.6608 8.32362 12.3202 7.78433 12.4393L8.21567 14.3922ZM16.2157 12.4393C15.6764 12.3202 15.1426 12.6608 15.0235 13.2001C14.9044 13.7394 15.245 14.2731 15.7843 14.3922L16.2157 12.4393ZM15 7C15 8.65685 13.6569 10 12 10V12C14.7614 12 17 9.76142 17 7H15ZM12 10C10.3431 10 9 8.65685 9 7H7C7 9.76142 9.23858 12 12 12V10ZM9 7C9 5.34315 10.3431 4 12 4V2C9.23858 2 7 4.23858 7 7H9ZM12 4C13.6569 4 15 5.34315 15 7H17C17 4.23858 14.7614 2 12 2V4ZM11 11V16H13V11H11ZM20 17C20 17.2269 19.9007 17.5183 19.5683 17.8676C19.2311 18.222 18.6958 18.5866 17.9578 18.9146C16.4844 19.5694 14.3789 20 12 20V22C14.5917 22 16.9861 21.5351 18.7701 20.7422C19.6608 20.3463 20.4435 19.8491 21.0171 19.2463C21.5956 18.6385 22 17.8777 22 17H20ZM12 20C9.62114 20 7.51558 19.5694 6.04218 18.9146C5.30422 18.5866 4.76892 18.222 4.43166 17.8676C4.0993 17.5183 4 17.2269 4 17H2C2 17.8777 2.40438 18.6385 2.98287 19.2463C3.55645 19.8491 4.33918 20.3463 5.2299 20.7422C7.01386 21.5351 9.40829 22 12 22V20ZM4 17C4 16.6824 4.20805 16.2134 4.96356 15.6826C5.70129 15.1644 6.81544 14.7015 8.21567 14.3922L7.78433 12.4393C6.22113 12.7846 4.83528 13.3285 3.81386 14.0461C2.81023 14.7512 2 15.747 2 17H4ZM15.7843 14.3922C17.1846 14.7015 18.2987 15.1644 19.0364 15.6826C19.792 16.2134 20 16.6824 20 17H22C22 15.747 21.1898 14.7512 20.1861 14.0461C19.1647 13.3285 17.7789 12.7846 16.2157 12.4393L15.7843 14.3922Z" fill="#36454f "></path> </g></svg>"""
PYTHON_SVG = """<svg width="30px" height="30px" viewBox="-5.76 -5.76 27.52 27.52" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M5.79 1.574h3.866c.14 0 .252.11.252.246v5.186a.25.25 0 01-.252.246H6.344c-.975 0-1.766.77-1.766 1.72v1.162a.25.25 0 01-.253.243H1.867a.25.25 0 01-.253-.246V6.177a.25.25 0 01.252-.246H7.98c.418 0 .757-.33.757-.737a.747.747 0 00-.757-.738H5.537V1.82a.25.25 0 01.253-.246zm5.632 2.592V1.82c0-.95-.79-1.72-1.766-1.72H5.79c-.976 0-1.767.77-1.767 1.72v2.636H1.867C.89 4.456.1 5.226.1 6.176v3.955c0 .95.79 1.72 1.766 1.72h2.46c.085 0 .17-.006.252-.017v2.346c0 .95.79 1.72 1.766 1.72h3.866c.976 0 1.767-.77 1.767-1.72v-2.636h2.156c.976 0 1.767-.77 1.767-1.72V5.868c0-.95-.79-1.72-1.767-1.72h-2.458c-.086 0-.17.005-.253.017zm-5.33 5.974V8.994a.25.25 0 01.252-.246h3.312c.976 0 1.766-.77 1.766-1.72V5.866a.25.25 0 01.253-.243h2.458c.14 0 .253.11.253.246v3.954a.25.25 0 01-.252.246H8.02a.747.747 0 00-.757.737c0 .408.339.738.757.738h2.442v2.636a.25.25 0 01-.253.246H6.344a.25.25 0 01-.252-.246v-4.04z" fill="#36454f"></path> </g></svg>"""
FRONTEND_SVG = """<svg fill="#36454f" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-151.9 -151.9 793.80 793.80" xml:space="preserve" width="30px" height="30px" stroke="#36454f" stroke-width="0.0049"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <rect x="166.224" y="222.069" width="30.625" height="72.263"></rect> <rect x="208.214" y="185.38" width="30.625" height="108.952"></rect> <rect x="250.204" y="148.684" width="30.625" height="145.648"></rect> <rect x="292.194" y="111.988" width="30.625" height="182.344"></rect> <path d="M467.031,43.707H22.969C10.336,43.707,0,54.043,0,66.676v273.073c0,12.633,10.336,22.969,22.969,22.969h183.75v52.951 h-69.863v30.625h216.289v-30.625h-69.863v-52.951h183.75c12.633,0,22.969-10.336,22.969-22.969V66.676 C490,54.043,479.664,43.707,467.031,43.707z M459.375,332.092H30.625V74.332h428.75V332.092z"></path> </g> </g></svg>"""
AI_SVG = """<svg width="30px" height="30px" viewBox="-10.24 -10.24 84.48 84.48" xmlns="http://www.w3.org/2000/svg" stroke-width="2.944" stroke="#36454f" fill="none"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><circle cx="34.52" cy="11.43" r="5.82"></circle><circle cx="53.63" cy="31.6" r="5.82"></circle><circle cx="34.52" cy="50.57" r="5.82"></circle><circle cx="15.16" cy="42.03" r="5.82"></circle><circle cx="15.16" cy="19.27" r="5.82"></circle><circle cx="34.51" cy="29.27" r="4.7"></circle><line x1="20.17" y1="16.3" x2="28.9" y2="12.93"></line><line x1="38.6" y1="15.59" x2="49.48" y2="27.52"></line><line x1="50.07" y1="36.2" x2="38.67" y2="46.49"></line><line x1="18.36" y1="24.13" x2="30.91" y2="46.01"></line><line x1="20.31" y1="44.74" x2="28.7" y2="48.63"></line><line x1="17.34" y1="36.63" x2="31.37" y2="16.32"></line><line x1="20.52" y1="21.55" x2="30.34" y2="27.1"></line><line x1="39.22" y1="29.8" x2="47.81" y2="30.45"></line><line x1="34.51" y1="33.98" x2="34.52" y2="44.74"></line></g></svg>"""
PROGRAMMING_SVG = """<svg fill="#36454f" width="30px" height="30px" viewBox="-5.76 -5.76 35.52 35.52" xmlns="http://www.w3.org/2000/svg" stroke="#36454f" stroke-width="0.384"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" d="M3,3 L21,3 C22.1045695,3 23,3.8954305 23,5 L23,19 C23,20.1045695 22.1045695,21 21,21 L3,21 C1.8954305,21 1,20.1045695 1,19 L1,5 C1,3.8954305 1.8954305,3 3,3 Z M3,5 L3,19 L21,19 L21,5 L3,5 Z M8.33333333,12 L5.4,9.8 L6.6,8.2 L11.6666667,12 L6.6,15.8 L5.4,14.2 L8.33333333,12 Z M12,16 L12,14 L17,14 L17,16 L12,16 Z"></path> </g></svg>"""
AUTOCAD_SVG = """<svg fill="#36454f" width="30px" height="30px" viewBox="-10.56 -10.56 45.12 45.12" role="img" xmlns="http://www.w3.org/2000/svg" stroke="#36454f" stroke-width="0.00024000000000000003"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title>Autodesk icon</title><path d="m14.574 1.0203c-0.097-0.096997-0.29099-0.58198-0.97097-0.58198h-6.7038s0.97097 0.096997 1.36 1.068c0 0 1.069 2.5269 2.0399 4.9558 2.8179 6.6068 7.1898 17.099 7.1898 17.099h6.5108c0.097-0.097-9.3267-22.443-9.4247-22.54zm-8.8407 0.87497-5.3438 12.631c-0.29199 0.87497-0.097997 1.9439 1.457 1.9439h4.1779l3.6919-8.8417c-1.166-2.9149-2.1359-5.2478-2.1359-5.2478-0.096997-0.29199-0.38899-1.069-0.97197-1.069-0.58298 0-0.77698 0.48598-0.87397 0.58298zm-0.097997 15.643h-4.4689c-0.77698 0-1.166-0.48598-1.166-0.48598 0.77698 1.36 3.0119 5.6358 3.0119 5.6358 0.38899 0.48598 0.77698 0.77698 1.36 0.77698 1.263 0 3.2069-1.263 3.2069-1.263l7.4808-4.6639z"></path></g></svg>"""
MICROSOFT_SVG = """<svg width="30px" height="30px" viewBox="-23.04 -23.04 238.08 238.08" xmlns="http://www.w3.org/2000/svg" fill="none"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path stroke="#36454f" stroke-width="8.256" d="M102.379 22.587c6.613 1.89 11.179 7.95 11.188 14.851v10.84L74.248 62.541a10.69 10.69 0 0 0-6.996 10.03v36.288a10.675 10.675 0 0 1-5.51 9.371l-12.188 6.606c-5.22 2.841-11.569-.963-11.554-6.924v-55.15a14.935 14.935 0 0 1 7.508-12.968l45-25.763A15.58 15.58 0 0 1 98.16 22a15.011 15.011 0 0 1 4.218.586Zm0 0c6.616 1.888 11.18 7.946 11.188 14.85v117.269c.019 6.82-4.485 12.82-11.022 14.682l41.667-11.908c6.382-1.846 10.779-7.704 10.788-14.369V48.86c.003-6.683-4.415-12.556-10.819-14.384l-41.802-11.889Zm11.188 114.994H67.084c-7.964.086-10.752 10.647-3.875 14.68l27.688 15.757A15.08 15.08 0 0 0 98.381 170a14.534 14.534 0 0 0 4.168-.612c6.535-1.863 11.037-7.862 11.018-14.68v-17.127Z"></path></g></svg>"""
LEARNING_SVG = """<svg width="30px" height="30px" viewBox="-12.8 -12.8 89.60 89.60" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#36454f" stroke-width="3.3920000000000003"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><polygon points="32 36 8 24 32 12 56 24 32 36"></polygon><polyline points="48 28 48 52 16 52 16 28"></polyline><line x1="56" y1="24" x2="56" y2="44"></line></g></svg>"""
BERGVARME_SVG = """<svg version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="30px" height="30px" viewBox="-174.08 -174.08 860.16 860.16" xml:space="preserve" fill="#36454f" stroke="#36454f" stroke-width="6.656000000000001"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <style type="text/css">  .st0{fill:#36454f;}  </style> <g> <path class="st0" d="M506.391,287.074c-3.578-10.219-13.484-22-20.734-29.047c-17.188-16.672-35.688-25-44.75-29.875 c-6.75-4.047-15.313-1.594-19.188,5.484c-3.844,7.063-1.313,15.703,5.219,20.141c42.844,29.234,49.906,64.281,18.906,100.859 c-9.266,10.922-21.641,19.563-39.813,29.75c-29.734,16.656-91.094,31.313-150.031,31.234 c-58.938,0.078-120.297-14.578-150.031-31.234c-18.156-10.188-30.531-18.828-39.813-29.75c-31-36.578-23.938-71.625,18.938-100.859 c6.5-4.438,9.047-13.078,5.188-20.141c-3.844-7.078-12.438-9.531-19.156-5.484c-9.078,4.875-27.594,13.203-44.75,29.875 c-7.281,7.047-17.188,18.828-20.75,29.047C2.047,297.262,0,308.402,0,320.027c0,12.016,2.25,23.766,6.375,34.719 c7.219,19.203,19.766,35.828,35.563,50.047c23.781,21.313,55.188,37.719,91.656,49.219c36.484,11.453,78.125,17.844,122.406,17.844 s85.922-6.391,122.406-17.844c36.469-11.5,67.875-27.906,91.656-49.219c15.797-14.219,28.359-30.844,35.563-50.047 c4.125-10.953,6.391-22.703,6.375-34.719C512.016,308.402,509.953,297.262,506.391,287.074z"></path> <path class="st0" d="M239.5,314.074c7.031,15.563,15.969,25.781,22.75,31.281c6.906,5.516,12.406,7.266,16.656,4.859 c4.281-2.406,5.188-8.484,3.594-17.016c-1.594-8.578-5.156-18.859-7.609-31.172c-2.516-12.188-4.203-27.906-4.203-45.328 c0.063-8.547,0.719-17.094,2.438-25.578c1.688-8.531,4.594-17.016,8.547-27.516c3.953-10.438,8.203-22.75,10.297-35.031 c2.188-12.313,2.531-24.234,1.953-35.094c-1.328-21.406-5.563-40.516-12.594-56.141c-7.016-15.578-15.984-25.781-22.766-31.281 c-6.906-5.516-12.406-7.266-16.656-4.859c-4.281,2.406-5.172,8.5-3.563,17.016c1.594,8.594,5.156,18.859,7.609,31.172 c2.516,12.172,4.203,27.906,4.203,45.313c-0.063,8.547-0.719,17.094-2.438,25.578c-1.688,8.531-4.594,17.016-8.563,27.516 c-3.953,10.453-8.188,22.75-10.281,35.063c-2.188,12.297-2.563,24.219-1.953,35.078C228.234,279.34,232.469,298.449,239.5,314.074z "></path> <path class="st0" d="M329.094,278.465c2.063,8.656,4.938,16.734,8.438,23.719c7.094,14.141,15.938,22.828,22.469,27.266 c6.688,4.453,12,5.531,16.141,2.922s5.016-8.344,3.469-16.063c-1.516-7.781-4.906-16.797-7.109-27.313 c-2.281-10.375-3.781-24-3.563-39.078c0.156-7.359,0.906-14.578,2.625-21.703c1.719-7.172,4.578-14.344,8.594-23.563 c3.969-9.141,8.453-20.219,10.813-31.547c2.438-11.328,3-22.438,2.516-32.438c-0.516-10.047-1.859-19.016-3.922-27.719 c-2.063-8.641-4.938-16.719-8.453-23.703c-7.078-14.156-15.922-22.844-22.469-27.266c-6.688-4.453-12-5.531-16.141-2.922 s-5,8.328-3.469,16.063c1.531,7.766,4.922,16.797,7.125,27.297c2.281,10.375,3.781,24,3.563,39.063 c-0.188,7.359-0.922,14.578-2.656,21.703c-1.719,7.172-4.594,14.344-8.594,23.578c-4,9.141-8.469,20.234-10.813,31.563 c-2.438,11.344-2.984,22.438-2.5,32.422C325.688,260.793,327.031,269.762,329.094,278.465z"></path> <path class="st0" d="M129.625,278.465c2.063,8.656,4.938,16.734,8.469,23.719c7.094,14.141,15.906,22.828,22.469,27.266 c6.688,4.453,12,5.531,16.125,2.922c4.156-2.609,5.016-8.344,3.469-16.063c-1.516-7.766-4.906-16.797-7.125-27.313 c-2.281-10.375-3.781-24-3.563-39.078c0.172-7.359,0.922-14.578,2.656-21.703c1.703-7.172,4.547-14.344,8.578-23.563 c3.984-9.141,8.453-20.219,10.797-31.547c2.453-11.328,3.016-22.438,2.516-32.438c-0.516-10.047-1.859-19-3.891-27.719 c-2.063-8.641-4.969-16.719-8.469-23.703c-7.094-14.141-15.938-22.844-22.469-27.281c-6.688-4.453-12-5.516-16.156-2.906 c-4.125,2.609-5,8.328-3.438,16.063c1.516,7.766,4.891,16.781,7.094,27.297c2.281,10.375,3.781,24,3.563,39.063 c-0.188,7.359-0.922,14.578-2.656,21.703c-1.719,7.172-4.563,14.344-8.594,23.578c-3.969,9.141-8.453,20.234-10.813,31.563 c-2.422,11.328-2.984,22.438-2.484,32.422C126.25,260.793,127.578,269.762,129.625,278.465z"></path> </g> </g></svg>"""

st.title('Hei! Jeg er Magne Syljuåsen')

st.write(''' 
         Sivilingeniør fra NTNU, og jobber som rådgiver innen bergvarme i Asplan Viak. 
         Har stor interesse for teknologi og er optatt av hvordan det kan bidra til å skape nye løsninger
         samt effektivisere arbeidsoppgaver. Jobber i dag mye med programmering i Python og Streamlit for å 
         lage ulike verktøy knyttet til helhetlig energiplanlegging og bergvarme. 
         ''')

tab1, tab2, tab3 = st.tabs(['Tidligere prosjekter', 'Teknologier jeg bruker', 'Om meg'])
with tab1:
    st.header('Bergvarmekalkulatoren')

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
    st.markdown(f'<a target="parent" style="font-size: 1.1rem; border-radius: 15px; text-align: left; padding: 0rem; min-height: 60px; display: inline-block; box-sizing: border-box; width: 100%; transition: background-color 0.3s;" href="https://www.varmepumpeinfo.no/bergvarme/kalkulator">Tjenesten ligger ute på varmepumpeinfo.no. Prøv den her!</a>', unsafe_allow_html=True)
    items = [
        dict(
            title="",
            text="",
            img="src/data/bergvarmekalkulator_showcase.png",
            link=""
        ),
        dict(
            title="",
            text="",
            img="src/data/bergvarmekalkulator_showcase_3.png",
            link=""
        ),
    ]
    carousel(items=items, container_height=600)

    st.header('AV-Energiplanlegging')
    st.write("""
                AV Energiplanlegging er en samling verktøy utviklet av 
                Asplan Viak til å beregne energi og effektbehov til en 
                bygningsmasse. Alt fra nabolag opp til hele kommuner og fylker. 
                Verktøyene kan brukes til å finne de beste energiforsyningsløsningene, 
                mtp. klimagassutslipp, kostnader, flaskehalser og hvordan disse kan løses. 
                """)
    st.markdown(f'<a target="parent" style="font-size: 1.1rem; border-radius: 15px; text-align: left; padding: 0rem; min-height: 60px; display: inline-block; box-sizing: border-box; width: 100%; transition: background-color 0.3s;" href="https://www.asplanviak.no/verktoy/av-energiplanlegging/">Les mer om verktøyene her.</a>', unsafe_allow_html=True)
    items = [
        dict(
            title="",
            text="",
            img="src/data/kringsjå_showcase.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/tempe_showcase.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/kildrift_showcase.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/melhus_showcase.png"
        ),
    ]
    carousel(items=items, container_height=600)


    st.header('AV-Energi')
    st.write("""
                AV-Energi er en intern webside for de som jobber med rådgivning
                innen energiforsyningsløsninger i Asplan Viak. Det er en 
                intern samhandlingsplattform for å forenkle, forbedre 
                og effektivisere repetetive arbeidsoppgaver. 
                Her vises noen skjermbilder av løsningene som finnes:""")
    items = [
        dict(
            title="",
            text="",
            img="src/data/internside_showcase.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/internside_showcase_5.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/internside_showcase_2.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/internside_showcase_4.png"
        ),
        dict(
            title="",
            text="",
            img="src/data/internside_showcase_3.png"
        )
    ]
    carousel(items=items, container_height=600)

with tab2:
    st.header('Teknologier')
    st.write('Dette er noen av teknologiene jeg har erfaring med:')
    render_svg(svg=PYTHON_SVG, text=""" Python og da særlig pakkene numpy og pandas for beregninger og plotly for visualisering. Bred erfaring med oppkobling mot API'er og ulike databaser.  """)
    render_svg(svg=GIS_SVG, text=""" Open-source GIS-tjenester som Folium (2D) og Pydeck (3D). GeoPandas, pandas og shapely for geografisk dataprosessering.""")
    render_svg(svg=FRONTEND_SVG, text=""" Frontend-utvikling med Streamlit, CSS og HTML. Har også brukt low-code-plattformen Webflow.""")
    render_svg(svg=ARCGIS_SVG, text=""" ArcGIS for å lage flere Python-toolboxer til Arcgis Pro samt utvikling av low-code apper i ArcGIS Online. """)
    render_svg(svg=BERGVARME_SVG, text=""" Earth Energy Designer og Pygfunction for å dimensjonere brønnparker og GeoTermos-systemer.""") 
    render_svg(svg=AUTOCAD_SVG, text=""" AutoCAD for prosjektering av brønner i byggetegninger. """)
    render_svg(svg=SOURCE_SVG, text=" GitHub og Azure DevOps for kildekodehåntering.")
    render_svg(svg=AI_SVG, text=""" ChatGPT som jeg bruker i det daglige for tekst og kode. """)
    render_svg(svg=MICROSOFT_SVG, text=""" MS Office for dagligdagse oppgaver med Word, PowerPoint og Excel. """)
    render_svg(svg=PROGRAMMING_SVG, text=""" Programmeringspråk som MATLAB, C++, JavaScript og React der jeg har litt erfaring.""")
    st.write('Jeg er alltid interessert i å lære meg nye teknologier :-)')
    
with tab3:
    st.header('Om meg')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image('src/personal-img/presentasjon.png', caption='Midt i en presentasjon for næringslivsforeningen i Stjørdal')
    with c2:
        st.image('src/personal-img/påtur.png', caption='På fjelltur med min samboer Emma!')
    with c3:
        st.image('src/personal-img/medhund.png', caption='Vanligvis er jeg ikke så god med hunder, men denne var veldig rolig:-) ')
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image('src/personal-img/landslaget.png', caption='Toppen av fotballkarrieren - spilte på student-fotballlandslaget i EM i Portugal i 2018')
    with c2:
        st.image('src/personal-img/idanmark.png', caption='På tur i København til mine hjemtrakter. Her bodde jeg i 8 år da jeg var barn.') 
    with c3:
        st.image('src/personal-img/hytta.png', caption='Utsikten fra hytta på fjellet. Her er det godt å koble av!')
c1, c2, c3 = st.columns(3)
with c1:
    render_click_logos(svg = LINKEDIN_SVG, text = "LinkedIn", link_url = "https://www.linkedin.com/in/magne-sylju%C3%A5sen-35235738/")
with c2:
    render_click_logos(svg = GITHUB_SVG, text = "GitHub", link_url = "https://github.com/magnesyljuasen")
with c3:
    render_click_logos(svg = CODING_SVG, text = "CV", link_url = "https://github.com/magnesyljuasen/streamlit-portfolio/blob/main/CV.pdf")
