import snscrape.modules.twitter as sntwitter
import openai
import streamlit as st

# Votre clé d'API pour OpenAI
openai.api_key = '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'

# Widget pour saisir l'ID du tweet
tweet_id = st.text_input('Enter Tweet ID')

if tweet_id:
    # Récupération des commentaires
    comments = list(sntwitter.TwitterSearchScraper(f'to:{tweet_id}').get_items())

    # Création d'une liste de commentaires
    comments_list = [comment.content for comment in comments]

    # Construction du prompt pour GPT-3.5
    prompt = "Given the following comments on a tweet, identify which ones provide valuable context and which ones are irrelevant:\n"
    for i, comment in enumerate(comments_list):
        prompt += f"{i+1}: {comment}\n"

    # Utilisation de GPT-3.5 pour analyser les commentaires
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    # Affichage de l'analyse
    st.write(f"Analysis: {response.choices[0].text.strip()}")
