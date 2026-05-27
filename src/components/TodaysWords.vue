<script setup>
import { ref } from 'vue'
import TypeWriter from './HomeView/TypeWriter.vue'

const isModalOpen = ref(false)
const isFlipped = ref(false)
const currentItem = ref({ text: '', gif: false, audio: false, 'bg-card': false })

const isPlaying = ref(false)

let activeAudio = null

// Text: plain
// gif: link
// audio: link upload on Cloudinary
// bg-card: link gif/Cloudinary

const wordsArray = [
    {
        text: "knp genteng berat? karena ada \"G\"nya, klo ga ada jdi enteng",
        gif: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeThoOHlmbnJ1YXM5OHNsb2w4ZXl4ZXl2bWR5ajdkejV1cjJlbmNrNCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/GCO5WNzFmlc0vjK8cA/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "Hi! (gw ga sok ganteng yee)",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bnpxbXQ0b2luaXlkbXcxYW1mNjFpdms1ajZhb3BtbWc0dXduaDd2OCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/6hKL8BI8rRNrMRFtAx/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "gw ketika nemu error di kodingan...",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OXJhbjdlcDZyYTNuN2Y0ajRhNWJhcGlzc2k4ZnQ1dmVobzZ1OXV5OSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/pj6kX3c8bRijBrl6yR/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "potret orng yang bilang \"keknya gw avoidant dehh...\"",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dzRydHJzdHFocm10Y2lqMzBmdGsxYnZyNDlvN24wNnJzamRxYm12NSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/GDIEPuMGKgqiltEw68/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "masih sempet-sempetnya lu mikir \"telur dulu atau ayam dulu?\"",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NjJlcHN0dWpyMmdsZ3AycHI0aW9raGRicjc4eTdhdjg0amIzaXlsMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TPl5N4Ci49ZQY/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "ahhh.... pria solo itu lagi",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bm1pdXlzZXJ6b25sY2hic3ZjaXR4dnhoc201enp4d212eG9iZXkybCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VbYJPW1rjSrqRive5G/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "cewe lu ketika baca gugel maps",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Zno0azR5ZHliM2lwbmk5eWR0N3g5cXI4aTdqd2xhc3ZkcGpocWk0MSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/3o7aCTPPm4OHfRLSH6/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "jujur, ini absolute novel/manhwa, gw rekomen buat baca nih \"Omniscient Reader Viewpoint\"",
        gif: false,
        audio: "https://res.cloudinary.com/dg620epmv/video/upload/v1773269546/interlinked_bmszyr.mp3",
        'bg-card': "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGhrbGR4MWR0cGgyZzZhcHFwdG0wc3IxYngwa2I4amd0bnU5NGV4MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/joAu7iOWDOI2bdcDeF/giphy.gif"
    },
    {
        text: "bisa ga sih kalo tugas tuh datengnya 1 1, lu ngasih seabrek dikira gw dikasih makanan",
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cmllbjZ6MndoYmt2YzEybWNtZnRzbjQzOHRzc3U3aTRqdXlmdHUyNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tEG1nF1v7AL8A/giphy.gif",
        audio: false,
        'bg-card': false
    },
    {
        text: "coba kasih gw rekomendasi music/playlist, udh jenuh ama lagu indo (lagu galau smeua jirr...)",
        gif: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm9lc2hkN3lpdG9wcmM3ZjMxaWVmd2xxZjZycjU0ZnJkdzl1NmV3eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cPa0VPT5ZR8d6s9UGU/giphy.gif",
        audio: "https://res.cloudinary.com/dg620epmv/video/upload/v1773269183/music-calm_q8fdxs.mp3",
        'bg-card': false
    },
    {
        text: "congrats! lu nemuin kartu rare! ",
        gif: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWRzZnFmZno1cHprd3JoY21vMGJ6OTExNXBqYnMxdTdlcThxaG8zayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9HvfMzSvhM9K8/giphy.gif",
        audio: "https://res.cloudinary.com/dg620epmv/video/upload/v1773271264/brainrot_jfpafz.mp3",
        'bg-card': "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWRzZnFmZno1cHprd3JoY21vMGJ6OTExNXBqYnMxdTdlcThxaG8zayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9HvfMzSvhM9K8/giphy.gif",
    },
    {
        text: false,
        gif: "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aHdheWY3MzJ0ajB4MjVwOHlqaDRwbGcyNWUwbzJuaGZ5M2xkbzdqYyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/i17zHLTMt1SmJMv6Aw/giphy.gif",
        audio: "",
        'bg-card': "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aHdheWY3MzJ0ajB4MjVwOHlqaDRwbGcyNWUwbzJuaGZ5M2xkbzdqYyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/i17zHLTMt1SmJMv6Aw/giphy.gif",
    }
]

