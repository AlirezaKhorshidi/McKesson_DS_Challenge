import streamlit as st
import pandas as pd
from models import ForecastEnsemble


def publish(sql_object, new_orders_df):
    st.subheader("Login Page")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.checkbox("Login"):
        sql_object.create_users_table()
        result = sql_object.login_user(username=username, password=password)
        if result:
            st.success(f"Logged In as {username}. Welcome!")
            tasks = ["Submit Order", "Prediction", "Profiles"]
            task = st.selectbox("Task", tasks)
            if task == "Submit Order":

                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<p class="big-font">Submit your order here:</p>',
                            unsafe_allow_html=True)

                CUST_ID = st.number_input("Pharmacy ID", 0, 99)
                ORDER_QTY = st.number_input("Order Quantity", 1)
                DATE = st.date_input("Today's Date")
                submit = st.button('Submit')
                if submit:
                    st.success("Thanks for submitting the order!")
                    st.snow()
                    new_orders_df = pd.concat([new_orders_df,
                                               pd.DataFrame([[DATE, CUST_ID, ORDER_QTY]],
                                                            columns=new_orders_df.columns)],
                                              ignore_index=True)

            elif task == "Prediction":

                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<p class="big-font">Fill out the pharmacy ID and drug price, the model will then predict the order quantity:</p>',
                            unsafe_allow_html=True)

                CUST_ID = st.number_input("Pharmacy ID", 0)
                PRICE_USD = st.number_input("Price", 0)
                ensemble_model = ForecastEnsemble(cust_id=CUST_ID)
                ORDER_QTY = ensemble_model.predict(price=PRICE_USD)
                if st.button('Predict'):
                    st.info(f"The model predicts {int(ORDER_QTY)} orders for Pharmacy ID {CUST_ID} at price point ${PRICE_USD}.")

            elif task == "Profiles":
                st.subheader("User Profiles")
                user_result = sql_object.view_all_users()
                df = pd.DataFrame(user_result, columns=["Username", "Password"])
                st.dataframe(df)
        else:
            st.warning("Incorrect Username/Password")
