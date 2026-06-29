import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Apex Strategy Engine", page_icon="📈")
st.title("Apex Strategy Engine")

api_key = st.text_input("Enter Groq API Key", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        # Refined professional label
        problem = st.text_area("Define your strategic objective or business challenge:")
        
        if st.button("Generate Strategic Roadmap"):
            if not problem:
                st.warning("Please enter a business challenge first.")
            else:
                # Elite Strategy Prompt (McKinsey-level rigor, but brand-neutral)
                system_prompt = """
                You are an Elite Global Strategy Consultant. Your goal is to provide high-level, board-room ready strategic advice. 
                Apply the following rigor to every user problem:

                1. THE PYRAMID PRINCIPLE: Start immediately with the Executive Summary/Recommendation. Focus on the answer first.
                2. MECE FRAMEWORK: Ensure all analyses are Mutually Exclusive and Collectively Exhaustive. Eliminate logical gaps.
                3. FIRST PRINCIPLES & ECONOMIC LOGIC: Challenge all underlying assumptions. Use Economic theory (Marginal Analysis, Opportunity Cost, ROI) to validate your solutions.
                4. AGGRESSIVE SCALING: Prioritize strategies that offer 10x growth and structural competitive advantages. Avoid incremental advice.
                5. RIGOROUS EXECUTION: Provide a 30-day "Critical Path" with quantifiable KPIs that track success.

                STRUCTURE: Use bold headings (###), professional tables where appropriate, and bullet points. Use clear, concise, and analytical language.
                """
                
                with st.spinner("Synthesizing strategic roadmap..."):
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
