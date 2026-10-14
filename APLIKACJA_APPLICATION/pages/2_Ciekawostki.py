import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title = "Ciekawostki",layout="wide", page_icon= "🕵🏻‍♀️")

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

st.header("Co mówią dane o czasie spędzanym w mediach społecznościowych?", text_alignment="center")
st.markdown("Na podstawie wybranych baz danych sprawdziliśmy, jak czas ekranowy wiąże się ze snem, stresem, aktywnością fizyczną i samopoczuciem.", text_alignment="center")

st.markdown("""### Co oznaczają dane wykresy? 
Każdy wykres pokazuje **średnie wartości** dla różnych przedziałów czasu ekranowego. Nie oznacza to, że social media są jedyną przyczyną tych zmian — wykresy pokazują **ogólne trendy widoczne w danych**.""")

st.info("Średni czas korzystania z mediów społecznościowych wynosi około **209 minut dziennie** (3 godziny i 29 minut). To właśnie wokół tej wartości zaczynają być widoczne istotne różnice w śnie, poziomie stresu i samopoczuciu.")
st.markdown("Poniższe wykresy pokazują ogólne trendy obserwowane w danych, a nie indywidualne diagnozy użytkowników.")
st.caption("⬅ ➡ Przeglądaj wykresy, aby zobaczyć wpływ czasu ekranowego na różne obszary życia")


sleep_hours_data = pd.read_csv("./sleep_hours.csv")
happiness_data = pd.read_csv("./happiness_level.csv")
physical_activity_data = pd.read_csv("./physical_activity_min.csv")
sleep_quality_data = pd.read_csv("./sleep_quality.csv")
stress_data = pd.read_csv("./stress_level.csv")

df_sleep_hours = pd.DataFrame(sleep_hours_data)
df_happiness = pd.DataFrame(happiness_data)
df_physical_activity = pd.DataFrame(physical_activity_data)
df_sleep_quality = pd.DataFrame(sleep_quality_data)
df_stress_level = pd.DataFrame(stress_data)

bins = [30, 60, 120, 180, 240, 300, 360, 420, 999]
labels = ["30–60", "60–120", "120–180", "180–240", "240–300", "300–360", "360–420", "420+"]

# czas ekranu vs sen
df_sleep_hours["time_bin"] = pd.cut(df_sleep_hours["social_media_time_min"],bins=bins,labels=labels)
sleep_grouped = (df_sleep_hours.groupby("time_bin", observed=True)["sleep_hours"].mean().reset_index())
fig_sleep = px.line(sleep_grouped,x="time_bin",y="sleep_hours",markers=True)
fig_sleep.update_layout(xaxis_title="Czas przed ekranem [minuty]",yaxis_title="Średnia ilość snu [godziny]")

# czas ekranu vs sleep quality
df_sleep_quality["time_bin"] = pd.cut(df_sleep_quality["screen_time_min"],bins=bins,labels=labels)
sleep_quality_grouped = (
df_sleep_quality.groupby("time_bin", observed=True)["Sleep_Quality(1-10)"].mean().reset_index())
fig_sleep_quality = px.line(sleep_quality_grouped, x="time_bin", y="Sleep_Quality(1-10)", markers=True)
fig_sleep_quality.update_layout(xaxis_title="Czas przed ekranem [minuty]", yaxis_title="Średnia jakość snu (1–10)")

# czas ekranu vs happiness level
df_happiness["time_bin"] = pd.cut(df_happiness["screen_time_min"],bins=bins,labels=labels)
happiness_grouped = (df_happiness.groupby("time_bin", observed=True)["Happiness_Index(1-10)"].mean().reset_index())
fig_happiness = px.line(happiness_grouped, x="time_bin", y="Happiness_Index(1-10)", markers=True)
fig_happiness.update_layout(xaxis_title="Czas przed ekranem [minuty]", yaxis_title="Średni poziom szczęścia (1–10)")

