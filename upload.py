import streamlit as st
from PIL import Image
#im = Image.open('')
#st.image(Im,width = 700,caption = "Fifa 2021")
#app title
html_temp = """
<div style = "background-color:blue;padding:1.5px">
<h1 style= 'color:white;text-align:center;'>Overall Score Prediction </h1>
</div> <br> """
st.markdown(html_temp,unsafe_allow_html = True)

#get input values
st.sidebar.title("please enter the parameters")#get input values
potential = st.sidebar.slider("input the f")
value_eur = st.sidebar.slider("input the f")
power_shot_power= st.sidebar.slider("input the f")
attacking_short_passing =st.sidebar.slider("input the f")
skill_long_passing =st.sidebar.slider("input the f")
passing = st.sidebar.slider("input the f")
dribbling = st.sidebar.slider("input the f")
goalkeeping_positioning =st.sidebar.slider("input the f")
goalkeeping_reflexes = st.sidebar.slider("input the f")
goalkeeping_diving = st.sidebar.slider("input the f")
goalkeeping_hadling = st.sidebar.slider("input the f")
goalkeeping_kicking = st.sidebar.slider("input the f")
attacking_volleys = st.sidebar.slider("input the f")
player_positions = st.sidebar.slider("input the f")

def CsMPa():
    my_dict = {
        'potential': potential,
        'value_eur': value_eur,
        'power_shot_power':power_shot_power,
        'attacking_short_passing':attacking_short_passing
        
        
        
    }

import pandas as pd
df = pd.DataFrame.from_dict(['my_dict'])
df
df = CsMPa()

model = pickle.load(open('xgb','rb'))
if st.sidebar.button('Submit'):
    result = (model.predict(dfc))
    st.success(result)

streamlit.run fifa20.py