import streamlit as st

def main():
    # Set the title of the website
    st.title("My First Python Website with Streamlit")
    
    # Add a header
    st.header("Welcome to My Web App!")
    st.subheader("This website was built with Streamlit in just 15 minutes!")

    # Display an image (Streamlit's logo in this case)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", 
             caption="Streamlit Logo", 
             use_container_width=True)  # Updated parameter

    # User Input: Asking for the user's name
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}! Welcome to my website. 👋")

    # Add a button and show more information
    if st.button("Learn More"):
        st.write("""
        **Streamlit** is an open-source app framework that allows you to quickly build 
        web applications for data science and machine learning projects.
        
        🚀 It's very user-friendly and requires minimal setup to get started!
        """)

    # Contact section
    st.header("📬 Contact Me")
    st.write("Feel free to reach out to me at: [faizaanum210@gmail.com](mailto:faizaanum210@gmail.com)")

if __name__ == "__main__":
    main()