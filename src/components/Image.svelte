<script>
export let src;
export let alt;

function getDefault() {
    src = 'images/logo.png'
}

</script>


<img src="{src}" alt="{alt}" on:error="{() => getDefault()}"/>

<style lang="scss">
    img {
        width: 100%;
        object-fit: contain;
    }
    img:hover {
        transform: scale(1.05);
        box-shadow: 5px 5px 15px 5px #000000;
    }
</style>