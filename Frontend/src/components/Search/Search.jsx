import React, { useEffect, useState, useRef } from "react";
import "./search.css";
import SEARCH_IMAGE from "../../assets/search.svg";
import axios from "axios";
import validateYouTubeUrl from "../../Scripts/YoutubeValidator";

const Search = () => {
  const [videoUrl, setVideoUrl] = useState("");
  const [query, setUserQuery] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [videoID, setVideoID] = useState("");
  const [progressStatus, setProgressStatus] = useState("");
  const [error, setError] = useState("");
  const errorRef = useRef();
  const [videoTranscript, setVideoTranscript] = useState({});
  const [semanticMatches, setSemanticMatches] = useState([]);
  const transRef = useRef();
  const [startTime, setStartTime] = useState(0);
  const videoRef = useRef();
  // const URL = "https://semantoapi.vercel.app";
  // const URL = "http://127.0.0.1:5000";
  const URL = "https://semantoapi.onrender.com"
  // const URL = "http://192.168.100.5:5000";
  const urlExamples = [
    "https://youtu.be/_uQrJ0TkZlc",
    "https://youtu.be/P7wUNMyK3Gs",
    "https://youtu.be/bz7yYu_w2HY"
  ]

  useEffect(() => {
    setIsLoading(false);
    setProgressStatus("");
    getVideoID();
  }, [videoUrl]);

  const setTheError = (error) => {
    setError(error);
    errorRef.current.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  };
  const getVideoID = () => {
    if (!videoUrl) {
      return;
    }
    if (videoUrl.includes("=")) {
      setVideoID(videoUrl.split("=")[1]);
      if (videoID.includes("&")) {
        setVideoID(videoID.split("&")[0]);
      }
    } else {
      setVideoID(videoUrl.split("/")[3]);
    }
  };

  const findBestVideo = async()=>{
    const response = await axios.post(
      `${URL}/generic`,
      {
        query,
      },
      {
        headers: {
          // Overwrite Axios's automatically set Content-Type
          "Content-Type": "application/json",
        },
      }
    );


  }
  const GetVideoTranscript = async (e) => {
    e.preventDefault();
    if (!validateYouTubeUrl(videoUrl)) {
      setTheError("Invalid URL");
      return;
    }
    try {
      setError("");
      setIsLoading(true);
      setProgressStatus("Getting Video Transcript...");
      const response = await axios.post(
        URL,
        {
          video_id: videoID,
        },
        {
          headers: {
            // Overwrite Axios's automatically set Content-Type
            "Content-Type": "application/json",
          },
        }
      );
      
      setVideoTranscript(response.data);
      await performSemanticSearch(response.data);
      setIsLoading(false);
      setProgressStatus("");

    } catch (error) {
      setTheError("Seems video or transcript doesn't exist");
      setIsLoading(false);
      setProgressStatus("");
    }
  };

  const performSemanticSearch = async (transData) => {
    try {
      setProgressStatus("Comparing best results...");
      const text = transData["text"];
      const transcript = transData["transcript"];
      const response = await axios.post(
        `${URL}/semantic`,
        {
          text,
          transcript,
          query,
        },
        {
          headers: {
            // Overwrite Axios's automatically set Content-Type
            "Content-Type": "application/json",
          },
        }
      );
      setSemanticMatches(response.data);
      setProgressStatus("");

      if(!response.data.length > 0){
        setTheError("No matching transcript found!")
        return
      }
      transRef.current.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });

    } catch (error) {
      setTheError(
        `Some server error occurred retry
        (Cohere free API provides limited api call per min)`
      );
      setProgressStatus("");
    }
  };
  const handleCardClick = (val) => {
    setStartTime(Math.ceil(val.start));
    videoRef.current.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  };
  return (
    <div className="section search__section" id="search" ref={errorRef}>
      <h2>Search</h2>
      <p>
        "Find exactly what you're looking for in YouTube videos with
        SemantoTube's advanced search."
      </p>
      <div className="searcher__portion">
        <div className="form__portion" data-aos="fade-right">
          <form onSubmit={GetVideoTranscript}>
          <p className="error">{error}</p>
                <input
                  type="text"
                  placeholder="Enter the url.."
                  value={videoUrl}
                  onChange={(e) => setVideoUrl(e.target.value)}
                  required
                />
                <div className="examples__container">
                  <span>e.g: </span>
                  {
                    urlExamples.map((val, ind) =>{ 
                      return(
                        <p key={ind} onClick={(e)=> setVideoUrl(e.target.innerHTML)}>{val}</p>
                      )}
                      )
                  }
                </div>
             
            <input
              type="text"
              placeholder="Enter query"
              value={query}
              onChange={(e) => setUserQuery(e.target.value)}
              required
            />
            <button
              className="btn btn__primary"
              disabled={(videoUrl && !isLoading)  ? false : true}
              type="submit"
            >
              {progressStatus ? progressStatus : "Search"}
            </button>
          </form>
        </div>
        <div className="player__portion" data-aos="fade-left">
          <img src={SEARCH_IMAGE} alt="" />
        </div>
      </div>
      <div className="video__container" ref={videoRef}>
        {/* <YouTube
           style={{ display : videoID && videoUrl ? "block" : "none" }} 
          videoId={videoID}
          ref={ytRef}
        />  */}
        {videoID && videoID ? <iframe
          id="player"
          className="youtube__iframe"
          height="500"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
          // src={`https://www.youtube.com/embed/${videoID}`}
          src={`https://www.youtube.com/embed/${videoID}?start=${startTime}`}
        ></iframe> : null}
      </div>
      <div className="transcripts__section" ref={transRef}>
        {semanticMatches.map((val, index) => {
          return (
            <div className="card trans" key={index}>
              <h3>
                {val.Time.Hr +
                  " Hr " +
                  val.Time.Min +
                  " Min " +
                  val.Time.Sec +
                  " Sec "}
              </h3>
              <p onClick={() => handleCardClick(val)}>
                {val.text.length > 300
                  ? val.text.slice(0, 300) + "...."
                  : val.text}
              </p>
            </div>
            
          );
        })}
      </div>
    </div>
  );
};

export default Search;
