<template>
    <img :src="gifs[currentIndex]" alt="gif" class="rounded-2xl w-full h-full object-cover" draggable="false">
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const gifs = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2kzNGdnZmltMWNpN2NwcTd4M2tmejl4Ynh2YnNnNDBsODJxZXI3cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0MYC0LajbaPoEADu/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2kzNGdnZmltMWNpN2NwcTd4M2tmejl4Ynh2YnNnNDBsODJxZXI3cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ae7SI3LoPYj8Q/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NXdvOHNnNWJwMWRyczU5Mm50eGk5YTl5dnVkeXJ6MmVzc2I1YmdtaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ASd0Ukj0y3qMM/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bTRtZXQwcWh6bWF3d2lxajR3aHF3ZHhrMDJscWIzY2dyaGZleWc4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Xunf7NetNL7WunHnVv/giphy.gif",
];

const currentIndex = ref(0);
let timer;

onMounted(() => {
    timer = setInterval(() => {
        currentIndex.value = (currentIndex.value + 1) % gifs.length;
    }, 3000);
});

onUnmounted(() => {
    clearInterval(timer);
});
</script>