from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

summary_generator = Agent(
    name="generate summary",
    instructions="You are a skilled content rewriter. Rewrite any text to make it more engaging, original, and SEO-friendly.",
    model=model
)

async def generate_summary(user_input: str):
    return await Runner.run(summary_generator, user_input, run_config=config)

def run_summary_generator() -> str:
    st.title("✍ AI summary generator")

    user_input = st.text_area("Enter your summary:")

    if "summary_output" not in st.session_state:
        st.session_state.summary_output = ""

    if st.button("press Enter"):
        if user_input:
            with st.spinner("write summary..."):
                try:
                    response = asyncio.run(generate_summary(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_summary(user_input))

                st.session_state.summary_output = response.final_output
        else:
            st.warning("Please enter summary.")

    if st.session_state.summary_output:
        st.markdown("### ✨ write summary")
        st.write(st.session_state.summary_output)
