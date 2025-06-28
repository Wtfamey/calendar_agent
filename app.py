# app.py
from agents import Agent, main_agent
from swarm import Swarm

import streamlit as st
import prompts

if __name__ == "__main__":
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    swarm = Swarm(
        agent=main_agent,
        title="Create A Google Calendar AI Agent!"
    )
    if swarm.session.state.messages:
        for message in swarm.session.state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    prompt = st.chat_input("Enter your prompt here!")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = swarm.run(
                agent=main_agent,
                messages=st.session_state.messages
            )
            st.session_state.messages.append({"role": "assistant", "content": response.messages[-1]["content"]})
            st.markdown(response.messages[-1]["content"])