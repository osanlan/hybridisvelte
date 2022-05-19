<script>
  import { Router, Route } from 'svelte-routing';
  import Home from '../routes/index.svelte';
  import About from '../routes/about.svelte';
  // import History from '../routes/history.svelte';
  import Gigs from '../routes/gigs.svelte';
  import Organization from '../routes/organization.svelte';
  import Calendar from '../routes/calendar.svelte';
  import Nav from '../components/nav.svelte';
  import Footer from '../components/footer.svelte';
  import Songs from '../routes/songs.svelte';

  export let url = '';
</script>

<Router {url}>
  <Nav />
  <Route path="/"><Home /></Route>
  <Route path="/speksi"><About /></Route>
  <!-- <Route path="/history" component={History} /> -->
  <Route path="/gigs"><Gigs /></Route>
  <Route path="/yhdistys"><Organization /></Route>
  <Route path="/calendar"><Calendar /></Route>
  <Route path="/biisit"><Songs /></Route>
  <Footer />
</Router>
