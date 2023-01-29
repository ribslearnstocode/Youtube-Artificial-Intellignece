import React from "react";
import { AiFillYoutube } from "react-icons/ai";
import AI_IMAGE from "../../assets/ai.png";
import "./hero.css";
const Hero = () => {
  return (
    <div className="section hero__section">
      <div className="text__container" data-aos="face-right">
        <h1>
          <AiFillYoutube /> Semanto<span>Tube</span>
        </h1>
        <p>
          "SemantoTube makes it easy to find the information you need in YouTube
          video transcripts, with advanced semantic search capabilities."
        </p>
        <div className="btn__container">
          <a href="#search">
            <button className="btn btn__primary">Get Started</button>
          </a>
          <a href="#about">
            <button className="btn">Learn more</button>
          </a>
        </div>
      </div>
      <div className="img__container" data-aos="fade-left">
        <img src={AI_IMAGE} alt="AI Image" />
      </div>
    </div>
  );
};

export default Hero;
