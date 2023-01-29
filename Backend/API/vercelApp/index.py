from flask import Flask, request
from flask_cors import cross_origin, CORS
from views import getVideoTranscript, performSemanticSearch
app = Flask(__name__)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/', methods=['POST'])
@cross_origin()
def getTranscript():
    request_data = request.json
    video_id = request_data["video_id"]
    return getVideoTranscript(video_id)

@app.route('/semantic', methods=['POST'])
@cross_origin()
def result():
    # try:
        request_data = request.json
        dataset = request_data["text"]
        UserQuery = request_data["query"]
        transcript = request_data["transcript"]
        output = performSemanticSearch(dataset,UserQuery, transcript)
        return output

    # except Exception as e:
    #     return {"error" : str(e)}

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")