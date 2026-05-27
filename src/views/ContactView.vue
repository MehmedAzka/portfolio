<script setup>
import { ref, onMounted } from 'vue'
import ContactForm from '@/components/ContactView/ContactForm.vue'
import CardLink from '@/components/ContactView/CardLink.vue';

// Logic transisi lu
const isLoaded = ref(false)
onMounted(() => {
    setTimeout(() => {
        isLoaded.value = true
    }, 100)
})


</script>

<template>
    <main class=" pt-20 min-h-screen">
        <section class="w-full flex justify-center items-center">

            <div class="w-full max-w-4xl mx-auto flex flex-col items-center lg:items-start py-10 sm:py-20 px-4 xl:px-0 transition-all duration-700"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                <ContactForm />
            </div>
        </section>
    </main>
</template>