import streamlit as st


def publish(sql_object):
    st.subheader("Create an Account")
    new_user = st.text_input('Username')
    new_passwd = st.text_input('Password', type='password')
    if st.button('SignUp'):
        sql_object.create_users_table()
        sql_object.add_user_data(new_user, new_passwd)
        st.success("Congrats! You have successfully created an account.")
        st.info("Go to the Login menu on the left sidebar to login.")
        st.balloons()
