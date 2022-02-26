<script>
  import songs from '../assets/songs.json';
</script>

<svelte:head>
  <title>Biisit - HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
  {#each songs as song}
    <div>{song.name}</div>
    {#each song.verses as verse}
      <div>{verse}</div>
    {/each}
  {/each}
</section>
