<script setup>
import { namedQuery } from 'firebase/firestore'
import { ref, onMounted } from 'vue'

const skills = [
    { name: 'HTML/CSS', target: 90, bg: "https://upload.wikimedia.org/wikipedia/commons/5/5f/Html-1.svg" },
    { name: 'JavaScript', target: 40, bg: "https://upload.wikimedia.org/wikipedia/commons/3/3b/Javascript_Logo.png" },
    { name: 'Vue.js', target: 35, bg: "https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" },
    { name: 'Tailwind', target: 85, bg: "https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" },
    { name: 'PHP', target: 20, bg: "https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg" },
    { name: 'C# WinForms', target: 35, bg: "https://gistcdn.githack.com/johndward01/95c1d09de9e3707cfb4154989962376d/raw/f74007782421219d9e9ab4b6a27de2e172a8b714/csharp-logo.svg" },
    { name: 'SQL', target: 40, bg: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Microsoft_SQL_Server_2025_icon.svg/960px-Microsoft_SQL_Server_2025_icon.svg.png" },
    { name: 'Firebase', target: 20, bg: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Firebase_Logo_%28No_wordmark%29_%282024-%29.svg" },
    { name: 'ESP32 IoT', target: 70, bg: "https://upload.wikimedia.org/wikipedia/commons/7/73/Arduino_IDE_logo.svg" },
    { name: 'Photoshop', target: 60, bg: "https://upload.wikimedia.org/wikipedia/commons/a/af/Adobe_Photoshop_CC_icon.svg" },
    { name: 'Figma', target: 90, bg: "https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" },
    { name: 'Word', target: 80, bg: "https://upload.wikimedia.org/wikipedia/commons/e/e8/Microsoft_Office_Word_%282025%E2%80%93present%29.svg" },
    { name: 'Excel', target: 75, bg: "https://upload.wikimedia.org/wikipedia/commons/6/60/Microsoft_Office_Excel_%282025%E2%80%93present%29.svg" },
]

const currentValues = ref(skills.map(() => 0))

const showProgress = ref(false)

onMounted(() => {
    setTimeout(() => {
        showProgress.value = true
    }, 100)

    skills.forEach((skill, index) => {
        let start = 0
        const duration = 1400
        const increment = skill.target / (duration / 16)

        const updateCounter = () => {
            start += increment
            if (start < skill.target) {
                currentValues.value[index] = Math.floor(start)
                requestAnimationFrame(updateCounter)
            } else {
                currentValues.value[index] = skill.target
            }
        }
        updateCounter()
    })
})
</script>

<template>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 w-full">

        <div v-for="(skill, index) in skills" :key="index"
            class="relative overflow-hidden w-full p-4 bg-zinc-900 border border-emerald-500/20 rounded-lg shadow-lg hover:border-emerald-400 hover:shadow-[0_0_15px_rgba(52,211,153,0.3)] transition-all group">

            <img v-if="skill.bg" :src="skill.bg"
                class="absolute -bottom-10 -left-5 w-auto h-32 opacity-10 grayscale group-hover:opacity-20 group-hover:grayscale-0 transition-all duration-500 z-0 select-none pointer-events-none mask-add"
                draggable="false">

            <div class="relative z-10 flex justify-between items-end mb-3">
                <h1
                    class="font-normal text-lg text-zinc-200 tracking-tight group-hover:text-emerald-400 transition-colors">
                    {{ skill.name }}
                </h1>
                <p class="text-emerald-400 font-mono text-sm font-normal">
                    {{ currentValues[index] }}%
                </p>
            </div>

            <div class="relative z-10 w-full bg-zinc-950 h-2 rounded-full overflow-hidden shadow-inner">
                <div class="bg-emerald-400 h-full rounded-full transition-all ease-out"
                    style="transition-duration: 1500ms;" :style="{ width: showProgress ? skill.target + '%' : '0%' }">
                </div>
            </div>

        </div>

    </div>
</template>