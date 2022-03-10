<script>
  import song_dic from '../assets/songs.json';
  let song_keys = Object.keys(song_dic);
  let song_values = Object.values(song_dic);
  let song_entries = Object.entries(song_dic);
  
  let selectedSong = song_values[0];
  let selectedYear;
</script>

<svelte:head>
  <title>Biisit - HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
  <form>
    <select bind:value={selectedYear}>
      <option value="9999" selected="selected">Meidän speksi</option>
      <option value="2022">2022 Inferno</option>
      <option value="2021">2021 Inferno - the beginning</option>
      <option value="2020">2020 Avaruusristeily 2101</option>
      <option value="2019">2019 Viimeinen Lohikäärmeisku</option>
      <option value="2018">2018 Älä Ammu Ohi</option>
      <option value="2017">2017 Kruunun Kohtalo</option>
      <option value="2016">2016 Bratva Kontra</option>
      <option value="2015">2015 H.A.L.I.</option>
    </select>

    <select bind:value={selectedSong}>
      <option value="">Valitse biisi</option>
      {#each song_entries as [key, value]}
        {#if value.year === selectedYear}
        <option value="{value}">{value.title}</option>
        {/if}
      {/each}
    </select>
  </form>

  {#if selectedSong}
    <div class="song" id={selectedSong.id}>
      <div class="name">{selectedSong.title}</div>
      <div class="origin">{selectedSong.origin}</div>
      {#each selectedSong.lines as line}
        {#if (line.length < 1)}
        <div class="verse"></div>
        {/if}
        <p>{line}</p>
      {/each}
    </div>
  {/if}
</section>

<style lang="scss">
  .song {
    margin: 20px;
    .name {
      // margin: 10px;
      font-size: 2rem;
    }
    .speksi {
      margin: 10px;
      padding-left: 5px;
      font-size: 1.5rem;
    }
    .origin {
      margin: 10px;
      padding-left: 5px;
      font-size: 1.5rem;
      font-style: italic;
    }

    .verse {
      height: 10px;
    }
    p {
      margin: 4px;
    }
    // }
    display: flex;
    flex-direction: column;
  }
</style>
