import streamlit as st
import pandas as pd
from utilities.sql import SQL
from contents.home import publish as publish_home
from contents.signup import publish as publish_signup
from contents.login import publish as publish_login
import sqlite3

st.set_page_config(layout="wide")


def main(sql_object, new_orders_df):
    """
    This is the main function which publishes the app.

    Parameters
    ----------
    sql_object: utilities.sql.SQL object.
        This class is used for generating the sql database and committing/fetching values to/from it.

    new_orders_df: Pandas dataframe.
        Pandas dataframe which will collect new orders.

    """

    st.title("McKesson Web App")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        publish_home()
    elif choice == "Login":
        publish_login(sql_object, new_orders_df)
    elif choice == "SignUp":
        publish_signup(sql_object)


if __name__ == "__main__":
    conn = sqlite3.connect(database="username_password.db")
    sql_object = SQL(sql_connection=conn)
    new_orders_df = pd.DataFrame(columns=["DATE", "CUST_ID", "ORDR_QTY"])
    main(sql_object=sql_object, new_orders_df=new_orders_df)
