import streamlit as st

# Set the title of the web app
st.title("Welcome to My Streamlit App")

# Add a text input box
user_input = st.text_input("Enter something:")

# Add a button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")

# Display an image (optional, if you have an image file)
# st.image("example.jpg", caption="Example Image")

# Add a sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("This is a simple sidebar!")

# Add a checkbox
tagline = st.checkbox("Show tagline")
if tagline:
    st.write("Streamlit makes app development easy!")
