<script>
  import { add_styles } from 'svelte/internal';
import segments from '../assets/yhdistys.json';
import t from '../assets/toimijat.json';
</script>

<svelte:head>
  <title>Yhdistys - HybridiSpeksit</title>
</svelte:head>
hallitus
{#each t.hallitus as tt}
<p>{tt.who}</p>
{/each}
toimarit
{#each t.toimihenkilot as tt}
<p>{tt.kuka}</p>
{/each}
yhdenvertaiset
{#each t.yhdenvertaiset as tt}
<p>{tt.tyyppi}</p>
<p>{tt.tyyppi2}</p>
<p>{tt.info}</p>
{/each}
tuottis
{#each t.tuottis as tt}
<p>{tt.who}</p>
{/each}
<section class="wrap">
  <div class="text">
    <h1>Yhdistys ja toimihenkilöt</h1>
    {#each segments as segment}
      <div class="segment">
        <h3>{segment.tableName}</h3>
        {#if segment.id == 'yhdenvertaiset'}
          {#each segment.people as person }
            {#if person.link}
          <div class="row">
            <p class="center">Voit antaa meille palautetta yhdistyksen tai produktion toiminnasta, 
              ilmoittaa kokemastasi häirinnästä tai kertoa mistä vain mieltäsi painavasta asiasta: 
              <a href="{person.link}">linkki yhteydenottolomakkeeseen</a></p>
          </div>
            {:else}
          <div class="row">
            <p class="left">{person.title}</p>
            <p class="right">{person.name}</p>
          </div>
            {/if}
          {/each}
        {:else}
          {#each segment.people as person}
        <div class="row">
          <p class="left">{person.title}:</p>
          <p class="right">{person.name}</p>
        </div>
          {/each}
        {/if}
      </div>
    {/each}
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
