<script> 
  import speksit from '../assets/speksit.json';
  import Image from '../components/Image.svelte';
  import Speksi from '../components/Speksi.svelte';
  import jQuery from 'jquery';

  let year;
  let open = false;

  function openSpeksi(syear) {
    year = syear;  
    if (!open) {
      jQuery(".speksit-poster").css('height', '100px');
      open = true;
    } else {

    }

  }
</script>

<svelte:head>
  <title>Aikaisemmat HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
  <h1>Aikaisemmat HybridiSpeksit</h1>
  <div class="speksit-container" id="spkesi">
    {#each speksit as speksi}
    <!-- <a href="#speksi"> -->
      <div class="speksit-poster" on:click="{() => openSpeksi(speksi.year)}">
        <Image src="images/db/{speksi.year}/{speksi.poster}" alt=""  />
      </div>
    <!-- </a> -->
    {/each}
  </div>
  <div id="speksit">
    {#each speksit as speksi}
      {#if (speksi.year == year)}
        <Speksi {speksi} />
      {/if}
    {/each}
  </div>
</section>

<style lang="scss">
  @use '../main.scss';
  section.wrap {
    justify-content: normal;
  }
  .speksit-container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .speksit-poster {
      display: flex;
      box-shadow: 5px 5px 15px 5px #000000;
      margin: 10px; 
    }
  }
  
</style>