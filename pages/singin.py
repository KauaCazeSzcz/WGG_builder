"""Access request page"""

import streamlit as st

def main():
    """Build page content"""

    st.set_page_config(
        "WGG Builder | Sing in",
        "📋",
        "centered",
        "collapsed"
    )

    st.markdown("""
        <h1 style='text-aling: center;'>📋 Sing In</h1>
    """, unsafe_allow_html=True)
    
    # form container
    left_col, center_col, right_col = st.columns([1,2,3])
    with center_col:
        with st.form("sing_in_form"):
            username = st.text_input("👤 Username", placeholder="Create your username...")
            password = st.text_input("🔒 Password", type="password", placeholder="Create a password...")
            confirm_password = st.text_input("✔️ Confirm password", type="password", placeholder="Confirm your password...")

            form_left, form_center, form_right = st.columns(3)

            with form_right:
                if st.form_submit_button(type="primary", use_container_width=True):
                    if not any((not username, not password, not confirm_password)):
                        st.error("Preencha todos os campos")
                        return
                    if not password == confirm_password:
                        st.error("A senha e a confirmação devem ser iguais")
                        return
                    send_access_request(username, password)

        if st.button("Login", type="tertiary"):
            st.navigation([st.Page("pages/login.py")])
            st.switch_page("pages/login.py")

def send_access_request(username: str, password: str):
    """"""

if __name__ == "__main__":
    main()