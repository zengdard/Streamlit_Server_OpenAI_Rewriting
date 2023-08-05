import openai
import streamlit as st
import tweepy


# Votre clé d'API pour OpenAI
openai.api_key = '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'

consumer_key = 'AknQg4BbBgDnhJ8W8O6p8D7tS'
consumer_secret = 'AhjaPSZBmbGfaj4CmmFZjjwv4oypS7dmT2MNVGJfPBrL3h9dtg'
access_token = '1526862349944205313-pGiuUmUFoMhS04MFLRIbq3JKZq75w3'
access_token_secret = 'rwhiGeTpF16oWD59mD7nv4RVFnLrv3jXlT993elPqPSTc'


# Authentification OAuth1
#auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


# By default, only the ID and text fields of each Tweet will be returned
# Additional fields can be retrieved using the tweet_fields parameter
# Widget pour saisir l'ID du tweet
tweet_ids = st.text_input('Enter Tweet ID')

if tweet_ids:
    # Récupération des commentaires
    comments = client.get_tweet(tweet_ids, tweet_fields=["in_reply_to_user_id", "referenced_tweets", "context_annotations", "edit_history_tweet_ids"])

    # Création d'une liste de commentaires
    comments_list = comments.data
    print(comments_list)
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

