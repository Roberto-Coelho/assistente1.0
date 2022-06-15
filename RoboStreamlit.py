from calendar import c
import streamlit as st
#from streamlit import theme
import pandas as pd
import numpy as np
import altair as alt

# with open("aparenciastreamlit.css") as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.title('Asistente Para Trader Esportivo')

option = st.selectbox(
    'Ligas',
    ('Selecione Uma Liga', 'Italia Serie A', 'Brasil Serie A'))


option1 = st.selectbox(
    'Over Gols',
    ('Todos', 0, 1, 2, 3, 4)
)

if option == 'Italia Serie A' and option1 == 'Todos Over gols':

    dados = pd.read_csv("C:/Users/Roberto/Desktop/I1.csv")
    dados['over_total'] = dados['FTHG'] + dados['FTAG']
    total_jogos = dados['HomeTeam'].count()
    dados['over_ht'] = dados['HTHG'] + dados['HTAG']
    dados['over_cantos'] = dados['Hc'] + dados['AC']

    quanti_gol_um = dados.loc[(dados['over_total'] == 1)]
    quanti_jogos_um_gol = quanti_gol_um['HomeTeam'].count()
    umgolE = quanti_jogos_um_gol/total_jogos * (100)
    umgolEX = ('{:.0f}%'.format(umgolE))

    quanti_gols_dois = dados.loc[(dados['over_total'] == 2)]
    quanti_jogos_dois_gols = quanti_gols_dois['HomeTeam'].count()
    doisgols = quanti_jogos_dois_gols/total_jogos * (100)
    doisgolsEx = ('{:.0f}%'.format(doisgols))

    quanti_over2_gols = dados.loc[(dados['over_total'] > 2)]
    quanti_jogos_dois_gols = quanti_over2_gols['HomeTeam'].count()
    over2 = quanti_jogos_dois_gols/total_jogos * (100)
    overdois = ('{:.0f}%'.format(over2))

    quanti_menos_tres = dados.loc[(dados['over_total'] < 3)]
    quanti_jogos_tres_gols = quanti_menos_tres['HomeTeam'].count()
    under3 = quanti_jogos_tres_gols/total_jogos * (100)
    undertres = ('{:.0f}%'.format(under3))

    quanti_gols_tres = dados.loc[(dados['over_total'] > 3)]
    quanti_jogos_tres_gols = quanti_gols_tres['HomeTeam'].count()
    over3 = quanti_jogos_tres_gols/total_jogos * (100)
    overtres = ('{:.0f}%'.format(over3))

    quanti_gols_quatro = dados.loc[(dados['over_total'] > 4)]
    quanti_jogos_quatro_gols = quanti_gols_quatro['HomeTeam'].count()
    over4 = quanti_jogos_quatro_gols/total_jogos * (100)
    overquatro = ('{:.0f}%'.format(over4))

    quanti_cantos = dados.loc[(dados['over_cantos'] > 10)]
    quanti_jogos_cantos = quanti_cantos['HomeTeam'].count()
    overcantos = quanti_jogos_cantos/total_jogos * (100)
    overc = ('{:.0f}%'.format(overcantos))

    quanti_cantos_menos = dados.loc[(dados['over_cantos'] < 10)]
    quanti_jogos_cantos_menos = quanti_cantos_menos['HomeTeam'].count()
    undercantos = quanti_jogos_cantos_menos/total_jogos * (100)
    underc = ('{:.0f}%'.format(undercantos))

    quanti_cantos_exa = dados.loc[(dados['over_cantos'] == 10)]
    quanti_jogos_cantos_exa = quanti_cantos_exa['HomeTeam'].count()
    cantosexa = quanti_jogos_cantos_exa/total_jogos * (100)
    cantosexatos = ('{:.0f}%'.format(cantosexa))

    if st.button('Ver tendencias'):
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        col1.metric('Total de Jogos até agora', f'{total_jogos}', '')
        col2.metric('Um Gol Exato', f'{umgolEX}', '')
        col3.metric('Dois Gols Exatos', f'{doisgolsEx}', '')
        col4.metric('Over dois', f'{overdois}', '')
        col5.metric('Under 3', f'{undertres}', '')
        col6.metric(f'Over 3,5', f'{overtres}', '')
        col7.metric('Over 4,5', f'{overquatro}', '')

    if st.button('Ver Cantos'):
        c1, c2, c3 = st.columns(3)
        c1.metric('over 10 cantos', f'{overc}', '')
        c2.metric('under 10 cantos', f'{underc}', '')
        c3.metric('Exatamente 10 cantos', f'{cantosexatos}', '')


if option == 'Brasil Serie A':
    dados = pd.read_excel(r'C:\Users\Roberto\Desktop\Intervalo1.xlsx')
    dados['over_total'] = dados['Hfinal'] + dados['Afinal']
    dados['over_ht'] = dados['H1t'] + dados['A1t']

    quanti_gol_um = dados.loc[(dados['over_total'] == 1)]
    quanti_jogos_um_gol = quanti_gol_um['Home'].count()
    umgol = quanti_jogos_um_gol/dados['Home'].count() * (100)
    umgolex = ('{:.0f}%'.format(umgol))

    quanti_gol_over2 = dados.loc[(dados['over_total'] > 2)]
    quanti_jogos_over2_gols = quanti_gol_over2['Home'].count()
    over2gol = quanti_jogos_over2_gols/dados['Home'].count() * (100)
    over2 = ('{:.0f}%'.format(over2gol))

    quantijogo = dados['Home'].count()

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric('Total de Jogos até agora', f'{quantijogo}', '')
    col2.metric('Um Gol Exato', f'{umgolex}', '')
    col3.metric('Over 2,5', f'{over2}', '')


#escanteios_totais_C = dados.HC
