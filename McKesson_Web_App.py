import streamlit as st
import pandas as pd
from utilities.sql import SQL
from contents.home import publish as publish_home
from contents.signup import publish as publish_signup
from contents.login import publish as publish_login
import sqlite3

st.set_page_config(layout="wide")


def main(sql_object, new_orders_df):
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


# with st.form(key="my_form"):
#     username = st.text_input("Username")
#     password = st.text_input("Password")
#     st.form_submit_button("Login")
#
# st.title("This is a Test")
#
# st.text_area("What is your costumer ID?")
#
# st.balloons()
#
# st.metric("My metric", 42, 2)
#
# CUST_ID = st.number_input("Pharmacy ID", 0, 99)
#
# ORDER_QTY = st.number_input("Order Quantity", 1)
#
# st.success("Thanks for submitting the order!")
#
# DATE = st.date_input("Today's Date")




