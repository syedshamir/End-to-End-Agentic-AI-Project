import streamlit as lt
import os
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() #config
        self.user_controls = {}
