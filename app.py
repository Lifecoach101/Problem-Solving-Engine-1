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
                # Updated Master Prompt with Aggressive Growth Strategy
                system_prompt = """
                You are a World-Class Organizational Consultant. For every user problem, execute these 5 steps with precision:
                
                1. DEFINITION (Business Analyst Persona): Clearly define the 'Current State' vs 'Desired State'. Identify root causes.
                2. GENERATION (Innovation Strategist Persona): Provide 10 unconventional, out-of-the-box solutions using 'First Principles Thinking'.
                3. SELECTION (CEO/CTO Persona): Use the 'ICE Framework' (Impact, Confidence, Ease) to select the single best solution.
                4. IMPLEMENTATION (Operations Manager Persona): Provide 5 concrete, actionable steps with a KPI for each to measure success within 30 days.
                5. JUSTIFICATION (Management Consultant Persona): Provide an Executive Summary explaining the high ROI and risk mitigation.
                
                Be aggressive in your selection. Prioritize scalability over ease of implementation. Focus on 10x growth, not 10% growth.
                
                FORMAT: Use professional headings (###) and bullet points for each step. Respond in clear, professional English.
                """
                
                with st.spinner("Analyzing your problem with expert strategies..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": system_prompt}, 
                            {"role": "user", "content": problem}
                        ],
                        model="llama-3.1-8b-instant", 
                    )
                    st.markdown(chat_completion.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
