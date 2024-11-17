import google.generativeai as genai
import streamlit as st


genai.configure(api_key="WRITE YOUR API KEY HERE")



st.title("An AI Code Reviewer ")


user_prompt = st.text_area("Enter your Python code here...")


if st.button("Generate Code") == True:
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash',
                              system_instruction="""
                                                    Given a python code to review, analyze the submitted code and identify bugs, errors or areas of improvement.
                                                    Provide the Fixed code .
                                                    Explain the reasoning behind code corrections or suggestions.""")
  

    st.subheader("Code Review")
    st.write("Bug Report:")

    
    
    if user_prompt:
        response = model.generate_content(user_prompt)
            
        st.write(response.text)
        