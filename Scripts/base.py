import cohere
import numpy as np
import re
import pandas as pd
# from tqdm import tqdm
from datasets import load_dataset
# import umap
import altair as alt
# from sklearn.metrics.pairwise import cosine_similarity
from annoy import AnnoyIndex
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)

API_KEY = "17kcKXM7U1YHJcukH6xEoX7P5lKDvtJL8yD1QQ6D"

co = cohere.Client(API_KEY)


def base(dataset, UserQuery):
    df = pd.DataFrame(dataset)

    embeds = co.embed(texts=list(df['text']), model="large", truncate="LEFT").embeddings

    embeds = np.array(embeds)

    print(embeds.shape)

    # Create the search index, pass the size of embedding
    search_index = AnnoyIndex(embeds.shape[1], 'angular')
    # Add all the vectors to the search index
    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])

    search_index.build(10) # 10 trees
    search_index.save('test.ann')

    # Get the query's embedding
    query_embed = co.embed(texts=[UserQuery],
                    model="large",
                    truncate="LEFT").embeddings

    # Retrieve the nearest neighbors
    similar_item_ids = search_index.get_nns_by_vector(query_embed[0],10,
                                                    include_distances=True)
    # Format the results
    results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'], 
                                'distance': similar_item_ids[1]})   
    return results

