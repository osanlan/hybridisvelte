<script>
  import data from '../assets/yhdistys.json';
</script>

<svelte:head>
  <title>Aikaisemmat HybridiSpeksit</title>
</svelte:head>

<main class="centered">
  <h1>Aikaisemamt</h1>
  <p>content</p>
  {#each data as item}
    <p>{item.id}</p>
  {/each}
</main>
