import React from "react";
import { AiFillYoutube } from "react-icons/ai";
import "./navbar.css";
const Navbar = () => {
  return (
    <nav id="home">
      <h3>
        <AiFillYoutube /> Semanto<span>Tube</span>
      </h3>
      <ul>
        <li>
          <a href="#home">Home</a>
        </li>
        <li>
          <a href="#search">Search</a>
        </li>
        <li>
          <a href="#team">Team</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
