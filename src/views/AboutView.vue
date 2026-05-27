<script setup>
import { ref, onMounted, watch } from 'vue'
import translationsData from './../components/_dataJSON/AboutView.json'
import SkillsCard from '@/components/AboutView/SkillsCard.vue'
import Experience from '@/components/AboutView/Experience.vue'

const isLoaded = ref(false)

onMounted(() => {
    setTimeout(() => {
        isLoaded.value = true
    }, 100)
})

const selectedLang = ref('english')
const displayText = ref('')
let typingTimer = null

const startTypewriter = () => {
    if (typingTimer) clearInterval(typingTimer)

    const fullText = translationsData[selectedLang.value]
    displayText.value = ''

    let i = 0
    const speed = 1600 / fullText.length

    typingTimer = setInterval(() => {
        displayText.value += fullText.charAt(i)
        i++
        if (i >= fullText.length) {
            clearInterval(typingTimer)
        }
    }, speed)
}

watch(selectedLang, () => {
    startTypewriter()
})

onMounted(() => {
    startTypewriter()
})
</script>

<template>
    <main class=" pt-20 min-h-screen">

        <section class=" w-full min-h-100 flex justify-center
        pt-10 md:pt-0 px-5 lg:px-0 pb-10
        transition-all duration-700 ease-out"
            :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
            <div
                class="w-full max-w-250 mx-auto flex flex-col justify-start md:justify-center items-start pt-0 sm:pt-20">

                <div class="w-full h-auto border-b pb-4 mb-6
                    flex flex-col sm:flex-row justify-center sm:justify-between items-center sm:items-end">
                    <h1 class="text-5xl font-bold tracking-tighter text-zinc-200 mb-5 sm:mb-0">
                        <span class="text-emerald-400">About </span>Me!
                    </h1>

                    <select v-model="selectedLang" id="language" class="w-40 h-10 bg-zinc-950 rounded-sm text-center text-white shadow-xl shadow-emerald-400/10 border-x-2 border-emerald-400 appearance-none select-none
                         transition-all cursor-pointer font-normal focus:outline-none">
                        <option value="ind">Indonesia</option>
                        <option value="english">English</option>
                        <option value="japan">日本 (Japan)</option>
                        <option value="india">भारत (India)</option>
                        <option value="russia">Россия (Rusia)</option>
                        <option value="lorem">Lorem Ipsum 😮</option>
                    </select>
                </div>

                <div class="min-h-20 w-full h-full">
                    <p class="text-zinc-400 text-lg leading-relaxed mb-1 whitespace-pre-wrap">
                        {{ displayText }}<span
                            class="inline-block w-2 h-5 ml-1 bg-emerald-400 animate-pulse align-middle"></span>
                    </p>
                    <p class=" text-sm font-normal text-gray-700">translated by DeepL.</p>
                </div>

            </div>
        </section>

        <section class=" w-full flex flex-col justify-center items-center">
            <div class="w-full max-w-250 mx-auto flex flex-col justify-start items-center sm:items-start py-10 sm:py-20 px-4 lg:px-0
            transition-all duration-700 ease-out delay-200"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                <h1 class=" text-5xl font-bold tracking-tighter text-zinc-200 mb-5">
                    <span class="text-emerald-400">Catalog </span>Skills
                </h1>
                <SkillsCard />
            </div>
        </section>

        <section class=" w-full flex flex-col justify-center items-center overflow-hidden">
            <div class="w-full max-w-250 mx-auto flex flex-col justify-start items-center sm:items-start py-10 sm:py-20 px-4 lg:px-0 transition-all duration-700 ease-out delay-400"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                <Experience />
            </div>
        </section>
    </main>
</template>

<!-- Buang paragraf panjang soal lu lahir di mana dan hobi lu apa. Ga ada yang mau baca novel di web porto.

1. Experience Timeline: Bikin timeline vertikal animasi scroll. Masukin sejarah lu, dari pengalaman ngurus kepanitiaan, project kampus, sampe sertifikasi.
2. Personal Stats (RPG Style): Ini easter egg biar lu keliatan kayak manusia, bukan AI. Bikin semacam progress bar atau status card.
Isinya bisa skill coding lu, dicampur sama personal quest lu (misal: Current Goal: Achieving Sleeper Build atau Main Fuel: Monster Energy Ultra White).
Ini nunjukin personality tanpa jadi alay. -->