<script>
  import { Router, Route } from 'svelte-routing';
  import Home from '../routes/index.svelte';
  import About from '../routes/about.svelte';
  // import History from '../routes/history.svelte';
  // import Gigs from '../routes/gigs.svelte';
  import Yhdistys from '../routes/organization.svelte';
  import Calendar from '../routes/calendar.svelte';
  import Nav from '../components/nav.svelte';
  import Footer from '../components/footer.svelte';

  export let url = '';
</script>

<Router {url}>
  <Nav />
  <div>
    <Route path="/" component={Home} />
    <Route path="/speksi" component={About} />
    <!-- <Route path="/history" component={History} /> -->
    <!-- <Route path="/gigs" component={Gigs} /> -->
    <Route path="/yhdistys" component={Yhdistys} />
    <Route path="/calendar" component={Calendar} />
  </div>
  <Footer />
</Router>

<style lang="scss">
</style>
