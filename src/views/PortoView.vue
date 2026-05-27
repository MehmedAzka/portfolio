<script setup>
import { ref, onMounted } from 'vue'
import PortoList from '@/components/PortoView/PortoList.vue'
import ChatBot from '@/components/PortoView/ChatBot.vue'

const isLoaded = ref(false)

onMounted(() => {
    setTimeout(() => {
        isLoaded.value = true
    }, 100)
})
</script>

<template>
    <main class=" pt-20 min-h-screen">

        <section class=" w-full flex flex-col justify-center items-center">
            <div class="w-full max-w-7xl mx-auto flex flex-col items-center lg:items-start py-10 sm:py-20 px-4 xl:px-0 transition-all duration-700"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                <PortoList />
            </div>
        </section>

        <!-- <section class=" w-full flex flex-col justify-center items-center">
            <div class="w-full max-w-7xl mx-auto flex flex-col items-center lg:items-start py-10 sm:py-20 px-4 xl:px-0 transition-all duration-700 delay-200"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                <ChatBot />
            </div>
        </section> -->

    </main>
</template>

<!-- Ini panggung lu. Realitanya, HRD atau klien ga peduli sama UI lu kalo dalemannya sampah. Mereka mau liat LOGIKA lu nyelesaiin masalah.

1. Jangan Cuma List Gambar: Tiap project harus bisa di-klik dan buka case study detail.
2. Bedah Kasus (Case Study): * Kalo lu majang project IoT, jangan cuma foto alatnya. Jelasin gimana lu ngatur pin ESP32-nya, sensor apa yang lu pake, dan data flow-nya ke aplikasi.
    - Kalo lu majang project Windows Forms pake C#, pamerin skema database SQLite lu. Ceritain bug paling goblok yang lu alamin dan gimana lu nge-fix itu.
3. Links: Wajib ada tombol ke repo GitHub atau Live Demo. Kalo ga ada link kodenya, lu cuma dianggep tukang claim hasil kerjaan orang. -->