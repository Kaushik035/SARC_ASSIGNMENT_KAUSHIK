import "./Temple.css"
import { AppState } from "../../App"
import { useContext } from "react"
import Title from "../Title"
import Container from "../Container"

export default function Temple() {

    const context = useContext(AppState)

const {temple} =context


    return <div ref={temple} className="temple">
        <div className="header3">
        <Title name ={"TEMPLES"} classs={"templeT"}></Title>
            
        </div>
        <div className="page3">

        <Container
          clas={"kamakhya"}
          nclass={"nkamakhya"}
          pic={"imgkamakhya"}
          Name={"KAMAKHYA TEMPLE"}
        ></Container>
        <Container
          clas={"basishta"}
          nclass={"nbasishta"}
          pic={"imgbasishta"}
          Name={"BASISTHA TEMPLE"}
        ></Container>

        <Container
          clas={"navagraha"}
          nclass={"nnavagraha"}
          pic={"imgnavagraha"}
          Name={"NAVAGRAHA TEMPLE"}
        ></Container>
        </div>

    </div>
}