"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """
## Languages
- Python
- SQL 
- VBA for MS Excel

## Platforms and Libraries
- **MS Office** - Excel, Powerpoint, Word, Access
- **Python** - Pandas, Numpy, Skicit Learn, Scipy, Tensorflow, Keras, Opencv, PyThaiNLP, Streamlit, FastAPI, Matplotlib, Seaborn, etc.
- **SQL** - MS SQL, MS Access, Oracle,  
- Tableau

## Analytical Skills
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Web Scraping

## Huawei Stack
- EC2

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
