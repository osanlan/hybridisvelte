<script>
  import { link } from 'svelte-routing';
  // const pages = [
  //   { label: 'Home', href: '/' },
  //   { label: 'Home2', href: '/about' },
  //   { label: 'Home3', href: '/history' },
  //   { label: 'Home4', href: '/gigs' },
  //   { label: 'Home5', href: '/info' },
  // ];
</script>

<section>
  <div class="nav">
    <a href="/" use:link>Inferno</a>
    <a href="/about" use:link>Mikä speksi?</a>
    <a href="/history" use:link>Aikaisemmat</a>
    <a href="/gigs" use:link>Keikat</a>
    <a href="/info" use:link>Yhdistys</a>
  </div>
</section>

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
      align-items: center;
      justify-content: center;
      // font-family: 'Orbitron', sans-serif;
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
