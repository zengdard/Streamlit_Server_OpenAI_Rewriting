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

bearer_token = "AAAAAAAAAAAAAAAAAAAAAHTrcgEAAAAAkH71IoBq0AvFAjotzMXCnF9rfkU%3D5sEedVO5KhjsjBWLJR1YSFnOBZroXCScuBGOvn7YxjrwwCM2TB"

clients = tweepy.Client(bearer_token)

# By default, only the ID and text fields of each Tweet will be returned
# Additional fields can be retrieved using the tweet_fields parameter
# Widget pour saisir l'ID du tweet
tweet_ids = st.text_input('Enter Tweet ID')
name = st.text_input('Enter Tweet Name')
if tweet_ids and name :
        
    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    # Récupération des commentaires
    #comments = api.get_tweets(tweet_ids, tweet_fields=["in_reply_to_user_id", "referenced_tweets", "context_annotations", "edit_history_tweet_ids"])

    # Création d'une liste de commentaires
    
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

