<section class="wrap">
  <div class="banner-space" />
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
<section class="wrap">
  <h1>Yhteistyössä</h1>
</section>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-image: linear-gradient(
      to right,
      rgba(34, 34, 34, 0.9),
      rgba(90, 58, 43, 0.9),
      rgba(34, 34, 34, 0.9)
    );
    display: flex;
    flex-direction: column;
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
      margin-top: 5rem;
      display: block;
      min-height: 533px;
      // max-height: 100vw;
      width: 100%;
      background-image: url('/images/index.jpg');
      background-repeat: no-repeat;
      background-size: 100% 100%;
    }
    .trailer {
      margin: 10px auto;
    }
  }
</style>
