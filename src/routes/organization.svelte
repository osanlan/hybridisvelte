<script>
  import data from '../assets/yhdistys.json';
</script>

<svelte:head>
  <title>Yhdistys - HybridiSpeksit</title>
</svelte:head>

<main class="centered">
  <div class="wrap">
    <div class="text">
      <h1>Yhdistys ja toimihenkilöt</h1>
      {#each data as item}
        <h3>{item.id}</h3>
        <div class="data">
          {#each item.people as thing}
            <div class="row">
              <p class="left">{thing.title}:</p>
              <p class="right">{thing.name}</p>
            </div>
          {/each}
        </div>
      {/each}
    </div>
  </div>
</main>

<style lang="scss">
  @use '../main.scss';
  .wrap {
    background-color: rgba(90, 47, 10, 0.692);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: medieval;
    margin: auto;
    background-attachment: fixed;
    .text {
      max-width: 95vw;
      text-align: center;
    }
  }
  .data {
    display: flex;
    flex-direction: column;
  }
  .row {
    display: flex;
    flex-direction: row;
    max-width: 70vw;
    align-items: center;
  }

  h3 {
    text-transform: capitalize;
    font-size: 2rem;
    color: gold;
  }
  p {
    color: rgb(27, 27, 27);
    font-size: 1.5rem;
  }
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
  @media only screen and (max-width: 767px) {
    p {
      font-size: 1rem;
    }
  }
</style>
