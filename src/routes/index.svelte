<svelte:head>
  <title>INFERNO - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
  <div class="banner-space">
    <img src="/images/image.svg" alt="bannerlogo" />
    <h1>kunnes Kadotus meidät korjaa</h1>
  </div>
  <div class="paral">
    <h2>Vuoden 2022<br /> Hybridi&shy;Speksi <br />on täällä!</h2>
    <p>Ensi-ilta 16.3. klo 19.00</p>
    <p>17.3. klo 19.00</p>
    <p>18.3. klo 19.00</p>
    <p>19.3. klo 14.00</p>
    <p>19.3. klo 19.00</p>
    <p>20.3. klo 14.00</p>
    <p>
      Lipunmyynnin löydät <a
        href="https://kide.app/community/d96376eb-02ff-4b1b-be75-a959f0fe0c42"
        >Kide.Appistä</a
      >
    </p>
  </div>
  <section class="dudes">
    <div>
      <img
        alt="dude100"
        class="dude left"
        src="/images/Hahmo2_200.png"
        style="top: 100vh"
      />
    </div>
    <div>
      <img
        alt="dude130"
        class="dude right"
        src="/images/Hahmo3_200.png"
        style="top: 130vh"
      />
    </div>
    <div>
      <img
        alt="dude160"
        class="dude left"
        src="/images/Hahmo1_200.png"
        style="top: 160vh"
      />
    </div>
    <div>
      <img
        alt="dude190"
        class="dude right"
        src="/images/Hahmo4_200.png"
        style="top: 190vh"
      />
    </div>
    <div>
      <img
        alt="dude220"
        class="dude"
        src="/images/Hahmo5_200.png"
        style="top: 220vh"
      />
    </div>
  </section>
  <div class="paral">
    <p>Ja jumaskekka trailerikin pamahti eetteeriin !?!?</p>
    <div class="video">
      <a
        href="https://www.youtube.com/watch?v=uOijMBuS_lQ"
        rel="noopener"
        target="_blank"
        class="video-container"
      >
        <img src="/images/teaser.jpg" alt="teaser" class="video-img" />
        <img src="/images/icon-youtube-red.svg" alt="youtube" class="yt-icon" />
      </a>
    </div>
  </div>
  <h1>Pääyhteistyö&shy;kumppani</h1>
  <div class="logos">
    <div class="logo">
      <a href="https://axelhealth.com">
        <img alt="axel" class="logo" src="/images/logos/axelhealth.png" />
      </a>
    </div>
  </div>
  <h1>Yhteistyö&shy;kumppanit</h1>
  <div class="logos">
    <div class="logo">
      <a href="https://tek.fi">
        <img alt="tek" src="/images/logos/tek.png" />
      </a>
    </div>
    <div class="logo sampsa">
      <a href="https://sampsavuorela.com">sampsavuorela.com</a>
    </div>
    <div class="logo">
      <a href="https://www.punanaamio.fi/">
        <img alt="punanaamio" src="/images/logos/punanaamio.png" />
      </a>
    </div>
    <div class="logo">
      <a href="https://www.iqvia.com/">
        <img src="/images/logos/iqvia.png" alt="iqvia" />
      </a>
    </div>
    <div class="logo">
      <a href="https://www.ailea.fi/">
        <img src="/images/logos/ailea.svg" alt="ailea logo" />
      </a>
    </div>
  </div>
</section>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-image: url('/images/Kerberos_1280.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-color: black !important;
    background-attachment: fixed;
    .paral {
      background-color: rgba(39, 20, 3, 0.4);
      width: 100%;
      display: flex;
      flex-direction: column;
      p {
        color: gold;
        font-size: 2rem;
      }
    }
    .banner-space {
      h1 {
        font-size: 5rem;
        @media only screen and (max-width: 767px) {
          font-size: 3rem;
        }
      }
      margin-top: 5rem;
      display: flex;
      flex-direction: column;
      width: 100%;
      max-width: 1043px;

      img {
        margin: 1rem;
      }
    }
    .video {
      margin: 10px auto;
      max-width: 95vw;
      display: flex;
      flex-direction: column;
      .video-container {
        position: relative;
        &:hover {
          .yt-icon {
            width: 17rem;
          }
        }
        .video-img {
          margin: 4rem;
          width: 55rem;
          max-width: 80vw;
          box-shadow: 0px 0px 15px rgba(39, 20, 3, 0.4);
          border-radius: 4px;
          transition: all 0.5s;
          @media only screen and (max-width: 767px) {
            margin: 4rem 0;
          }
        }
        .yt-icon {
          position: absolute;
          top: 50%;
          left: 50%;
          transition: all 0.3s;
          transform: translate(-50%, -50%);
          width: 15rem;
          max-width: 30vw;
        }
      }
    }
  }
  .dudes {
    height: 500px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;

    img {
      margin: 10px;
    }

    .dude {
      &.right {
        right: 5rem;
        transform: scaleX(-1);
      }
      &.left {
        left: 5rem;
      }
      height: 10rem;
    }
    @media only screen and (max-width: 767px) {
      display: none;
    }
  }
</style>