# czas ekranu vs physical activity min
df_physical_activity["time_bin"] = pd.cut(df_physical_activity["social_media_time_min"],bins=bins,labels=labels)
physical_activity_grouped = (
df_physical_activity.groupby("time_bin", observed=True)["physical_activity_min"].mean().reset_index())
fig_physical_activity = px.line(physical_activity_grouped, x="time_bin", y="physical_activity_min",markers=True)
fig_physical_activity.update_layout(xaxis_title="Czas przed ekranem [minuty]", yaxis_title="Średni czas aktywności fizycznej [minuty]")

# czas ekranu vs stress level
df_stress_level["time_bin"] = pd.cut(df_stress_level["screen_time_min"],bins=bins,labels=labels)
stress_grouped = (df_stress_level.groupby("time_bin", observed=True)["Stress_Level(1-10)"].mean().reset_index())
fig_stress = px.line(stress_grouped, x="time_bin", y="Stress_Level(1-10)", markers=True)
fig_stress.update_layout(xaxis_title="Czas przed ekranem [minuty]", yaxis_title="Średni poziom stresu (1–10)")

# karuzela
descriptions = {
    "Średnia ilość snu":
    "Im więcej czasu spędzamy przed ekranem, tym krótszy staje się sen. "
    "Wieczorne korzystanie z telefonu może opóźniać zasypianie i obniżać regenerację organizmu.\n\n"
    "**Skala:** Wartości podane są w **godzinach** (np. 8 oznacza osiem godzin snu na dobę).",

    "Jakość snu":
    "Jakość snu spada wraz ze wzrostem czasu ekranowego. "
    "Nawet jeśli długość snu się nie zmienia, intensywna ekspozycja na ekran "
    "często oznacza płytszy i mniej regenerujący sen.\n\n"
    "**Skala 1 do 10:**\n"
    "1 – bardzo zła jakość snu (częste wybudzanie, zmęczenie rano)\n"
    "10 – doskonały, głęboki i w pełni regenerujący sen",

    "Poziom szczęścia":
    "Dłuższy czas spędzany w mediach społecznościowych wiąże się z niższym poziomem szczęścia. "
    "Może to wynikać z porównań społecznych oraz zmęczenia psychicznego.\n\n"
    "**Skala 1 do 10:**\n"
    "1 – skrajne niezadowolenie z życia i przygnębienie\n"
    "10 – pełnia szczęścia i świetne samopoczucie",

    "Aktywność fizyczna":
    "Wraz ze wzrostem czasu ekranowego spada ilość aktywności fizycznej. "
    "Mniej snu i więcej stresu oznaczają mniej energii do ruchu.\n\n"
    "**Skala:** Wartości podane są w **minutach** dziennie (np. 45 oznacza 45 minut ruchu w ciągu dnia).",

    "Poziom stresu":
    "Im więcej czasu w social mediach, tym wyższy średni poziom stresu. "
    "Stres ten może być zarówno skutkiem przeciążenia informacyjnego, "
    "jak i gorszej jakości snu.\n\n"
    "**Skala 1 do 10:**\n"
    "1 – całkowity brak stresu (pełen relaks i spokój)\n"
    "10 – ekstremalnie wysoki, przytłaczający stres"
}

if "chart_index" not in st.session_state:
    st.session_state.chart_index = 0

charts = [("Średnia ilość snu", fig_sleep), ("Jakość snu", fig_sleep_quality), ("Poziom szczęścia", fig_happiness),
          ("Aktywność fizyczna", fig_physical_activity), ("Poziom stresu", fig_stress)]
col_l, col_c, col_r = st.columns([1, 8, 1])

with col_l:
    if st.button("⬅"):
        st.session_state.chart_index = (st.session_state.chart_index - 1) % len(charts)
with col_r:
    if st.button("➡"):
        st.session_state.chart_index = (st.session_state.chart_index + 1) % len(charts)

title, fig_to_show = charts[st.session_state.chart_index]

