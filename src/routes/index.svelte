<svelte:head>
  <title>INFERNO - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
  <div class="banner-space">
    <img src="/images/image.svg" alt="bannerlogo" />
    <h1>kunnes Kadotus meidät korjaa</h1>
  </div>
  <div class="paral">
    <h2>Vuoden 2022 HybridiSpeksi on täällä!</h2>
    <p>Ensi-ilta 16.3. klo 19.00</p>
    <p>17.3. klo 19.00</p>
    <p>18.3. klo 19.00</p>
    <p>19.3. klo 14.00</p>
    <p>19.3. klo 19.00</p>
    <p>20.3. klo 19.00</p>
    <p>Lipunmyynnin löydät <a href="https://www.kide.app">Kide.Appistä</a></p>
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
    <div class="trailer">
      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/uOijMBuS_lQ"
        title="YouTube video player"
        frameborder="0"
        allowfullscreen
      />
    </div>
  </div>
  <h1>Yhteistyössä</h1>
  <p>Axel Health</p>
  <p>Loimu</p>
  <p>TEK</p>
</section>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-image: url('/images/Kerberos_1280.jpg');
    background-repeat: no-repeat;
    background-size: cover;

    // background-image: linear-gradient(
    //   to right,
    //   rgba(34, 34, 34, 0.9),
    //   rgba(90, 58, 43, 0.9),
    //   rgba(34, 34, 34, 0.9)
    // );
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: medieval;

    background-attachment: fixed;

    h1 {
      font-size: 4rem;
      text-align: center;
      color: rgb(255, 60, 0);
      text-decoration: underline;
      text-shadow: rgb(201, 155, 57) 2px 2px;
    }
    h2 {
      font-size: 3rem;
      text-align: center;
      color: rgb(201, 155, 57);
      text-shadow: red 2px 2px;
    }
    p {
      font-size: 2rem;
      text-align: center;
      color: gold;
    }
    .paral {
      background-color: rgba(39, 20, 3, 0.4);
      // background-blend-mode: darken;
      width: 100%;
      display: flex;
      flex-direction: column;
    }
    .empty {
      height: 500px;
    }
    .banner-space {
      h1 {
        font-size: 5rem;
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
    .trailer {
      margin: 10px auto;
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
