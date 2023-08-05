import openai
import streamlit as st
import tweepy


# Votre clé d'API pour OpenAI
openai.api_key = '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'

bearer_token = "AAAAAAAAAAAAAAAAAAAAAHTrcgEAAAAAym3cZ0Rk0pjUFCoHJ7DFkwJsKt4%3DKTFUaNIeS8WLx86KtV0HMKphp4clrqifnzc3cmaDk14dI5gobE"

client = tweepy.Client(bearer_token)


# By default, only the ID and text fields of each Tweet will be returned
# Additional fields can be retrieved using the tweet_fields parameter
response = client.get_tweet(tweet_ids, tweet_fields=["comments"])
# Widget pour saisir l'ID du tweet
tweet_ids = st.text_input('Enter Tweet ID')

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