with col_c:
    st.markdown(f"<h3 style='text-align: center;'>{title}</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_to_show, use_container_width=True)
    st.caption(descriptions[title], text_alignment="center")

# st.markdown("""
# ### Co łączy te wszystkie wykresy?
#
# Z danych wyłania się spójny mechanizm:
# **czas ekranowy wpływa na sen, sen wpływa na stres, a stres wpływa na aktywność i samopoczucie**.
# Nie są to pojedyncze zależności, lecz system wzajemnie powiązanych czynników.
# """)
#
# st.warning("""
# 🧩 **Efekt domina**
#
# mniej snu → więcej stresu → mniej ruchu → gorsze samopoczucie.
#
# Dobra wiadomość? Działa to też w drugą stronę.
# Nawet niewielkie ograniczenie czasu ekranowego wieczorem
# może uruchomić pozytywną reakcję łańcuchową.
# """)
#
#
# st.markdown("""
# ### Najważniejsze obserwacje z danych
# - Krótszy czas ekranowy zwykle wiąże się z **lepszą jakością snu** i **niższym poziomem stresu**.
# - Umiarkowany czas korzystania z mediów społecznościowych często daje **najlepszy balans**
#   między snem, samopoczuciem i aktywnością fizyczną.
# - Bardzo długi czas ekranowy (powyżej kilku godzin dziennie) częściej wiąże się z:
#   - krótszym i gorszym snem,
#   - wyższym poziomem stresu,
#   - gorszym samopoczuciem psychicznym.
# """)
#
# st.markdown("""
# ### Dlaczego te czynniki są ze sobą powiązane?
# Dane sugerują, że wiele z tych elementów wzajemnie na siebie wpływa.
# Dłuższy czas ekranowy często wiąże się z krótszym snem, a niedobór snu
# z wyższym poziomem stresu. Wyższy stres może z kolei obniżać produktywność
# i ograniczać chęć do aktywności fizycznej, co wpływa na ogólne samopoczucie.
#
# Nawet niewielkie zmiany — takie jak skrócenie czasu ekranowego wieczorem lub lepsze dbanie o sen — mogą pozytywnie wpłynąć na samopoczucie i poziom stresu.
# """)
#
# st.success("""
# 💡 **Ciekawostka**:
#  Najlepsze średnie wyniki snu, stresu i samopoczucia
# pojawiają się przy umiarkowanym czasie ekranowym —
# nie przy jego całkowitym braku, ale też nie przy kilku godzinach dziennie.
# """)

st.markdown("""
### Co łączy te wszystkie wykresy?

Z danych wyłania się spójny mechanizm wzajemnie powiązanych czynników. Nie są to pojedyncze zależności, lecz cały system.
""")

st.warning("""
🧩 **Efekt domina:** zbyt długi czas ekranowy skraca sen → niewyspanie potęguje stres → to z kolei odbiera chęci do ruchu i drastycznie pogarsza samopoczucie.

Dobra wiadomość? Ten mechanizm działa w obie strony! Nawet niewielkie ograniczenie czasu ekranowego (zwłaszcza wieczorem) może uruchomić pozytywną reakcję łańcuchową, poprawiając od razu kilka aspektów życia.
""")

st.markdown("""
### Najważniejsze obserwacje z danych
- **Skrajności nie służą:** Bardzo długi czas przed ekranem (powyżej kilku godzin dziennie) to niemal gwarancja krótszego snu, wyższego napięcia nerwowego i gorszego samopoczucia psychicznego.
- **Mniej znaczy lepiej:** Ograniczenie czasu ekranowego wyraźnie koreluje z lepszą jakością snu i niższym poziomem stresu.
""")

st.success("""
💡 **Ciekawostka: Efekt Złotowłosej** \n
Najlepsze średnie wyniki snu, stresu i samopoczucia pojawiają się przy **umiarkowanym** czasie ekranowym — a nie przy jego całkowitym braku, ani tym bardziej przy wielu godzinach dziennie.
""")