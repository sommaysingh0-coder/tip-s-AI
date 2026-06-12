import streamlit as st

st.title("I AM SOMMAY and this is my first AI project")
st.text("If you want to try the AI, press the button below.")
if st.button("Try AI"):
   
    st.text("for running the code, make sure you have installed python ")
    st.text("open terminal and run the command: python ")
    st.text("its looks like this :-")
    st.image("Screenshot_2026-06-12_19-31-48.png")
    st.text("if it's not look like this means your python was not installed .")
    st.text("second step is enter this command in terminal:-")
    st.image("Screenshot_2026-06-12_19-49-38.png")
    st.text("the last step is emter this command in terminal:-")
    with st.expander("Show Code"):
      with open("tips.py", "r") as f:
         content = f.read()
         st.code(content, language="python")