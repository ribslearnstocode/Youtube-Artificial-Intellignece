from youtube_transcript_api import YouTubeTranscriptApi
import math
import requests
import cohere
import pandas as pd
import numpy as np
from annoy import AnnoyIndex
import json


API_KEY = "17kcKXM7U1YHJcukH6xEoX7P5lKDvtJL8yD1QQ6D"
API_KEY_2 = "lAWsKemg9CfhrqvSSKrc98zLvH37tJtU3fDETubx"
URL = "http://bark.phon.ioc.ee/punctuator"
BASE_URL = "https://www.youtube.com/youtubei/v1/search"
VIDEO_BASE_URL = "https://youtu.be/"
EN_LANG_CODE_LIST = ['en','en-US', 'en-GB']

def get_sentence(full_transcript):

    body = {"text": full_transcript}
    response = requests.post(URL, data=body) 
    return response.text.split(".")

def getVideoTranscript(video_id):
    # try:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en'])
    except:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en-US'])

    video_full_transcript = ""

    for trans in transcript:
        video_full_transcript += trans["text"]

    if video_full_transcript.count(".") > 5:
        video_full_trans_list = video_full_transcript.split(".")
    else:
        video_full_trans_list =  get_sentence(video_full_transcript)

    video_full_trans_length = len(video_full_trans_list)

    # print("Original Transcript Length:", video_full_trans_length)

    if video_full_trans_length > 1000:

        temp_list = []
        
        temp_sentences = ""
        
        no_of_sentences_to_join = math.ceil(video_full_trans_length/1000.0)

    
        for sentence_counter in range(1, len(video_full_trans_list)):
        
            temp_sentences += video_full_trans_list[sentence_counter] 
        
            if sentence_counter%no_of_sentences_to_join == 0:
        
                temp_list.append(temp_sentences)
        
                temp_sentences = ""

          
    
        
        video_full_trans_list = temp_list

        # print("Modified Transcript Length:", len(video_full_trans_list))
    

    dataset = {"text": video_full_trans_list, "transcript" : transcript}

    return dataset 


def calculateHrMinSec(timeInSeconds):

    timeInMiliSec = int(timeInSeconds * 1000)
    timeInSec = int(timeInMiliSec/1000)
    timeInMin = int(timeInSec/60)
    timeInHr = int(timeInMin/60)
    #Updating Values
    timeInMin = int(timeInMin%60)
    timeInSec = int(timeInSec%60)
    timeInMiliSec = int(timeInMiliSec%1000)
    
    return {"Hr": timeInHr, "Min": timeInMin, "Sec": timeInSec, "Mili":timeInMiliSec}

def performSemanticSearch(dataset, UserQuery, transcript):
    dataset = {'text': dataset}

    df = pd.DataFrame(dataset)


    # print(dataset)
    try:
        co = cohere.Client(API_KEY)
        embeds = co.embed(texts=list(df['text']), model="large", truncate="LEFT").embeddings
    except:
        co = cohere.Client(API_KEY_2)
        embeds = co.embed(texts=list(df['text']), model="large", truncate="LEFT").embeddings

    embeds = np.array(embeds)

    search_index = AnnoyIndex(embeds.shape[1], 'angular')

    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])

    search_index.build(10) # 10 trees

    # search_index.save('test.ann')

    query_embed = co.embed(texts=[UserQuery],
                    model="large",
                    truncate="LEFT").embeddings

    similar_item_ids = search_index.get_nns_by_vector(query_embed[0],10,
                                                    include_distances=True)
    results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'], 
                                'distance': similar_item_ids[1]})


    relevant_strings_with_time_list = []
    most_relevant_strings = []
    distances_dict = results.to_dict()["distance"]

    for index in distances_dict:
        if distances_dict[index] < 1.1:
            most_relevant_strings.append(dataset["text"][index])

    # print(len(most_relevant_strings))
    # print(transcript)
    # print(most_relevant_strings)
    # print("No of matched strings:", len(most_relevant_strings))

    for string in most_relevant_strings:
        for trans in transcript:
            trans_text = trans["text"]
            is_trans_text_in_string_found = False

            for trans_text_partition in trans_text.split("."):
               if len(trans_text_partition) > 10 and ((trans_text_partition in string) or (trans_text_partition == string)):
                  
                  trans_start_time_in_sec = trans["start"]
                  timeDict = calculateHrMinSec(trans_start_time_in_sec)
                  
                  relevant_strings_with_time_list.append({'text': string, "start": trans_start_time_in_sec ,"Time":  timeDict})
                  is_trans_text_in_string_found = True
                  break
            if is_trans_text_in_string_found:
              break
  
    return relevant_strings_with_time_list


