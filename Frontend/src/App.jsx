import { useEffect } from "react";
import "./App.css";
import Hero from "./components/Hero/Hero";
import Navbar from "./components/Navbar/Navbar";
import Search from "./components/Search/Search";
import Team from "./components/Team/Team";
import AOS from "aos";
import "aos/dist/aos.css";
import Thanks from "./components/Thanks/Thanks";
function App() {
  useEffect(() => {
    AOS.init({
      duration: 800,
    });
  }, []);
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <Search />
      <Team />
      <Thanks />
    </div>
  );
}

export default App;