const openModal = () => {
    isFlipped.value = false
    isModalOpen.value = true
    isPlaying.value = false

    const today = new Date()
    if (today.getMonth() === 2 && today.getDate() === 28) {
        currentItem.value = {
            text: "What day is it today? Take a guess.",
            gif: false,
            audio: "https://res.cloudinary.com/dg620epmv/video/upload/v1773267466/calm_ar3i5f.mp3",
            'bg-card': "https://res.cloudinary.com/dg620epmv/image/upload/v1773267245/luxury_jnuobv.png",
        }
    } else {
        const randomIndex = Math.floor(Math.random() * wordsArray.length)
        currentItem.value = wordsArray[randomIndex]
    }
}

const closeModal = () => {
    isModalOpen.value = false
    isPlaying.value = false

    if (activeAudio) {
        activeAudio.pause()
        activeAudio.currentTime = 0
        activeAudio = null
    }
}

const flipCard = () => {
    if (isFlipped.value) return

    isFlipped.value = true

    if (currentItem.value.audio) {
        activeAudio = new Audio(currentItem.value.audio)
        activeAudio.loop = false

        activeAudio.play().then(() => {
            isPlaying.value = true
        }).catch(e => console.error("Error muter lagu:", e))

        activeAudio.onended = () => {
            isPlaying.value = false
        }
    }
}
</script>

<template>
    <div>
        <button @click="openModal"
            class="border border-emerald-400 text-emerald-400 rounded-sm px-3 py-2 font-normal hover:bg-emerald-400 hover:text-black hover:shadow-lg hover:shadow-emerald-400 transition-all">
            Get some words!
        </button>

        <Teleport to="body">
            <transition name="fade">
                <div v-if="isModalOpen" @click.self="closeModal"
                    class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm">

                    <div class="card-container w-82 h-106 cursor-pointer" @click="flipCard">
                        <div
                            :class="['card-inner relative w-full h-full transition-transform duration-700', isFlipped ? 'rotate-y-180' : '']">

                            <div
                                class="card-front absolute inset-0 flex flex-col items-center justify-center bg-zinc-900 border border-emerald-500/30 rounded-xl shadow-[0_0_30px_rgba(16,185,129,0.1)]">
                                <span class="text-emerald-400 font-mono tracking-widest text-sm animate-pulse">TAP THE
                                    CARD</span>
                            </div>

                            <div class="card-back absolute inset-0 flex flex-col items-center justify-center border border-emerald-400 rounded-xl p-6 text-center rotate-y-180 shadow-[0_0_40px_rgba(16,185,129,0.3)] overflow-hidden bg-emerald-950 bg-cover bg-center"
                                :style="currentItem['bg-card'] ? `background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(2, 44, 34, 0.9)), url('${currentItem['bg-card']}');` : ''">

                                <img v-if="currentItem.gif" :src="currentItem.gif" draggable="false"
                                    class="w-32 h-32 object-cover rounded-lg mb-4 border-2 border-emerald-500/30 shadow-lg relative z-10"
                                    alt="Daily GIF" />

                                <p
                                    class="text-zinc-200 font-sans font-medium text-lg leading-relaxed relative z-10 drop-shadow-md">
                                    {{ currentItem.text }}
                                </p>
                                <div class="mt-4 relative z-10">

                                    <div v-if="currentItem.audio"
                                        class="flex items-center gap-2 bg-emerald-950/80 border border-emerald-500/50 shadow-[0_0_10px_rgba(16,185,129,0.2)] px-3 py-1 rounded-full transition-all">

                                        <div class="relative flex h-3 w-3 items-center justify-center">
                                            <span v-if="isPlaying"
                                                class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>

                                            <span
                                                :class="['relative inline-flex rounded-full h-2 w-2 transition-colors duration-300', isPlaying ? 'bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.8)]' : 'bg-zinc-500']"></span>
                                        </div>

                                        <span
                                            :class="['font-mono text-xs uppercase font-normal tracking-widest transition-colors duration-300', isPlaying ? 'text-emerald-400' : 'text-zinc-500']">
                                            Audio
                                        </span>
                                    </div>

                                    <div v-else
                                        class="bg-black/60 border border-zinc-700 px-3 py-1 rounded-full backdrop-blur-sm">
                                        <span
                                            class="text-zinc-400 font-mono text-xs uppercase font-normal tracking-widest text-shadow-sm">Some
                                            Words</span>
                                    </div>

                                </div>
                            </div>

                        </div>
                    </div>

                </div>
            </transition>
        </Teleport>
    </div>
</template>

<style scoped>
/* CSS tetep sama persis kayak sebelumnya, ga ada yang dirubah */
.card-container {
    perspective: 1000px;
}

.card-inner {
    transform-style: preserve-3d;
}

.card-front,
.card-back {
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
}

.rotate-y-180 {
    transform: rotateY(180deg);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>