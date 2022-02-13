<script>
  import { link } from 'svelte-routing';
  import MediaQuery from 'svelte-media-query';
  import { onMount } from 'svelte';

  let mobile = false;
  const pages = [
    { label: 'Inferno', href: '/' },
    { label: 'about', href: '/about' },
    { label: 'history', href: '/history' },
    { label: 'gigs', href: '/gigs' },
    { label: 'info', href: '/info' },
  ];
  const handleMobileIconClick = () => (mobile = !mobile);

  const mediaQueryHandler = (e) => {
    if (!e.matches) {
      mobile = false;
    }
  };

  onMount(() => {
    const mediaListener = window.matchMedia('(max-width: 600px)');
  });
</script>

<nav>
  <div class="inner">
    <div
      on:click={handleMobileIconClick}
      class={`mobile-icon${mobile ? ' active' : ''}`}
    >
      <div class="middle-line" />
    </div>
    <ul class={`navbar-lsit${mobile ? ' mobile' : ''}`}>
      {#each pages as item}
        <li>
          <a href={item.href}>{item.label}</a>
        </li>
      {/each}
    </ul>
  </div>
</nav>

<!-- 
<section>
  <div class="nav" id="navi">
    <a href="/" use:link>Inferno</a>
    <a href="/about" use:link>Mikä speksi?</a>
    <a href="/history" use:link>Aikaisemmat</a>
    <a href="/gigs" use:link>Keikat</a>
    <a href="/info" use:link>Yhdistys</a>
<MediaQuery query="(max-width: 600px)" let:matches>
      {#if matches}
        <div on:click={navFunc()}>
          <div>asdasd</div>
        </div>
      {/if}
    </MediaQuery>
  </div>
</section> -->
<style lang="scss">
  @use '../main.scss';
  section {
    background-color: main.$brown;
    .nav {
      z-index: 99;
      position: fixed;
      top: 0;
      left: 0;
      height: 5rem;
      width: 100vw;
      font-size: 2rem;
      background-image: linear-gradient(
        to right,
        rgba(34, 34, 34, 0.9),
        rgba(90, 58, 43, 0.9),
        rgba(34, 34, 34, 0.9)
      );
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      transition: all 0.3s;
    }
    a {
      text-transform: uppercase;
      list-style-type: none;
      display: inline-block;
      color: #e7e7e7;
      text-align: center;
      text-decoration: none;
      border-radius: 5rem;
      padding: 1rem 2rem;
      margin: 0.5rem;
      transition: all 0.3s;
      letter-spacing: 1px;
      font-size: 1.6rem;
      &:hover {
        background-color: #fdfdfd;
        color: main.$brown;
      }
    }
  }
</style>
