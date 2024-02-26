import streamlit as st

# Helper function to translate text
def translate(text, lang):
    translations = {
        "Select your language": {"es": "Selecciona tu idioma"},
        "English": {"es": "Inglés"},
        "Spanish": {"es": "Español"},
        "Trading Strategy Recommendation Tool": {"es": "Herramienta de Recomendación de Estrategias de Trading"},
        "Answer the following questions based on your analysis to get a strategy recommendation:": {"es": "Responde las siguientes preguntas basadas en tu análisis para obtener una recomendación de estrategia:"},
        "Is the price above the Ichimoku Cloud?": {"es": "¿Está el precio por encima de la Nube Ichimoku?"},
        "Has the Tenkan-sen crossed above the Kijun-sen?": {"es": "¿Ha cruzado el Tenkan-sen por encima del Kijun-sen?"},
        "Is the current price above the future cloud?": {"es": "¿Está el precio actual por encima de la nube futura?"},
        "Has there been an increase in volume?": {"es": "¿Ha habido un aumento en el volumen?"},
        "Is the RSI above 50?": {"es": "¿El RSI está por encima de 50?"},
        "Is the price above the 30-SMA?": {"es": "¿Está el precio por encima de la SMA-30?"},
        "Recommendation": {"es": "Recomendación"},
        "Long": {"es": "Comprar"},
        "Short": {"es": "Vender"},
        "Wait": {"es": "Esperar"},
        "Yes": {"es": "Sí"},
        "No": {"es": "No"}
    }
    return translations.get(text, {}).get(lang, text)

# Streamlit app layout
def app():
    st.title(translate("Trading Strategy Recommendation Tool", "English"))

    # Language selection
    lang = st.sidebar.selectbox(translate("Select your language", "en"), ["English", "Spanish"])

    st.header(translate("Answer the following questions based on your analysis to get a strategy recommendation:", lang))

    # Questions for bullish signals
    bullish_questions = [
        "Is the price above the Ichimoku Cloud?",
        "Has the Tenkan-sen crossed above the Kijun-sen?",
        "Is the current price above the future cloud?",
        "Has there been an increase in volume?",
        "Is the RSI above 50?",
        "Is the price above the 30-SMA?"
    ]

    # Questions for bearish signals
    bearish_questions = [
        "Is the price below the Ichimoku Cloud?",
        "Has the Tenkan-sen crossed below the Kijun-sen?",
        "Is the current price below the future cloud?",
        "Has there been an increase in volume?",
        "Is the RSI below 50?",
        "Is the price below the 30-SMA?"
    ]

    bullish_responses = [st.radio(translate(question, lang), [translate("Yes", lang), translate("No", lang)], key=question) for question in bullish_questions]
    bearish_responses = [st.radio(translate(question, lang), [translate("Yes", lang), translate("No", lang)], key=question) for question in bearish_questions]

    # Analyze responses to determine the strategy
    if all(response == translate("Yes", lang) for response in bullish_responses):
        recommendation = translate("Long", lang)
    elif all(response == translate("Yes", lang) for response in bearish_responses):
        recommendation = translate("Short", lang)
    else:
        recommendation = translate("Wait", lang)

    st.subheader(translate("Recommendation", lang))
    st.write(recommendation)

if __name__ == "__main__":
    app()
