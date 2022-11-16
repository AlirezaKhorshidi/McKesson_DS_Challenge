import streamlit as st


def publish():
    """
    Publish text in the home page.

    """
    st.subheader("Home Page")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Welcome to the web app for McKesson data challenge.</p>',
                unsafe_allow_html=True)
    st.markdown('<p class="big-font">You can use this app to submit orders and predict order quantity.</p>',
                unsafe_allow_html=True)
    st.markdown('<p class="big-font">If you have an account you can login, if not you should signup from the left sidebar before logging in.</p>',
                unsafe_allow_html=True)
