"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    
    st.title("About Me")
    
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.image("./resources/images/kim.jpg")
    
    st.markdown(
            """
"_I'm a bronze medalist in the Super AI Engineer competition._"


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A Data processing with 1.5 years of experience in managing data, developing reports, and troubleshooting data issues. 
Spending more than 1 year to upskill and join to competition about AI/ML and Data science competition. 
Always on the lookout for new technologies, I am passionate about AI technology and data science to drive business.
 ***
**Open to work **\n
**Data Analyst · Data Scientist · Machine Learning Engineer · Artificial Intelligence Engineer**

[**LinkedIn**](https://www.linkedin.com/in/naratip-boonbanyen-86778717b/) | [**Email**](mailto:nrtp.boon@gmail.com) | [**GitHub**](https://github.com/kimlolipop)
""",unsafe_allow_html=True,)
    
    

if __name__ == "__main__":
    main()
