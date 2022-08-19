<svelte:head>
  <title>INFERNO - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
  <div class="paral">
    <div class="banner-text">
      <h1>HybridiSpeksin rekry aukeaa taas pian!</h1>
      <p>Hae mukaan tekemään yhtä Turun suurimmista spekseistä!</p>
      <p>HybridiSpeksin rekrytilaisuus on <strong>ke 14.09.2022 klo 17 Quantumin auditoriossa</strong>, nähdään siellä!</p>
      <p>Lisätietoja <a href="./rekry">täältä</a></p>
    </div>
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
    <p>Infernon trailerin pääset tsiigailemaan tästä!</p>
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
  <h1>2022 Infernon Pääyhteistyö&shy;kumppani</h1>
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
    .banner-text {
      max-width: 60vw;
      @media only screen and (max-width: 767px) {
          max-width: 90vw;
        }
    }
    .paral {
      background-color: rgba(39, 20, 3, 0.4);
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      p {
        color: gold;
        font-size: 2rem;
        a {
          color: gold;
          text-decoration: underline;
        }
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
