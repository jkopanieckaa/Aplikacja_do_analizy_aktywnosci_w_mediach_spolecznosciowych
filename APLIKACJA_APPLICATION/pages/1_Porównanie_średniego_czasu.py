import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title = "Porówanie średniego czasu na social mediach",layout="wide")

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

st.header("Twój czas na social mediach na tle innych użytkowników", divider="blue", text_alignment="center")

data = pd.read_csv("./social_media_dataset_united.csv")
df = pd.DataFrame(data)

user_time = st.number_input("Wprowadź swój czas na social mediach w minutach na dobę", step=1)
user_age = st.pills('Wybierz swój przedział wieku',("0-18",'19-35','36-50','50+'), selection_mode='single')
used_platform = st.pills("Wybierz platformę",('TikTok','Instagram', 'Facebook', 'X','Snapchat','YouTube'),selection_mode='single')

if user_age=='0-18':
    df=df[df['age']<=18]
elif user_age == '19-35':
    df=df[(df['age']>=19)&(df['age']<=35)]
elif user_age == '36-50':
    df = df[(df['age'] >= 36) & (df['age'] <= 50)]
elif user_age == '50+':
    df=df[df['age'] > 50]

if used_platform:
    df = df[df['social_media_platform']== used_platform]


# #tworzenie figury
# fig,ax = plt.subplots(figsize = (10,5))
#
# ax.hist(time,bins = 60, color='#006c3f', edgecolor='darkgreen')
# ax.axvline(users_time,color='red',linestyle='-.',linewidth=2, ymin=0,ymax=0.95)
# ax.text(users_time - 20, ax.get_ylim()[1]* 0.96,"Twój czas" )
#
# ax.set_xlabel("Czas na social media [minuty]")
# ax.set_yticks([])
#
# st.pyplot(fig)

#inny sposób tworzenia figury

if user_time <= 120:
    time_label = "low"
elif user_time <= 240:
    time_label = "medium"
elif user_time <= 360:
    time_label = "high"
else:
    time_label = "very_high"



if 0 < user_time <= 1440:
    fig = px.histogram(df, x="screen_time_min", nbins=70, color_discrete_sequence=['#8FBDE0'])
    fig.update_traces(marker = dict(line=dict(width=0.5, color='black')), hovertemplate = "Czas: %{x}<br>")
    fig.add_vline(x=user_time, line_dash='dash', line_color='red',annotation_text = "Twój czas na social mediach", annotation_position='top')
    fig.update_layout(xaxis_title = "Czas na social mediach [minuty]", yaxis_title = '', bargap = 0.1)
    fig.update_yaxes(showticklabels=False)

    st.plotly_chart(fig)


    if time_label == "low":
        st.success("""
        Twój czas ekranowy znajduje się w przedziale, który według danych wiąże się
        z najlepszą jakością snu, niższym poziomem stresu oraz wyższym
        samopoczuciem i produktywnością.
        """)
        st.page_link("./pages/2_Ciekawostki.py", label='Kliknij, aby dowiedzieć się więcej... 🔍')
    elif time_label == "medium":
        st.info("""
        Twój czas ekranowy jest umiarkowany. Według danych to zakres, w którym
        jakość snu i samopoczucie są zwykle nadal dobre, choć zaczynają być
        widoczne pierwsze różnice w poziomie stresu i aktywności fizycznej.
        """)
        st.page_link("./pages/2_Ciekawostki.py", label='Kliknij, aby dowiedzieć się więcej...🔍')
    elif time_label == "high":
        st.warning("""
        Twój czas spędzany w mediach społecznościowych jest wysoki.
        Według danych ten zakres często wiąże się z krótszym snem, wyższym poziomem
        stresu oraz mniejszą ilością aktywności fizycznej.
        """)
        st.page_link("./pages/2_Ciekawostki.py", label='Kliknij, aby dowiedzieć się więcej...🔍')
    else:
        st.error("""
        Twój czas ekranowy jest bardzo wysoki. Według danych ten poziom
        najczęściej wiąże się z wyraźnie gorszą jakością snu,
        wyższym stresem oraz gorszym samopoczuciem psychicznym.
        """)
        st.page_link("./pages/2_Ciekawostki.py", label='Kliknij, aby dowiedzieć się więcej...🔍')

elif user_time > 1440:
    st.warning('Doba ma tylko 1440 minut. Upewnij się, że wpisujesz swój czas w minutach i spróbuj ponownie.')
else:
    st.info("Wprowadź swój czas, aby zobaczyć porównanie.")

