<script>
</script>

<section>
  <div class="logos">
    <button>insta</button>
    <button>face</button>
    <button>youtube</button>
    <button>mail</button>
    <button>calndart</button>
  </div>
  <div>© 2020 HybridiSpeksi</div>
</section>

<style lang="scss">
  @use '../main.scss';
  $grad: linear-gradient(
    to right,
    rgba(14, 14, 14, 0.9),
    rgba(60, 28, 23, 0.9),
    rgba(14, 14, 14, 0.9)
  );
  section {
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: gold;
    background-image: $grad;
  }
</style>
