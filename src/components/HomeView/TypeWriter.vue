<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

// Definisi array kata-kata lu
const roles: string[] = [
    "Newbie Typewriter 🥲",
    "Front-End Dev 🔥🔥",
    "UI/UX Designer 😎",
    "Poster Designer . . .",
    "Low Cortisol Person~~"
];

const displayText = ref<string>("");
const currentWordIndex = ref<number>(0);
const isDeleting = ref<boolean>(false);
const typeSpeed = ref<number>(150);

const type = () => {
    const currentFullText = roles[currentWordIndex.value];

    if (isDeleting.value) {
        displayText.value = currentFullText.substring(0, displayText.value.length - 1);
        typeSpeed.value = 40;
    } else {
        displayText.value = currentFullText.substring(0, displayText.value.length + 1);
        typeSpeed.value = 150;
    }

    if (!isDeleting.value && displayText.value === currentFullText) {
        isDeleting.value = true;
        typeSpeed.value = 800;
    } else if (isDeleting.value && displayText.value === "") {
        isDeleting.value = false;
        currentWordIndex.value = (currentWordIndex.value + 1) % roles.length;
        typeSpeed.value = 300;
    }

    setTimeout(type, typeSpeed.value);
};

onMounted(() => {
    type();
});
</script>

<template>
    {{ displayText }}<span class="animate-pulse-fast border-r border-white"></span>
</template>

<style scoped>
/* Biar kursornya kedip-kedip kayak terminal beneran */
@keyframes blink {
    50% {
        display: none;
    }
}

.animate-pulse-fast {
    animation: blink 0.7s step-end infinite;
}
</style>