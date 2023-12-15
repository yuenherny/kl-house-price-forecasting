import streamlit as st

def get_about_section():

    st.header("Author")
    st.write(
        "This app was created by [Yuen Hern](https://github.com/yuenherny), as part of his Master's project. "
        "Please reach out via [LinkedIn](https://www.linkedin.com/in/yuenhernyu/) if there are any issues or feedback."
    )

    st.header("Motivation")
    st.write(
        "The motivation behind the creation of this app is to help everyone to make informed decision "
        "when purchasing a real estate. Users can use the app to check the current estimated value of "
        "a real estate in a particular township, and also to forecast the future value of the real estate."
    )

    st.header("Data Used")
    st.write(
        "The app uses data scraped from Brickz.my, from January 2000 to June 2023. "
        "Meanwhile, the economic indicators are obtained from Department of Statistics Malaysia (DOSM) and Bank Negara Malaysia (BNM)."
    )

    st.header("Methodology")
    st.write(
        "The models in this app were built using Seasonal Auto-Regressive Integrated Moving Average (SARIMAX) "
        "and artificial neural network (ANN). Missing values in economic indicators were extrapolated using "
        "the Time-Weighted Extrapolation method by Nia (2017) in his working paper with United Nations titled "
        "'A weighted extrapolation method for measuring the SDGs progress'."
    )

    st.header("Disclaimers")
    st.write("By using the app, you acknowledge following disclaimers:")
    st.write("- The information provided by this app is for educational and demonstration purposes only.")
    st.write(
        "- The author makes no representations or warranties of any kind, express or implied, "
        "about the completeness, accuracy, reliability, suitability, or availability with respect "
        "to the app or the information contained in it for any purpose."
    )
    st.write(
        "- The author will not be liable for any losses or damages, including without limitation, "
        "indirect or consequential losses or damages, or any loss or damage arising from loss of data "
        "or profits arising out of, or in connection with, the use of this app."
    )
    st.write("- The user is solely responsible for any decisions made based on the information provided by this app.")
