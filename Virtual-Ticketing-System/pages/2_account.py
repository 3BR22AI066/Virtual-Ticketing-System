import streamlit as st

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Create a dictionary to store user data
user_data = {
    "Aaftab": {"password": "password1", "email": "aaftab@gmail.com"},
    "Sowmya": {"password": "password2", "email": "sowmya@gmail.com"},
    "Aish": {"password": "password3", "email": "aish@gmail.com"},
    "Rakshitha": {"password": "password4", "email": "rakshitha@gmail.com"}
}

# Create a signup form
def signup_form():
    new_username = st.text_input("New username")
    new_password = st.text_input("New password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")
    new_email = st.text_input("New email")
    if st.button("Sign up"):
        if new_password == confirm_password:
            # Check if the new username is already taken
            if new_username not in user_data:
                # Save the new user to the user_data dictionary
                user_data[new_username] = {"password": new_password, "email": new_email}
                st.success("Sign up successful")
                st.session_state.logged_in = True
                st.session_state.username = new_username
            else:
                st.error("Username already taken")
        else:
            st.error("Passwords do not match")

# Create a login form
def login_form():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check if the username and password are correct
        if username in user_data and user_data[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password")

# Create a sign out button
def signout():
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.session_state.username = None

# Display the forms and sign out button based on session state
tab1, tab2 = st.tabs(["Login", "Sign up"])
with tab1:
    if st.session_state.logged_in:
        st.write(f"Welcome, {st.session_state.username}!")
        signout()
    else:
        login_form()
with tab2:
    if st.session_state.logged_in:
        st.write("You are already logged in.")
    else:
        signup_form()