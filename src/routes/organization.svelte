<script>
  import segments from '../assets/yhdistys.json';
</script>

<svelte:head>
  <title>Yhdistys - HybridiSpeksit</title>
</svelte:head>

<section class="wrap">
  <div class="text">
    <h1>Yhdistys ja toimihenkilöt</h1>
    {#each segments as segment}
      <div class="segment">
        <h3>{segment.id}</h3>
        {#each segment.people as person}
          <div class="row">
            <p class="left">{person.title}:</p>
            <p class="right">{person.name}</p>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</section>

<style lang="scss">
  @use '../main.scss';

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
  }
</style>
