<svelte:head>
  <title>Rekry - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
    <div class="banner-text">
        <h1>HybridiSpeksin rekry on sulkeutunut syksyn osalta.</h1>
        <p>Jos sinulle jäi kysyttävää rekryyn tai yleisesti speksiin liittyen, ota yhteyttä tuottajiimme.</p>
        <!-- <p><a class="link" href="https://forms.gle/k5dy8NHvKFyyXNBEA">Rekrylomake</a> auki sunnuntai iltaan asti!</p><br><br> -->
      
    </div>
</section>
<style lang="scss">
    @use '../main.scss';
    .link {
        padding: 10px;
        border: brown 2px solid;
        border-radius: 50%;
    }
    .banner-text {
        max-width: 60vw;
        min-height: 80vh;
        @media only screen and (max-width: 767px) {
            max-width: 90vw;
        }
        strong {
            color: gold
        }
        a {
            color: gold!important;
            text-decoration: underline;
        }
    }
</style>  