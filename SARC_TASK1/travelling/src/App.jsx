import { useState } from "react";
import { useRef } from "react";
import Home from "./components/home/Home";
import "./app.css";
import Temple from "./components/temple/Temple";
import NationalPark from "./components/nationalPark/NationalPark";
import WaterFall from "./components/waterFall/WaterFall";
import React from "react";

export const AppState = React.createContext();

function App() {
  const home = useRef();
  const temple = useRef();
  const nationalpark = useRef();
  const waterfall = useRef();

  const scrollToSectionHome = (elementRef) => {
    console.log(elementRef);
    window.scrollTo({
      top: elementRef.home.current.offsetTop,
      behavior: "smooth",
    });
  };

  const scrollToSectionTemple = (elementRef) => {
    console.log(elementRef);
    window.scrollTo({
      top: elementRef.temple.current.offsetTop,
      behavior: "smooth",
    });
  };
  const scrollToSectionPark = (elementRef) => {
    console.log(elementRef);
    window.scrollTo({
      top: elementRef.nationalpark.current.offsetTop,
      behavior: "smooth",
    });
  };
  const scrollToSectionWater = (elementRef) => {
    console.log(elementRef);
    window.scrollTo({
      top: elementRef.waterfall.current.offsetTop,
      behavior: "smooth",
    });
  };

  return (
    <div className="App">
      <AppState.Provider
        value={{
          home,
          temple,
          nationalpark,
          waterfall,
          scrollToSectionHome,
          scrollToSectionTemple,
          scrollToSectionPark,
          scrollToSectionWater

        }}
      >
        <Home></Home>
        <WaterFall></WaterFall>
        <NationalPark></NationalPark>
        <Temple></Temple>
      </AppState.Provider>
    </div>
  );
}

export default App;
