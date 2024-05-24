import "./element.css";
import { useContext } from "react";
import { AppState } from "../App";
import img from "./images/assampng.png";

export default function Element({ name, logo, clas }) {
  const context = useContext(AppState);

  const {
    home,
    temple,
    nationalpark,
    waterfall,
    scrollToSectionHome,
    scrollToSectionTemple,
    scrollToSectionPark,
    scrollToSectionWater,
  } = context;



  return (
    <>
      <li onClick={() => scrollToSectionHome({ home })} className={"logoo"}>
        <span>A</span>A 
      </li>
      <li onClick={() => scrollToSectionHome({ home })} className={"home"} >
        Home
      </li>
      <li
        onClick={() => scrollToSectionWater({ waterfall })}
        className={"water"}
      >
        Waterfall
      </li>
      <li
        onClick={() => scrollToSectionPark({ nationalpark })}
        className={"park"}
      >
        National Park
      </li>
      <li
        onClick={() => scrollToSectionTemple({ temple })}
        className={"temple"}
      >
        Temples
      </li>
    </>
  );
}
