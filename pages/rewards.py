"""Recommendations page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Recommendations :memo:")
    
    
    ### True Lab Startup Sandbox Hackaton
    st.markdown(
        """### 1 of 4 teams True Lab Startup Sandbox Hackaton
* Image Recognition | DeepSec | May 2021
        """,
            unsafe_allow_html=True,)
    
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.image("./resources/images/rewards/TrueHackaton_1.jpg")

    st.markdown(
        """

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Under Startup Sandbox, the True Lab Startup Sandbox project is organized for new-generation startups 
and entrepreneurs interested in robotics and AI are invited to join the hack idea and recruit team members with True Group.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Selected to participate in Hackathon, a total of 10 teams (3-5 people per team). Only accept 4 teams with the best results to join the project.
        """,
            unsafe_allow_html=True,)
    
    
    ### SuperAIEngineer Competition
    st.markdown(
        """### Bronze Medal - SuperAIEngineer Competition
* Bronze Medal | 10 Oct 2019 - 31 July 2020
        """,
            unsafe_allow_html=True,)
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.image("./resources/images/rewards/AI_Engineer_1.jpg")
    
    
    st.markdown(
        """

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Super-AI engineer development program is a project 
to train and develop people in the AI profession to develop the country 
and find the top winner of Thailand. The program has selected (5%) of experienced people nationwide (2059 candidates). 
Those who qualify for each round will receive different competition problems and full-time work with leading companies 
under the Artificial Intelligence Association of Thailand (AiAT) supervision. 
[**See credential**](https://aiat.or.th/cert/) ID: SuperAI01-036
        """,
            unsafe_allow_html=True,)
    
    ### Kaggle Competition
    st.markdown(
        """### Kaggle Competition
* [**Goto Kaggle Profile**](https://www.kaggle.com/naratipboonbanyen/competitions)
        """,
            unsafe_allow_html=True,)
    
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.image("./resources/images/rewards/Kaggle_1.jpg")
    

    
    ### Nielsen: Simpli Excellent Reward 
    st.markdown(
        """### Nielsen: Simpli Excellent Reward 
        """,
            unsafe_allow_html=True,)
    
    col1, col2, col3, col4, col5 = st.columns([1,4,4,4,1])
    with col2:
        st.image("./resources/images/rewards/Nielsen_1.jpg")
    with col3:
        st.image("./resources/images/rewards/Nielsen_2.jpg")
    with col4:
        st.image("./resources/images/rewards/Nielsen_3.jpg")
        
    st.markdown(
        """
* Excellence process improvement | Jun 2020 [**See credential**](https://drive.google.com/file/d/1qC5iRpSJjXz8jmaNh1-iZwbSgiVIB6rQ/view?usp=sharing)
* Hard working to achieve and exceed quarter's revenue targets. | Jul 2020 [**See credential**](https://drive.google.com/file/d/1zt8iR1ORv3a5A34r5KzUi8Z9ffTqqLYN/view?usp=sharing)
* Support revenue with an "Outward Mindset" | Dec 2020 [**See credential**](https://drive.google.com/file/d/1ljAWq8zNKwroPHGwwhwCadvAe2wCWSdc/view?usp=sharing)
        """,
            unsafe_allow_html=True,)
    
    
    
    
    ### Microsoft Office Specialist Excel 2016
    st.markdown(
    """### Microsoft Office Specialist Excel 2016
* Excel 2016: Core Data Analysis, Manipulation, and Presentation | Oct 2019.
    """,
        unsafe_allow_html=True,)
    col1, col2, col3 = st.columns([1,4,1])
    
    with col2:
        st.image("./resources/images/rewards/Excel_1.jpg")
    st.markdown(
        """

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Microsoft Excel 2016 Certification exam earners have a fundamental 
understanding of Excel 2016 and the ability to complete tasks independently. 
Earners have proven they can create and edit a workbook with multiple sheets, and use graphic 
elements to represent data visually including professional-looking budgets, 
financial statements, performance charts, and data-entry logs. Earners include students, business professionals, 
clerical workers, bookkeepers, educators, and others. 
[**See credential**](https://www.credly.com/badges/74ae2a84-0ec7-4099-bf4d-40a37da69410/linked_in_profile)
        """,
            unsafe_allow_html=True,)
    
    
if __name__ == "__main__":
    main()

