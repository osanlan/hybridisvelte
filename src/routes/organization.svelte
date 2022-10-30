<script>
import data from '../assets/toimijat.json';
</script>

<svelte:head>
  <title>Yhdistys - HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
    <div class="text">
        <h1>Yhdistys ja toimihenkilöt</h1>
        <div class="segment">
            <h3>Yhteystiedot</h3>
            {#each data.yhteystiedot as row}
              <div class="row">
                <p class="left">{row.name}</p>
                <p class="right">{row.value}</p>
              </div>
            {/each}
        </div>
        <div class="segment">
            <h3>HybridiSpeksi ry hallitus</h3>
            {#each data.hallitus as person}
            <div class="row">
                <p class="left">{person.name}</p>
                <p class="right">{person.title}</p>
            </div>
            {/each}
        </div>
        <div class="segment">
          <h3>Yhdenvertaisuus- ja hyvinvointivastaavat</h3>
          <div class="column">
          {#each data.yhdenvertaiset as person}
            <p>{person.name}</p>
            <p>{person.name2}</p>
            <p>{person.info} <a href="{personalbar.link}">Linkki yhteydenottolomakkeeseen</a></p>
            {/each}
          </div>
        </div>
        <div class="segment">
            <h3>Toimihenkilot</h3>
            {#each data.toimihenkilot as row}
            <div class="row">
                <p class="left">{row.name}</p>
                <p class="right">{row.title}</p>
            </div>
            {/each}
        </div>
        <div class="segment">
            <h3>Tuotantotiimi 2023</h3>
            {#each data.tuottis as person}
            <div class="row">
                <p class="left">{person.name}</p>
                <p class="right">{person.title}</p>
            </div>
            {/each}
        </div>
  </div>
  <div id="rules" class="flex flex_column">
    <a href="../assets/HybridiSpeksi ry säännöt.pdf">Yhdistyksen säännöt</a>
    <a href="../assets/HybridiSpeksi ry rekisteriseloste.pdf">Rekisteriseloste</a>
    <a href="../assets/HybridiSpeksi ry merkkiohjesääntö.pdf">Merkkiohjesääntö</a>
  </div>
</section>

<style lang="scss">
  @use '../main.scss';

  #rules {
    margin-top: 50px;
    a {
      padding: 10px;
    }
  }
  .segment {
    display: flex;
    flex-direction: column;
  }
  .row {
    display: flex;
    flex-direction: row;
    max-width: 70vw;
    align-items: center;
  }
  .text {
    .left {
      width: 50vw;
      text-align: right;
      margin-right: 10px;
    }
    .right {
      text-align: left;
      width: 50vw;
      margin-left: 10px;
    }
    .center {
      text-align: center;
      margin-left:  auto;
      margin-right: auto;
    }
  }
</style>
