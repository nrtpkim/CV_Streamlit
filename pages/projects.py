"""Projects page shown when the user enters the application"""
import streamlit as st
from src.main.projects.human_detection_Yolov5 import input_frame
import tensorflow
from src.main.projects.tic_tac_toe import main_tictactoe

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects - :male-construction-worker: ")
    
    ### Realtime Human Detection
    st.markdown(""" ### Realtime Human Detection
    - Used streamlit-webrtc to streaming webcam
    - Preprocessed video with opencv
    - Detected by pretrain model Yolov5s 
    - tracted boxes by sort algorithm
    """,unsafe_allow_html=True,)
    
    option_cam = st.selectbox('Please Select Mode', ('non', 'Subtraction', 'Human_detection'))
    run_cam = st.checkbox('Open Webcam')
    if run_cam:
        st.write('comming soon')
#         demo_obj_detection = input_frame.webcam_input(run_cam, option_cam)
    
    
    st.markdown('***')
    
    ### Tic-tak-toe games 10x10 Dimension
    st.markdown(""" ### Tic-tak-toe games 8x8 Dimension
    - Rule: 5 lines in a row, column, Diagonals will win.
    - Used DNN to train RL(Just test pipeline. The model still not good)
    """,unsafe_allow_html=True,)
    
    option_tictactoe = st.selectbox('Please Select', ('Player1 vs Player2', 'Player vs Tic Tak Toe(Ai)'))
    run_tictaktoe = st.checkbox('Start Game')
    if run_tictaktoe:
        main_tictactoe.run_tictaktor(run_tictaktoe, option_tictactoe)
    
  
    
    st.markdown('***')
    
    ### Recomendation System
    st.markdown(""" ### Recomendation System
    - Wrote [**Medium**](https://medium.com/super-ai-engineer/recommendation-system-machine-learning-%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AD%E0%B8%B1%E0%B8%95%E0%B9%82%E0%B8%99%E0%B8%A1%E0%B8%B1%E0%B8%95%E0%B8%B4-e822b47c0f71) blog explaining Recomendation modeling.
    - Shared code on [**Google Colab**](https://colab.research.google.com/drive/1GNj6pBTk-Z1GmI13yub8KydtXoAhjlso?authuser=3#scrollTo=JLNGvMhp0pnI). 
    """,unsafe_allow_html=True,)

    st.image("./resources/images/recomendation_model.jpg")
    
    st.markdown('***')
    
     ### Dashboard Design on open source data
    st.markdown(""" ### Dashboard Design on open source data
    - visualized and validated data with supermarket data (Open source data)
    - Designed dashboard on theory for tracking product sales(track KPI).
    - Used python to generate dashboard
    - Shared code on [**Google Colab**](https://colab.research.google.com/drive/1V8TAvTXEyhbcpQxJ09GtJKatBiC1Jo_Z?usp=sharing). 
    """,unsafe_allow_html=True,)
    st.image("./resources/images/Supermarket_Dashboard.jfif")
    
    st.markdown('***')
    st.markdown(""" ### You can review other projects on my [**GitHub**](https://github.com/kimlolipop).""",unsafe_allow_html=True)
    
   
    


if __name__ == "__main__":
    main()
