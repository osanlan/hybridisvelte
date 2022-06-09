<script>
    import Image from '../components/Image.svelte';

    export let speksi;

    let src = "images/db/" + speksi.year + "/" + speksi.banner
    let year = speksi.year;

</script>

{#if (year)}
<div class="container">
    <div class="speksi">
        <Image {src} alt=""/>
        {speksi.name}
    </div>
</div>
{/if}

<style lang="scss">
    .container {
        margin-top: 5rem;
        display: flex;
        justify-content: center;
        .speksi {
            width: 60%;
        }

    }
</style>
