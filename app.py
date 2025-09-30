"""Main page for the WebApp"""

import streamlit as st
from auth import require_auth

@require_auth
def main():
    """Build page content."""

    st.set_page_config(
        "WGG Builder | Home",
        "🏠",
        "wide",
        "expanded"
    )

    if not st.session_state.get("authenticated", False):
        st.switch_page("pages/login.py")
        return
    
    st.header("Bem-Vindo ao WWG Builder")
    st.subheader("Esse projeto é um builder automático do Weird Gun Game do roblox", divider=True)

    st.title("Sobre o WGG Builder:")
    st.divider()

    col1, col2, col3 = st.columns([1,2, 1])

    with col2:
        st.markdown("""
            <p>
                Teste de texto
            </p>
        """, True)

if __name__ == "__main__":
    main()