import streamlit as st
import pickle
import os
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/tasks",
    "https://www.googleapis.com/auth/userinfo.email"
]

def login():
    flow = Flow.from_client_secrets_file(
        "client_secret.json",
        scopes=SCOPES,
        redirect_uri="http://localhost:8501"
    )
    auth_url, _ = flow.authorization_url(prompt="consent")
    st.markdown(f"[🔐 Iniciar sesión con Google]({auth_url})")

    code = st.experimental_get_query_params().get("code")
    if code:
        flow.fetch_token(code=code[0])
        creds = flow.credentials
        with open("token.pkl", "wb") as token:
            pickle.dump(creds, token)
        st.session_state["token"] = True
        st.experimental_rerun()

def get_user_email():
    if not os.path.exists("token.pkl"):
        return None
    with open("token.pkl", "rb") as token:
        creds = pickle.load(token)
    service = build("oauth2", "v2", credentials=creds)
    info = service.userinfo().get().execute()
    return info.get("email")
