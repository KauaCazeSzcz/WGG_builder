"""Login page for users"""

import time, streamlit as st
import pages.singin as singin

st.markdown("""
<style>
    [data-testid="collapsedControl"]{
        display: none    
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Build page components"""

    st.set_page_config(
        "WGG builder | Login",
        "🔐",
        "centered",
        "collapsed"
    )

    # Title
    st.markdown("<h1 style='text-align: center;'>🔐 Login</h1>", unsafe_allow_html=True)

    # Form container
    left_col, center_col, right_col = st.columns([1,2,1])
    with center_col:
        with st.form("login_form"):
            username = st.text_input("👤 User", placeholder="Insert your username here...")
            password = st.text_input("🔒 Password", placeholder="Insert your password here..", type="password")

            form_col1, form_col2, form_col3 = st.columns([1,2,1])
            with form_col3:
                submit = st.form_submit_button("Enter", use_container_width=True, type="primary")

        if st.button("Sing in", type="tertiary"):
            st.navigation([st.Page("pages/singin.py")])
            st.switch_page("pages/singin.py")
        
    if submit:
        if any((not username, not password)):
            st.error("Preencha os campos para continuar")
            return
        st.success("Login Realizado!")
        st.session_state["authenticated"] = True
        time.sleep(1)
        st.switch_page("app.py")

if __name__ == "__main__":
    main()