<script>
  import { Router, Route } from 'svelte-routing';
  import Home from '../routes/index.svelte';
  import About from '../routes/about.svelte';
  import History from '../routes/history.svelte';
  import Gigs from '../routes/gigs.svelte';
  import Yhdistys from '../routes/organization.svelte';
  import Nav from '../components/nav.svelte';
  import Footer from '../components/footer.svelte';

  export let url = '';
</script>

<Router {url}>
  <Nav />
  <div>
    <Route path="/" component={Home} />
    <Route path="/about" component={About} />
    <Route path="/history" component={History} />
    <Route path="/gigs" component={Gigs} />
    <Route path="/info" component={Yhdistys} />
  </div>
  <Footer />
</Router>

<style lang="scss">
</style>
