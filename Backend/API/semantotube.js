// import YoutubeTranscript from 'youtube-transcript';


var API_KEY = "17kcKXM7U1YHJcukH6xEoX7P5lKDvtJL8yD1QQ6D"

var URL = "http://bark.phon.ioc.ee/punctuator"


function get_sentence(full_transcript){

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

let xhr = new XMLHttpRequest();

xhr.open("POST", URL, true);

xhr.setRequestHeader("Accept", "application/json");

xhr.setRequestHeader("Content-Type", "application/json");

xhr.onreadystatechange = function () {
//   if (xhr.readyState === 4) {
    console.log(xhr.status);
    console.log(xhr.responseText);
//   }
};

  xhr.send(JSON.stringify({
    "text": full_transcript
}));



}




// function semantoTube(UserQuery, videoID){

//     dataset = []

//     transcript = YoutubeTranscript.fetchTranscript(videoID).then(console.log);

//     video_full_transcript = ""

//     for trans in transcript:
//         video_full_transcript += trans["text"]

//     if video_full_transcript.count(".") > 5:
//         video_full_trans_list = video_full_transcript.split(".")
//     else:
//         video_full_trans_list =  get_sentence(video_full_transcript)

//     print("transcript list",video_full_trans_list)


//     video_full_trans_length = len(video_full_trans_list)

//     print("Original Transcript Length:", video_full_trans_length)

//     if video_full_trans_length > 1000:

//         temp_list = []
        
//         temp_sentences = ""
        
//         no_of_sentences_to_join = math.ceil(video_full_trans_length/1000.0)

//         print("No of sentences to join:", no_of_sentences_to_join)
    
//         for sentence_counter in range(1, len(video_full_trans_list)):
        
//             temp_sentences += video_full_trans_list[sentence_counter] 
        
//             if sentence_counter%no_of_sentences_to_join == 0:
        
//                 temp_list.append(temp_sentences)
        
//             temp_sentences = ""
    
        
//         video_full_trans_list = temp_list
    
//     print("Modified Transcript Length:", len(video_full_trans_list))

//     dataset = {"text": video_full_trans_list}

    

//     co = cohere.Client(API_KEY)

//     df = pd.DataFrame(dataset)

//     embeds = co.embed(texts=list(df['text']), model="large", truncate="LEFT").embeddings

//     embeds = np.array(embeds)

//     search_index = AnnoyIndex(embeds.shape[1], 'angular')

//     for i in range(len(embeds)):
//         search_index.add_item(i, embeds[i])

//     search_index.build(10) # 10 trees

//     search_index.save('test.ann')


//     query_embed = co.embed(texts=[UserQuery],
//                     model="large",
//                     truncate="LEFT").embeddings

//     similar_item_ids = search_index.get_nns_by_vector(query_embed[0],10,
//                                                     include_distances=True)
//     results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'], 
//                                 'distance': similar_item_ids[1]})
//     print(results)
//     output = []
//     matched_strings = []
//     distances_dict = results.to_dict()["distance"]
//     for index in distances_dict:
//         if distances_dict[index] < 1.5:
//             matched_strings.append(dataset["text"][index])

//     for string in matched_strings:
//       for trans in transcript:
//         if trans["text"] in string:
//           output.append({'text': string, 'start': trans['start'], 'duration' : trans['duration'] })
//           break
//     print(output)
//     return {"output": output}

// }

get_sentence("This is fucking javascript Fuck you javascript This is heavy Javascript")