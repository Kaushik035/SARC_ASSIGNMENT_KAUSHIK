import "./NationalPark.css"
import { AppState } from "../../App"
import { useContext } from "react"
import Title from "../Title"
import Container from "../Container"

export default function NationalPark(params) {
    const context = useContext(AppState)


    const {nationalpark} =context

    return <div ref={nationalpark} className="nationalpark">
        <div className="header2">
        <Title name ={"NATIONAL PARK"} classs={"parkT"}></Title>
        </div>
        <div className="page2">

        <Container
          clas={"kaziranga"}
          nclass={"nkaziranga"}
          pic={"imgkaziranga"}
          Name={"KAZIRANGA NATIONAL PARK"}
        ></Container>

        <Container
          clas={"manas"}
          nclass={"nmanas"}
          pic={"imgmanas"}
          Name={"MANAS NATIONAL PARK"}
        ></Container>

        <Container
          clas={"nameri"}
          nclass={"nnameri"}
          pic={"imgnameri"}
          Name={"NAMERI NATIONAL PARK"}
        ></Container>
        </div>

    </div>
}