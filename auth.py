
import streamlit as st

def require_auth(func):
    """Decorator para requerer autenticação"""
    def wrapper(*args, **kwargs):
        # st.set_page_config() deve ser chamado primeiro na função decorada
        if not st.session_state.get("authenticated", False):
            st.switch_page("pages/login.py")
            return
        return func(*args, **kwargs)
    return wrapper