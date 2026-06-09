import os
from google import genai
from google.genai.errors import ServerError, ClientError

def get_client(api_key_override=None):
    """Initializes the official Google GenAI client."""
    api_key = api_key_override or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

def ask_ai_chat(report_text, history, user_query, api_key=None):
    client = get_client(api_key)
    if not client:
        return "Please configure your Gemini API Key in the .env file."
        
    context = f"You are a helpful medical assistant AI. Here is the patient's parsed medical report context:\n{report_text}\n\n"
    
    history_context = ""
    for speaker, msg in history[-5:]:
        history_context += f"{speaker}: {msg}\n"
        
    prompt = f"{context}{history_context}Patient asks: {user_query}\nProvide a clear, patient-friendly response. Always append a disclaimer advising professional medical consultation."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except ServerError as e:
        if "503" in str(e) or "high demand" in str(e).lower():
            return "⚠️ Gemini servers are currently busy under heavy load. Please wait a minute and resubmit your question."
        return f"⚠️ Google Server Error: {e.message}"
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

def predict_disease_risks(df_summary, api_key=None):
    client = get_client(api_key)
    if not client:
        return "API Key missing. Unable to run AI risk assessment profiles."
        
    metrics_str = df_summary.to_string(index=False)
    prompt = f"Based on the following extracted lab parameters, flag potential metabolic or systematic disease risks (e.g., Diabetes, Cardiovascular disease, Anemia, Liver/Kidney distress) and suggest actionable preventative lifestyle modifications:\n\n{metrics_str}\n\nProvide clear bullet points with risk labels."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except ServerError as e:
        if "503" in str(e) or "high demand" in str(e).lower():
            return "⚠️ The risk prediction model is currently experiencing high demand. Please refresh or try again in a few moments."
        return f"⚠️ Google Server Error: {e.message}"
    except Exception as e:
        return f"⚠️ Could not generate risk predictions: {str(e)}"

def translate_content(text, target_lang, api_key=None):
    if target_lang == "English" or "⚠️" in text:
        return text
    client = get_client(api_key)
    if not client:
        return text
        
    prompt = f"Translate the following medical analysis text into {target_lang}. Keep formatting, markdown layout markers, and clinical labels identical, only translating descriptive text terms:\n\n{text}"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception:
        # If translation fails due to 503, return original English text so the app doesn't break
        return text