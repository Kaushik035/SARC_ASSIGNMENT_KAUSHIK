import Header from "../Header";
import FakeHeader from "./FakeHeader";
import styles from "./home.module.css";
import { AppState } from "../../App";
import { useContext } from "react";
import videoBg from "./video.mp4";

export default function Home() {
  const context = useContext(AppState);

  const { home } = context;

  return (
    <div ref={home} className={styles.home}>
      <header>
        <Header></Header>
      </header>

      <FakeHeader></FakeHeader>

      <video src={videoBg} autoPlay loop muted></video>

      <div className={styles.outer}>
        <div className={styles.page1}>
          <div className={styles.awesome}>AWESOME</div>
          <br />
          <div className={styles.assam}>ASSAM</div>
            <br />
          <div className={styles.tag}>
            Assam: The Gateway to Northeast Wonders
          </div>
        </div>
      </div>
    </div>
  );
}
