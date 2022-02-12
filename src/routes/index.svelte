<section class="wrap">
  <div class="banner-space">
    <img src="/images/image.svg" alt="bannerlogo" />
    <h1>kunnes Kadotus meidät korjaa</h1>
  </div>
  <h1>Vuoden 2022 HybridiSpeksi on täällä!</h1>
  <p>Ensi-ilta 16.3. klo 19.00</p>
  <p>17.3. klo 19.00</p>
  <p>18.3. klo 19.00</p>
  <p>19.3. klo 14.00</p>
  <p>19.3. klo 19.00</p>
  <p>20.3. klo 19.00</p>
  <p>Lipunmyynnin löydät <a href="https://www.kide.app">Kide.Appistä</a></p>
  <p>Ja jumaskekka trailerikin pamahti eetteeriin !?!?</p>
  <div class="trailer">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/uOijMBuS_lQ"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    />
  </div>
</section>
<section class="dudes">
  <img
    alt="dude100"
    class="dude left"
    src="/images/dude.png"
    style="top: 100vh"
  />
  <img
    alt="dude130"
    class="dude right"
    src="/images/dude.png"
    style="top: 130vh"
  />
  <img
    alt="dude150"
    class="dude left"
    src="/images/dude.png"
    style="top: 150vh"
  />
  <img
    alt="dude200"
    class="dude right"
    src="/images/dude.png"
    style="top: 200vh"
  />
</section>
<section class="wrap">
  <h1>Yhteistyössä</h1>
</section>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-image: url('/images/bkg.jpg');
    background-repeat: no-repeat;
    background-size: 100% auto;
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

    h1 {
      font-size: 4rem;
      text-align: center;
      color: gold;
      text-decoration: underline;
    }
    p {
      font-size: 2rem;
      text-align: center;
      color: gold;
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
        margin: 5rem;
      }
    }
    .trailer {
      margin: 10px auto;
    }
  }
  .dude {
    &.right {
      right: 5rem;
    }
    &.left {
      left: 5rem;
    }
    height: 7rem;
    display: block;
    position: absolute;
  }
</style>
