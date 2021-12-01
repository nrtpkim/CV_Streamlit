from src.main.projects.tic_tac_toe import p1vsp2
from src.main.projects.tic_tac_toe import PlayerVsBot
# import PlayerVsBot
import streamlit as st



def run_tictaktor(run, option):
#     option_tictactoe = st.selectbox('Please Select', ('Player1 vs Player2', 'Player vs Tic Tak Toe(Ai)'))
#     run_tictaktoe = st.checkbox('Run_tictaktoe')
    if run:
        if option == "Player1 vs Player2":
            p1vsp2.show()

        elif option == "Player vs Tic Tak Toe(Ai)":
            PlayerVsBot.show()

    