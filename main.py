import openai
import streamlit as st


# Votre clé d'API pour OpenAI
openai.api_key = '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'

def rewrite_text_objectively(text):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Réécrivez ce texte de manière objective : \"{text}\"",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.write("Erreur lors de la réécriture:", str(e))
        return text

st.title("Réécriture de texte de manière objective")

# Entrée utilisateur
user_input = st.text_area("Entrez votre texte (max 200 mots) :")

# Vérifier la longueur du texte
word_count = len(user_input.split())

if word_count > 200:
    st.write(f"Votre texte contient {word_count} mots. Veuillez réduire votre texte à 200 mots ou moins.")
else:
    if st.button("Réécrire"):
        if user_input:
            rewritten_text = rewrite_text_objectively(user_input)
            st.subheader("Texte réécrit :")
            st.write(rewritten_text)
        else:
            st.write("Veuillez entrer un texte à réécrire.")
