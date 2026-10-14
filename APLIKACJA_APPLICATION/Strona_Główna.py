import streamlit as st

st.set_page_config(
    page_title = "Strona Główna",
    layout="wide", initial_sidebar_state="expanded")

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("Gdzie jesteś na tle innych użytkowników?", text_alignment="center")
st.markdown("Sprawdź, jak Twój czas spędzany w mediach społecznościowych wypada na tle danych dotyczących snu, stresu i samopoczucia.",text_alignment="center")

col1, col2, col3 = st.columns([4, 3, 4])

with col2:
    st.page_link("pages/1_Porównanie_średniego_czasu.py",label="Kliknij aby przejść dalej... 👀",width="content")


st.markdown("---")
with st.expander("Źródła danych 📂", expanded=True):
    st.markdown("""
    - [Social Media Mental Health Indicators Dataset](https://www.kaggle.com/datasets/sonalshinde123/social-media-mental-health-indicators-dataset)
    - [Screen Time vs Mental Wellness Survey - 2025](https://www.kaggle.com/datasets/adharshinikumar/screentime-vs-mentalwellness-survey-2025)
    - [Social_Media_Students_Dataset (2025)](https://www.kaggle.com/datasets/aminasalamt/social-media-dataset-2025)
    - [Mental Health & Social Media Balance Dataset](https://www.kaggle.com/datasets/prince7489/mental-health-and-social-media-balance-dataset)
    - [Dark Side Of Social Media](https://www.kaggle.com/datasets/muhammadroshaanriaz/time-wasters-on-social-media)
    """)
