<template>
    <div class="w-full overflow-hidden py-2">

        <div class="flex w-max animate-marquee">

            <div v-for="section in ['A', 'B', 'C']" :key="section" class="flex gap-6 px-3" aria-hidden="true">

                <div v-for="(tech, index) in arsenal" :key="section + index"
                    class="group flex items-center gap-4 px-6 py-3 bg-zinc-900/40 border border-zinc-800 rounded-full transition-all duration-300 hover:bg-zinc-800/80 hover:border-emerald-500/50 hover:shadow-[0_0_20px_rgba(16,185,129,0.2)] hover:-translate-y-1">

                    <img v-if="tech.logo" :src="tech.logo" :alt="tech.name" draggable="false"
                        class="h-6 w-6 object-contain grayscale opacity-50 transition-all duration-300 group-hover:grayscale-0 group-hover:opacity-100 drop-shadow-md" />

                    <span
                        class="text-sm font-medium text-zinc-500 uppercase tracking-widest select-none transition-colors duration-300 group-hover:text-emerald-400">
                        {{ tech.name }}
                    </span>

                </div>
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const arsenal = ref([
    { name: 'Vue.js', logo: 'https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg' },
    { name: 'Tailwind CSS', logo: 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg' },
    { name: 'C# WinForms', logo: 'https://gistcdn.githack.com/johndward01/95c1d09de9e3707cfb4154989962376d/raw/f74007782421219d9e9ab4b6a27de2e172a8b714/csharp-logo.svg' },
    { name: 'SQL', logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Microsoft_SQL_Server_2025_icon.svg/960px-Microsoft_SQL_Server_2025_icon.svg.png' },
    { name: 'IoT', logo: 'https://upload.wikimedia.org/wikipedia/commons/7/73/Arduino_IDE_logo.svg' },
    { name: 'Photoshop', logo: 'https://upload.wikimedia.org/wikipedia/commons/a/af/Adobe_Photoshop_CC_icon.svg' },
    { name: 'Figma', logo: 'https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg' },
    { name: 'Github', logo: 'https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg' },
    { name: 'Word', logo: 'https://upload.wikimedia.org/wikipedia/commons/e/e8/Microsoft_Office_Word_%282025%E2%80%93present%29.svg' },
    { name: 'Excel', logo: 'https://upload.wikimedia.org/wikipedia/commons/6/60/Microsoft_Office_Excel_%282025%E2%80%93present%29.svg' },
    { name: 'FIrebase', logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Firebase_Logo_%28No_wordmark%29_%282024-%29.svg" },
]);
</script>

<style scoped>
@keyframes marquee {
    0% {
        transform: translateX(0%);
    }

    100% {
        transform: translateX(-33.3333%);
    }
}

.animate-marquee {
    animation: marquee 25s linear infinite;
}
</style>