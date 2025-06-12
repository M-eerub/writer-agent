# import asyncio 
# from config.sdk_client import model, config
# from agents import Agent, Runner
# import streamlit as st        

# # Define the agent
# content_writer_agent = Agent(
#     name="Content Writer",
#     instructions="You are the best content writer in the world.",
#     model=model 
# )

# # Async function to generate content using the agent
# async def generate_writer_agent(prompt):
#     return await Runner.run(generate_writer_agent(prompt))

# # Main function to run in Streamlit
# def run_content_writer_agent():
#     st.title("Content Agent")    

#     user_input = st.text_input("Enter topic for generating content")

#     # Initialize session state
#     if "Blog_response" not in st.session_state:
#         st.session_state."Blog_response" = ""

#     # Button action
#     if st.button("Generate content"):
#         if user_input:
#             with st.spinner("Generating content..."):
#                 try:
#                     response = asyncio.run(_writer_agent(user_input))
#                 except RuntimeError:
#                     # Handle case where there's already a running event loop (common in Streamlit)
#                     response = asyncio.new_event_loop().run_until_complete(Generate_writer_agent(user_input))
                
#                 st.session_state["Blog_response"] = response.final_output

#         else:
#             st.warning("Please enter a topic.")

#     # Show result
#     if st.session_state["Blog_response"]:
#         st.success("Content generated!")
#         st.markdown(st.session_state["Blog_response"])
from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

writer_agent = Agent(
    name="Content writer",
    instructions="You are a skilled content rewriter. Rewrite any text to make it more engaging, original, and SEO-friendly.",
    model=model
)

async def generate_written_content(user_input: str):
    return await Runner.run(writer_agent, user_input, run_config=config)

def run_content_writer() -> str:
    st.title("✍ AI Content Rewriter")

    user_input = st.text_area("Enter your written content here:")

    if "writer_output" not in st.session_state:
        st.session_state.writer_output = ""

    if st.button("write Content"):
        if user_input:
            with st.spinner("writing content..."):
                try:
                    response = asyncio.run(generate_written_content(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_written_content(user_input))

                st.session_state.writer_output = response.final_output
        else:
            st.warning("Please enter some content to rewrite.")

    if st.session_state.writer_output:
        st.markdown("### ✨ written Content")
        st.write(st.session_state.writer_output)