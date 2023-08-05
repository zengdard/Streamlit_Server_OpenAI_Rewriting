import openai
import streamlit as st
import tweepy


# Votre clé d'API pour OpenAI
openai.api_key = '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'

consumer_key = 'AknQg4BbBgDnhJ8W8O6p8D7tS'
consumer_secret = 'AhjaPSZBmbGfaj4CmmFZjjwv4oypS7dmT2MNVGJfPBrL3h9dtg'
access_token = '1526862349944205313-pGiuUmUFoMhS04MFLRIbq3JKZq75w3'
access_token_secret = 'rwhiGeTpF16oWD59mD7nv4RVFnLrv3jXlT993elPqPSTc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This endpoint/method returns a variety of information about the Tweet(s)
# specified by the requested ID or list of IDs
name = st.text_input('name')
tweet_id = st.text_input('Enter Tweet ID')
if tweet_id and name :
    # Récupération des commentaires
    replies=[]
    for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent').items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    
    print(replies)
    comments_list = replies
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

