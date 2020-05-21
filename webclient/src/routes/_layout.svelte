<script>
  import Nav from "../components/Nav.svelte";
</script>

<style>
  main {
    position: relative;
    max-width: 56em;
    background-color: white;
    padding: 0 2em 2em 2em;
    margin: 4em auto 0 auto;
    box-sizing: border-box;
  }
</style>

<Nav />

<main>
  <slot />
</main>
