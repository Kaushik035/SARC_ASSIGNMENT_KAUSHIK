import "./WaterFall.css";
import { AppState } from "../../App";
import { useContext } from "react";
import Title from "../Title";
import Container from "../Container";

export default function WaterFall(params) {
  const context = useContext(AppState);

  const { waterfall } = context;

  return (
    <div ref={waterfall} className="waterfall">
      <div className="header1">
        <Title name={"WATERFALL"} classs={"waterT"}></Title>
      </div>
      <div className="page1">
        <Container
          clas={"bhelughat"}
          nclass={"nbhelughat"}
          pic={"imgbhelughat"}
          Name={"BHELUGHAT WATERFALL"}
        ></Container>

        <Container
          clas={"panimur"}
          nclass={"npanimur"}
          pic={"imgpanimur"}
          Name={"PANIMUR WATERFALL"}
        ></Container>

        <Container
          clas={"mainapi"}
          nclass={"nmainapi"}
          pic={"imgmainapi"}
          Name={"MAINAPI WATERFALL"}
        ></Container>
      </div>
    </div>
  );
}
