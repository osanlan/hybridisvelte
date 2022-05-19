<svelte:head>
  <title>Keikat - HybridiSpeksi</title>
</svelte:head>
<section class="wrap">
  <h1>Keikat</h1>
  <div class="text">
    <h2>Bändi&shy;keikat</h2>
    <p>
      Kuuluuko korvissasi vain tuulen huminaa? Kaipaatko musiikillista menoa
      tapahtumaasi? HybridiSpeksin bändi, eli HSBändi, soittaa menevää
      musiikkia Abbasta Zappaan. Voit pyytää bändiä soittamaan haluamaasi
      musiikkia, tai antaa heille vapaat kädet suunnitella tilaisuuteesi
      sopivaa musiikkia.
    </p>
    <p>
      Olemme soittaneet akateemisilla vuosijuhlilla kamarimusiikkia kuin myös
      yökerhoilla ja syntymäpäiväjuhlilla helposti tanssittavaa
      kevytmusiikkia. Jokainen orkesterin jäsen on päätoiminen opiskelija,
      joten saatavuus selvitetään joka tilauksen yhteydessä erikseen.
      Tilaamalla meidät tuet opiskelijakulttuuria ja me pääsemme tekemään sitä
      mitä rakastamme!
    </p>
    <p>
      Huomioithan tapahtuman järjestäjänä, että niin ääni- ja valotekniikka
      kuin osaava teknikko tulee olla hankittuna tapahtumapaikalle meistä
      riippumatta. Erikoistapauksessa voimme parhaamme mukaan järjestää
      paikalle äänitekniikkaa ja teknikon, mutta tämä vaatii yhteydenottoa
      hyvissä ajoin.
    </p>
    <p>
      Varaathan siis meidät ajoissa - toiveen mukaan vähintään kuukautta
      aeimmin - erityisesti mikäli haluat esittää erityistoiveta esitykseen
      liittyen. Nähdään lavalla!
    </p>
      <h3>Tiedustelut bändikeikoista:</h3>
      <a href="mailto:emerve@utu.fi">Elias Ervelä / emerve@utu.fi</a>
  

    <div class="images flex">
      <img onclick="openImage('band_modal_1', true)" alt="Bändikuva 1" class="keikat__images__item" src="images/gigs/band_1_thumb.jpg" />
      <img onclick="openImage('band_modal_2', true)" alt="Bändikuva 2" class="keikat__images__item" src="images/gigs/band_2_thumb.jpg" />

      <img onclick="openImage('band_modal_3', true)" alt="Bändikuva 3" class="keikat__images__item" src="images/gigs/band_3_thumb.jpg" />

      <div id="band_modal_1" class="modal fadeIn">
        <span class="modal__close"><span class="modal__close__icon">&nbsp;</span></span><img id="band_modal_1_img" src="images/gigs/band_1.jpg" class="modal__image" alt="Bändikuva 1" />
      </div>
      <div id="band_modal_2" class="modal fadeIn">
        <span class="modal__close"><span class="modal__close__icon">&nbsp;</span></span><img id="band_modal_2_img" src="images/gigs/band_2.jpg" class="modal__image" alt="Bändikuva 2" />
      </div>
      <div id="band_modal_3" class="modal fadeIn">
        <span class="modal__close"><span class="modal__close__icon">&nbsp;</span></span><img id="band_modal_3_img" src="images/gigs/band_3.jpg" class="modal__image" alt="Bändikuva 3" />
      </div>
    </div>
  </div>
  <div class="text">
    <h2>Esiintyjät</h2>
    <p>
      Kaipaako pikkujoulusi tai syntymäpäiväsi laadukasta ja persoonallista
      esiintyjää? HybridiSpeksin näyttelijäkaarti on käytettävissäsi
      esiintyjätarpeisiisi. Tarjoamme tapahtumiin paketteja aina muutaman
      hengen juontokeikoista ison porukan improvisaatioteatteriin asti. Luomme
      tapahtumaasi ohjelman tarpeesi mukaan.
    </p>
    <h3>
      Tiedustelut esiintyjäkeikoista:
    </h3>
    <a href="mailto:hallitus@hybridispeksi.fi"><span>hallitus@hybridispeksi.fi</span></a>
    <div class="images flex">
      <img onclick="openImage('actors_modal_1', true)" alt="Esiintyjät 1" class="keikat__images__item" src="images/gigs/actors_1_thumb.jpg" />

      <div id="actors_modal_1" class="modal fadeIn">
        <span class="modal__close"><span class="modal__close__icon">&nbsp;</span></span><img id="actors_modal_1_img" src="images/gigs/actors_1.jpg" class="modal__image" alt="Bändikuva 1" />
      </div>
    </div>
  </div>
</section>
<style lang="scss">
  @use '../main.scss';
  div {
    .images {
      
    }
    .modal {
      display: none;
    }
  }
  
</style>