<script>
import { onMount } from "svelte";

let time;
    onMount(async () => {
        time = Date.now();
    })  
</script>
<svelte:head>
  <title>Rekry - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
    <div class="banner-text">
        <h1>Hei sinä korkea&shy;koulu&shy;kulttuurista kiinnostunut!</h1>
        <p>Oletko aina halunnut kokeilla jotain uutta ja erilaista?</p>
        <p>Jos vastasit kyllä yllä mainittuun kysymykseen, niin me haluamme juuri SINUT mukaan tekemään HybridiSpeksiä 2023!</p>
        <p>Speksi on interaktiivista musiikkiteatteria, jonka tekeminen on äärimmäisen hauskaa ja palkitsevaa.</p>
        <p>HybridiSpeksi etsii jälleen monipuoliseen joukkoonsa tanssijoita, muusikoita, näyttelijöitä, maskeeraajia, puvustajia, ääniteknikoita ja vaikka mitä muuta!</p>
        <p>Tule rohkeasti mukaan tekemään yhtä Turun suurimmista spekseistä!</p>
        <p>HybridiSpeksin rekrytilaisuus on <strong>ke 14.09.2022 klo 17 Quantumin auditoriossa</strong>, nähdään siellä!</p>
        <p>Nähdään myös etänä <a href="https://utu.zoom.us/j/69656087568">zoomissa!</a></p>
        {#if time > 1663164000000}
        <p><a class="link" href="https://forms.gle/k5dy8NHvKFyyXNBEA">Rekrylomake</a></p><br><br>
        {/if}
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