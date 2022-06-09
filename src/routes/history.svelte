<script> 
  import speksit from '../assets/speksit.json';
  import Image from '../components/Image.svelte';
  import Speksi from '../components/Speksi.svelte';
  import { scale } from 'svelte/transition';

  let year = 2019;
  
function openSpeksi(syear) {
    year = syear;
  }
</script>

<svelte:head>
  <title>Aikaisemmat HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
  <h1>Aikaisemmat HybridiSpeksit</h1>
  <div class="row">
    <div class="posters" id="spkesi">
      {#each speksit as speksi}
      {#if speksi?.year}
      <div class="poster" on:click="{() => openSpeksi(speksi.year)}" in:scale>
          <Image src="images/db/{speksi.year}/{speksi.poster}" alt=""  />
      </div>
      {/if}
      {/each}
    </div>
    <div class="speksi">
      {#each speksit as speksi}
        {#if (speksi.year == year)}
          <Speksi {speksi} />
        {/if}
      {/each}
    </div>
  </div>
</section>

<style lang="scss">
@use '../main.scss';
section.wrap {
    min-height: 85vh;
    .row {
        display: flex;
        flex-direction: row;
        padding: 0 2rem;
        .posters {
          display: flex;
          flex-wrap: wrap;
          justify-content: center;
          align-content: flex-start;
            .poster {
                display: flex;
                box-shadow: 5px 5px 15px 5px #000000;
                border-radius: 10px 10px 0 0;
                margin: 10px;
                height: 300px;
                > :global(img) {
                  border-radius: 10px 10px 0 0;
                }
            }
            .poster > :global(img:hover) {
                transform: scale(1.05);
                box-shadow: 5px 5px 15px 5px #000000;
            }
        }
        .speksi {
            width: 60%;
        }
    }
}
  
</style>