from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

brainstormer_agent = Agent(
    name="writer your idea",
    instructions="You are a skilled content rewriter. Rewrite any text to make it more engaging, original, and SEO-friendly.",
    model=model
)

async def idea_brainstormer_agent(user_input: str):
    return await Runner.run(brainstormer_agent, user_input, run_config=config)

def run_brainstormer_agent() -> str:
    st.title("✍ AI ideas writer")

    user_input = st.text_area("Enter your ideas:")

    if "idea_output" not in st.session_state:
        st.session_state.idea_output = ""

    if st.button("press Enter"):
        if user_input:
            with st.spinner("write idea..."):
                try:
                    response = asyncio.run(idea_brainstormer_agent(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(idea_brainstormer_agent(user_input))

                st.session_state.idea_output = response.final_output
        else:
            st.warning("Please enter some ideas.")

    if st.session_state.idea_output:
        st.markdown("### ✨ write idea")
        st.write(st.session_state.idea_output)