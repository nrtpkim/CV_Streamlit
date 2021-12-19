"""Projects page shown when the user enters the application"""
import streamlit as st
from src.main.projects.human_detection_Yolov5 import input_frame
from src.main.projects.tic_tac_toe import main_tictactoe

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects - :male-construction-worker: ")

    st.markdown("""&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; this is some part of the project I was able to do. If want to read more, check on my [**GitHub**](https://github.com/kimlolipop).
     """,unsafe_allow_html=True,)
#     st.write("You can call me Kim and this is my part of the project I was able to do.")
    
    ### Realtime Human Detection
    st.markdown(""" ### Realtime Human Detection
    - Used streamlit-webrtc to streaming webcam
    - Preprocessed video with opencv
    - Detected by pretrain model Yolov5s 
    - tracted boxes by sort algorithm
    """,unsafe_allow_html=True,)
    
    option_cam = st.selectbox('Please Select Mode', ("Default", "Subtraction"))
    demo_obj_detection = input_frame.webcam_input(option_cam)
    
    
    st.markdown('***')
    
    ### Recomendation System
    st.markdown(""" ### Recomendation System
    - Wrote [**Medium**](https://medium.com/super-ai-engineer/recommendation-system-machine-learning-%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AD%E0%B8%B1%E0%B8%95%E0%B9%82%E0%B8%99%E0%B8%A1%E0%B8%B1%E0%B8%95%E0%B8%B4-e822b47c0f71) blog explaining Recomendation modeling.
    - Shared code on [**Google Colab**](https://colab.research.google.com/drive/1GNj6pBTk-Z1GmI13yub8KydtXoAhjlso?authuser=3#scrollTo=JLNGvMhp0pnI). 
    """,unsafe_allow_html=True,)

    st.image("./resources/images/recomendation_model.jpg")
    
    st.markdown('***')
    
     ### Tranfer learning Packaging Classification
    st.markdown(""" ###  Tranfer Learning Packaging Classification
    - Used tranfer learnign method to create model.
    - Used repurposing a pre-trained model method to finetune model.
    - This model classify 9 class of packaging
    - Used FastAPI to create RESTful API
    - Shared code on [**Repo-Tranfer-learning-Packaging-Classification**](https://github.com/kimlolipop/Docker_Tranfer-learning-Packaging-Classification). 
     """,unsafe_allow_html=True,)
    

    st.image("./resources/images/s3-s6-Strategy.jpg", "Size-Similarity matrix (left) and decision map for fine-tuning pre-trained models (right).")
        
    st.image("./resources/images/packaging-9class.jpg", "packaging 9 class") 

    st.markdown('***')
    
    ### API Iris Classification
    st.markdown(""" ###  RESTful API For AI Model
    - Used Flask API library to create RESTful API.
    - Used random forest model to create model predict species iris.
    - Shared code on [**Repo-API Iris RFClassification**](https://github.com/kimlolipop/API_Iris_RFClassification). 
     """,unsafe_allow_html=True,)
    
    st.image("./resources/images/iris.png")
    
    st.markdown('***')
    
    
    ### Titanic - Predict survival on the Titanic
    st.markdown(""" ### Titanic - Predict survival on the Titanic
    
    - Exploratory Data Analysis and do feature engineering from the data insight.
    - Used classical machine learning(Decision Tree, GaussianNB, MLPClassifier, Catboost, lightgbm, XGboost) and 
    - Used ensemble methods for combining model.
    - Used KFold crossvalidation for validating model
    - Shared code on [**Kaggle-Titanic**](https://www.kaggle.com/naratipboonbanyen/titanic#KFold-crossvalidation). 
     """,unsafe_allow_html=True,)
    
    st.image("./resources/images/titanic.png")
    
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
    
    ### Dashboard Design on open source data
    st.markdown(""" ### VRP Problem with Ant Colony Algorithm
    - Used Ant Colony Algorithm to solve Dynamic Vehicle Routing Problem.
    - Shared code on [**Repo-DVRP-AntColony**](https://github.com/kimlolipop/DVRP-AntColony). 
    """,unsafe_allow_html=True,)
    st.image("./resources/images/ACO.jpg")
    
    
    st.markdown('***')

    st.markdown(""" ### You can review other projects on my [**Github**](https://github.com/kimlolipop).
    """,unsafe_allow_html=True)
    
    
   
    
   
    


if __name__ == "__main__":
    main()
