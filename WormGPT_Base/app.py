import streamlit as st
from database.auth_manager import AuthManager

# إعداد الصفحة
st.set_page_config(page_title="WORM-GPT", page_icon="💀")

# تهيئة نظام الدخول
auth = AuthManager()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# واجهة الدخول
if not st.session_state.authenticated:
    st.title("🧬 WORM-GPT ACCESS")
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Unlock"):
            tier = auth.verify_login(u, p)
            if tier:
                st.session_state.authenticated = True
                st.session_state.user_tier = tier
                st.rerun()
            else:
                st.error("Access Denied")
                
    with tab2:
        new_u = st.text_input("New User")
        new_p = st.text_input("New Pass", type="password")
        if st.button("Register"):
            if auth.register_user(new_u, new_p):
                st.success("Account Created!")
            else:
                st.error("Error creating account")

else:
    st.success(f"Welcome to WormGPT. Status: {st.session_state.user_tier}")
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()