import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('princess.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome to fifa prediction app'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(movement_reactions,potential,value_eur,power_shot_power,attacking_short_passing,skill_long_passing,passing,dribbling,attacking_volleys,mentality_composure,mentality_vision,physic,player_positions):
    prediction = classifier.predict(
        [[movement_reactions,potential,value_eur,power_shot_power,attacking_short_passing,skill_long_passing,passing, dribbling,player_positions,attacking_volleys,mentality_composure,mentality_vision,physic]])
    print(prediction)
    return prediction

    # this is the main function in which we define our webpage


def main():
    # giving the webpage a title
    st.title("Fifa Overall Rating Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Fifa Player Overall Rating Prediction </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    st.sidebar.title("please enter the parameters")  # get input values
    movement_reactions = st.sidebar.slider('movement_reactions')
    potential = st.sidebar.slider("potential")
    value_eur = st.sidebar.slider("Value Eur")
    power_shot_power = st.sidebar.slider("Power short power")
    attacking_short_passing= st.sidebar.slider("attacking short passing")

    dribbling = st.sidebar.slider("dribbling")
    passing = st.sidebar.slider("passing")
    physic = st.sidebar.slider("physic")
    mentality_composure = st.sidebar.slider("mentality composure")
    mentality_vision = st.sidebar.slider("mentality vision")

    skill_long_passing = st.sidebar.slider("skill long passing")
    player_positions = st.sidebar.slider("player positions")
    attacking_volleys = st.sidebar.slider("attacking volleys")

    result = ""


    if st.button("Predict"):
        result = prediction(movement_reactions,potential,value_eur,power_shot_power,attacking_short_passing,skill_long_passing,passing,dribbling,player_positions,attacking_volleys,mentality_composure,mentality_vision,physic)
    st.success('Overall rating is {}'.format(result))


if __name__ == '__main__':
    main()
