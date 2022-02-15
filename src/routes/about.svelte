<svelte:head>
  <title>Mikä speksi? - HybridiSpeksi</title>
</svelte:head>
<main class="wrap">
  <div class="text">
    <h1>HybridiSpeksi</h1>
    <div class="logo">
      <img alt="logo" src="/images/android-chrome-512x512.png" />
    </div>
    <p>
      HybridiSpeksi on Turun yliopiston luonnontieteiden ja tekniikan
      opiskelijoiden vuosittain toteuttama teatteriproduktio. Ensimmäinen
      HybridiSpeksi nähtiin keväällä 2015 Barker-teatterilla.
    </p>
    <h2>2022 - Jo seitsemäs HybridiSpeksi</h2>
    <p>
      Koronavuosien takaiskujen myötä HybridiSpeksi nähdään taas lavalla
      keväällä 2022! Infernaaliseen seikkailutunnelmaan päästään, kun
      HybridiSpeksin näytökset valtaavat speksiscenen jo seitsemmättä kertaa
      Turun historiassa. HybridiSpeksi 2022 tuotanto- ja käsikirjoitustiimit
      valittiin jo kaudelle 2021 ja työt onkin aloitettu jo viime vuonna.
      Muutama tuotantotiimin paikka on kuitenkin vielä auki, joten pysy
      kuulolla!
    </p>
  </div>
  <div class="text">
    <h2>Mikä on speksi?</h2>
    <p>
      Koronavuosien takaiskujen myötä HybridiSpeksi nähdään taas lavalla
      keväällä 2022! Infernaaliseen seikkailutunnelmaan päästään, kun
      HybridiSpeksin näytökset valtaavat speksiscenen jo seitsemmättä kertaa
      Turun historiassa. HybridiSpeksi 2022 tuotanto- ja käsikirjoitustiimit
      valittiin jo kaudelle 2021 ja työt onkin aloitettu jo viime vuonna.
      Muutama tuotantotiimin paikka on kuitenkin vielä auki, joten pysy
      kuulolla!
    </p>
  </div>
  <div class="text">
    <h2>Muut turun speksit</h2>
    <p>
      Koronavuosien takaiskujen myötä HybridiSpeksi nähdään taas lavalla
      keväällä 2022! Infernaaliseen seikkailutunnelmaan päästään, kun
      HybridiSpeksin näytökset valtaavat speksiscenen jo seitsemmättä kertaa
      Turun historiassa. HybridiSpeksi 2022 tuotanto- ja käsikirjoitustiimit
      valittiin jo kaudelle 2021 ja työt onkin aloitettu jo viime vuonna.
      Muutama tuotantotiimin paikka on kuitenkin vielä auki, joten pysy
      kuulolla!
    </p>
  </div>
</main>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-color: rgba(90, 47, 10, 0.692);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: medieval;
    margin: auto;
    background-attachment: fixed;
    .text {
      padding-top: 4rem;
      max-width: 60vw;
    }
  }
  .logo {
    margin: auto;
    display: flex;
    flex-direction: column;
  }
  img {
    // width: 90vw;
    margin: auto;
  }
  h2 {
    text-transform: uppercase;
    font-size: 2.5rem;
  }
  @media only screen and (max-width: 767px) {
    p {
      font-size: 1.5rem;
    }
    h1 {
      font-size: 3.7rem;
    }
    .wrap {
      .text {
        max-width: 95vw;
      }
    }
    img {
      width: 90vw;
    }
  }
</style>
