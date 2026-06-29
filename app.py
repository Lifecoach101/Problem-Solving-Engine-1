import streamlit as st
from groq import Groq

st.title("Universal Problem Solver")
api_key = st.text_input("Enter Groq API Key", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        problem = st.text_area("Problem likho:")
        
        if st.button("Solve"):
            if not problem:
                st.warning("Please enter a problem first.")
            else:
system_prompt = "You are an expert Organizational Consultant. Follow these 4 steps: 1. Definition (A to B). 2. 5 Creative Solutions. 3. Best Selection. 4. 5-step Implementation. Respond in English."                
                with st.spinner("Solving..."):
                    # Naya model use kar rahe haan jo active hai
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": problem}],
                        model="llama-3.1-8b-instant", 
                    )
                    st.write(chat_completion.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
