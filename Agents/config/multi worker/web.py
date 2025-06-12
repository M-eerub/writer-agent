# import streamlit as st
# from multi_worker.manager import Distributed_task  # Make sure function name matches

# st.title("Writer Agent Interface")

# # Initialize session state
# if "task" not in st.session_state:
#     st.session_state.task = None

# # UI logic
# if st.session_state.task is None:
#     task = st.text_input("Enter your task to call an agent")
    
#     if st.button("Run task and call agent"):
#         call = Distributed_task(task)
#         if call:
#             st.session_state.task = call
#         else:
#             st.warning("No suitable agent found for the task.")
# else:
#     st.success("Running the agent for your task...")
#     st.session_state.task()  # Run the stored task function

#     if st.button("Reset"):
#         st.session_state.task = None
    
#     st.write("Try tasks like: 'write email', 'generate summary', 'brainstorm ideas'")
