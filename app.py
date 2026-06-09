import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# Load the environment variables from your .env file invisibly
load_dotenv()

from gtts import gTTS
from io import BytesIO
from streamlit_mic_recorder import speech_to_text

from utils.ocr import extract_text_from_pdf
from utils.parser import extract_parameters
from utils.analyzer import analyze
from utils.ai_engine import ask_ai_chat, predict_disease_risks, translate_content
from utils.pdf_generator import generate_medical_pdf

# Fetch API Key directly from background environment configuration
active_key = os.environ.get("GEMINI_API_KEY")

# Page Config
st.set_page_config(page_title="MediInsight AI Pro", page_icon="🩺", layout="wide")

# Sidebar Configuration (Cleaned up - No API Key input)
with st.sidebar:
    st.header("⚙️ Configuration Hub")
    selected_lang = st.selectbox("🌐 Multi-Language Support", ["English", "Spanish", "French", "Hindi", "German", "Arabic"])
    st.caption("Translates dashboards and analytical profiles instantly.")
    
    if not active_key:
        st.error("⚠️ GEMINI_API_KEY missing from your .env file! Please check your file setup.")
    else:
        st.success("🔒 API Connection Secure")

# Main Application UI
st.title("🩺 MediInsight AI Pro")
st.subheader("Smart Diagnostics & AI Medical Assistant Studio")

uploaded_file = st.file_uploader("Upload Medical Report (PDF)", type=["pdf"])

if uploaded_file:
    # Read text data once and persist via Streamlit session cache states
    if "raw_text" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
        st.session_state["raw_text"] = extract_text_from_pdf(uploaded_file)
        st.session_state["file_name"] = uploaded_file.name
        st.session_state["chat_history"] = []

    text_extracted = st.session_state["raw_text"]

    tab1, tab2, tab3 = st.tabs(["📊 Diagnostic Dashboard", "💬 AI Medical Explainer Chat", "📄 Raw Report Text"])

    with tab3:
        st.text_area("Extracted Text Stream", text_extracted, height=400)

    # Core Engine Processing
    parsed_data = extract_parameters(text_extracted)
    
    if len(parsed_data) == 0:
        st.warning("No standard parameters detected. Use the AI Explainer Chat tab directly to evaluate custom layouts.")
    else:
        df = pd.DataFrame(parsed_data)
        statuses = [analyze(r["Test"], r["Value"]) for _, r in df.iterrows()]
        
        def map_emoji(s):
            if "Normal" in s: return "🟢 Normal"
            if "Slightly" in s: return "🟡 Slightly Abnormal"
            if "Critical" in s: return "🔴 Critical"
            return "⚪ Unknown"
            
        df["Status"] = [map_emoji(s) for s in statuses]

        # --- TAB 1: DIAGNOSTICS & RISKS ---
        with tab1:
            st.subheader("🧪 Parameter Analysis Matrix")
            st.dataframe(df[["Test", "Value", "Status"]], use_container_width=True)

            # High-level counters
            c1, c2, c3 = st.columns(3)
            c1.metric("🟢 Normal", (df["Status"] == "🟢 Normal").sum())
            c2.metric("🟡 Slightly Abnormal", (df["Status"] == "🟡 Slightly Abnormal").sum())
            c3.metric("🔴 Critical Attention", (df["Status"] == "🔴 Critical").sum())

            # Risk Predictive Profiles
            st.subheader("🧬 Disease Risk Prediction & Preventative Insight")
            if active_key:
                with st.spinner("Analyzing physiological data arrays..."):
                    risk_assessment = predict_disease_risks(df, api_key=active_key)
                    translated_risks = translate_content(risk_assessment, selected_lang, api_key=active_key)
                    st.markdown(translated_risks)
            else:
                st.info("Provide a Gemini API Key in your .env file to generate Disease Risk Predictions.")
                translated_risks = "No risk prediction data generated."

            # Report Export Engine Layout
            st.subheader("📥 Export Professional Patient Assessment")
            pdf_data = generate_medical_pdf(df, translated_risks)
            st.download_button(
                label="📥 Download Assessment Report as PDF",
                data=pdf_data,
                file_name="Patient_Analysis_Report.pdf",
                mime="application/pdf"
            )

        # --- TAB 2: COGNITIVE CHAT AND AUDIO COMPONENT ---
        with tab2:
            st.subheader("💬 Interactive Lab Explainer Chat")
            st.write("Ask questions like: *'What does high WBC mean?'* or *'Why is my hemoglobin low?'*")

            # Chat UI elements wrapper
            for side, msg in st.session_state["chat_history"]:
                with st.chat_message("user" if side == "Patient" else "assistant"):
                    st.write(msg)

            # Audio Input Assistant Component
            st.write("🎙️ **Voice Assistant Input:**")
            voice_input = speech_to_text(start_prompt="Click to Speak Question", stop_prompt="Stop Recording", just_once=True, key='voice_capture')
            
            # Standard Text Box Input Combo
            text_query = st.chat_input("Type your lab question here...")
            
            final_query = text_query if text_query else voice_input

            if final_query:
                with st.chat_message("user"):
                    st.write(final_query)
                st.session_state["chat_history"].append(("Patient", final_query))
                
                with st.spinner("Consulting medical knowledge bases..."):
                    ai_reply = ask_ai_chat(text_extracted, st.session_state["chat_history"], final_query, api_key=active_key)
                    localized_reply = translate_content(ai_reply, selected_lang, api_key=active_key)
                
                with st.chat_message("assistant"):
                    st.write(localized_reply)
                    
                    # Synthesize Audio Response Playback
                    try:
                        tts = gTTS(text=localized_reply[:300], lang='en', slow=False) # Limit reading to avoid timeouts
                        audio_fp = BytesIO()
                        tts.write_to_fp(audio_fp)
                        st.audio(audio_fp, format='audio/mp3')
                    except Exception:
                        pass # Gracefully handle alternative language engine limits
                        
                st.session_state["chat_history"].append(("MediInsight AI", localized_reply))