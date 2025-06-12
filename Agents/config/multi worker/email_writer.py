from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

email_writer_agent = Agent(
    name="writer Email",
    instructions="You are a skilled content rewriter. Rewrite any text to make it more engaging, original, and SEO-friendly.",
    model=model
)

async def email_written(user_input: str):
    return await Runner.run(email_writer_agent, user_input, run_config=config)

def run_email_writer_agent() -> str:
    st.title("✍ AI Email writer")

    user_input = st.text_area("Enter your email:")

    if "email_output" not in st.session_state:
        st.session_state.email_output = ""

    if st.button("press Enter"):
        if user_input:
            with st.spinner("write email..."):
                try:
                    response = asyncio.run(email_written(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(email_written(user_input))

                st.session_state.email_output = response.final_output
        else:
            st.warning("Please enter some emails.")

    if st.session_state.email_output:
        st.markdown("### ✨ write email")
        st.write(st.session_state.email_output)