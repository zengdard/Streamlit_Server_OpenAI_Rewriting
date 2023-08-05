import openai
import streamlit as st
import tweepy


# Votre clé d'API pour OpenAI
openai.api_key = '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'

consumer_key = 'oM33jzwGriVxgRTHnI1MKRGof'
consumer_secret='srVBaeZ3zRN3lfhecAQBVVzzVhoNJyRW8SfloskHN242MoJutk'

access_token='1538514143816425472-aizUWwWArAtu7lUGFCUw2YwXItQn5N'
access_token_secret='iZz6zqknZtHPt49bSkBYhn2VO7MqRzcOdEhu7zw11B3jH'

# Authentification à Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Widget pour saisir l'ID du tweet
tweet_id = st.text_input('Enter Tweet ID')

if tweet_id:
    # Récupération des commentaires
    comments = api.search(q=f'to:{tweet_id}', result_type='recent', count=100)

    # Création d'une liste de commentaires
    comments_list = [comment.text for comment in comments]

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

