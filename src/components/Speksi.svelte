<script>
    import Image from '../components/Image.svelte';
    import { scale, fade, slide } from 'svelte/transition';

    export let speksi;

    let src = "images/db/" + speksi.year + "/" + speksi.banner
    let year = speksi.year;

</script>

{#if (year)}
<div class="container" style="--bg1: {speksi.colors?.bg1}; --bg2: {speksi.colors?.bg2}"
    transition:slide="{{duration: 1000}}" >
    <div class="speksi" style="--bg1: {speksi.colors?.bg1}; --bg2: {speksi.colors?.bg2}">
        <Image {src} alt=""/>
        <h2>{speksi.name}</h2>
        <ul class="stats">
            {#each speksi.statistics as stat}
            <li><p><strong>{Object.keys(stat)}</strong>: {#if (speksi.year == 2020 && Object.keys(stat) =="Ensi-ilta")}<strike>{Object.values(stat)}</strike> TBA{:else}{Object.values(stat)}{/if}</p></li>
            {/each}
        </ul>
        {#each speksi.text as text}
        <p class="synopsis">{text}</p>
        {/each}
        <div class="buttons" style="--btncol: {speksi.colors.button}; --buttonColor: {speksi.colors?.buttonColor}">
            {#each speksi.resources as resource}
            <a class="button" href="{resource.url}">
                <span>{resource.title}</span>
            </a>
            {/each}
        </div>
    </div>
</div>
{/if}

<style lang="scss">
    @use '../main.scss';
    .container {
        font-family: 'Red Hat Display', sans-serif;
        // margin-top: 10px;
        display: flex;
        width: 100%;
        justify-content: center;
        background-image: linear-gradient(to right, var(--bg1), var(--bg2), var(--bg1));
        border-radius: 10px;
        @media only screen and (max-width:850px) {
                border-radius: 0;   
            }
        .speksi {
            width: 60%;
            flex-direction: column;
            max-width: 90%;
            text-align: center;
            background-color: white;
            margin: 5rem auto;
            border-radius: 7px;
            > :global(img) {
                border-radius: 7px 7px 0 0;
                width: 100%;
            }
            @media only screen and (max-width:850px) {
                width: 90%;
                margin: 15px;

                
            }
            h2 {
                text-transform: uppercase;
                color: var(--bg1);
            }
            .stats {
                list-style-type: none;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                justify-content: center;
                max-width: 80%;
                li {
                    padding: 0 10px;
                    p {
                        font-weight: 100;
                    }
                }
            }
            .synopsis {
                width: 80%;
                margin: 0 auto;
            }
            .buttons {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                a {
                    background-color: var(--btncol);
                    border: none;
                    border-radius: 5px;
                    display: inline-block;
                    padding: 5px 2rem;
                    margin: 1rem;
                    transition: all 0.3s;
                    box-shadow: 0px 2px 5px #484848;
                    color: var(--buttonColor);
                    width: 7rem;
                    span {
                        margin: 1px;
                    }
                    &:hover {
                        transform: scale(1.05);
                        box-shadow: 0px 2px 9px #484848;
                        text-decoration: none;
                    }
                }
            }
        }
    }
</style>
