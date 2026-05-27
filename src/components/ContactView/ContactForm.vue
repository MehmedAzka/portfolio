<script setup>
import { ref, onMounted } from 'vue'

const form = ref({
    name: '',
    email: '',
    subject: '',
    message: ''
})

const isSubmitting = ref(false)

const handlePing = async () => {
    if (!form.value.subject) return alert("pilih subject dulu")

    isSubmitting.value = true

    setTimeout(() => {
        // alert(`Pesan masuk!\nNiat: ${form.value.subject}\n\nKalo gw ga sibuk ntar gw bales.`)
        isSubmitting.value = false

        // form.value = { name: '', email: '', subject: '', message: '' }
        alert('Maaf, fitur belum tersedia')
    }, 1500)
}
</script>

<template>
    <div class="mb-12 w-full border-b border-zinc-800 pb-6 flex flex-col items-center md:items-start">
        <h1 class="text-5xl font-bold tracking-tighter text-zinc-200 uppercase">
            Hit <span class="text-emerald-400">Me</span> Up.
        </h1>
        <p class="text-zinc-500 mt-3 text-sm tracking-wide">
            Let's connect with each other!
        </p>
    </div>

    <div class="w-full flex justify-center sm:justify-start">
        <form @submit.prevent="handlePing" class="w-full flex flex-col gap-6">

            <div class="flex flex-col sm:flex-row gap-6">
                <div class="w-full flex flex-col gap-2">
                    <label class="text-zinc-400 text-xs uppercase tracking-widest font-normal">Tell me your
                        name!</label>
                    <input v-model="form.name" type="text" required placeholder="John Doe"
                        class="w-full bg-zinc-950 border-b-2 border-zinc-800 p-2 text-zinc-200 placeholder-zinc-700 focus:outline-none focus:border-emerald-400 transition-colors">
                </div>
                <div class="w-full flex flex-col gap-2">
                    <label class="text-zinc-400 text-xs uppercase tracking-widest font-normal">Your
                        email</label>
                    <input v-model="form.email" type="email" required placeholder="john@xyz.com"
                        class="w-full bg-zinc-950 border-b-2 border-zinc-800 p-2 text-zinc-200 placeholder-zinc-700 focus:outline-none focus:border-emerald-400 transition-colors">
                </div>
            </div>

            <div class="w-full flex flex-col gap-2 relative">
                <label class="text-zinc-400 text-xs uppercase tracking-widest font-normal">What is your
                    purpose</label>
                <select v-model="form.subject" required
                    class="w-full bg-zinc-950 border-b-2 border-zinc-800 p-2 text-zinc-200 focus:outline-none focus:border-emerald-400 transition-colors appearance-none cursor-pointer"
                    :class="!form.subject ? 'text-zinc-700' : 'text-emerald-400 font-normal'">
                    <option value="" disabled selected>Choose one</option>
                    <option value="value1">Collaboration</option>
                    <option value="value2">Learning</option>
                    <option value="value3">Asking</option>
                    <option value="value4">Ping</option>
                </select>
                <div class="pointer-events-none absolute bottom-4 right-4 text-zinc-500">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>

            <div class="w-full flex flex-col gap-2">
                <label class="text-zinc-400 text-xs uppercase tracking-widest font-normal">Drop your
                    messages here!</label>
                <textarea v-model="form.message" required rows="4" placeholder="Tell me something"
                    class="w-full bg-zinc-950 border-b-2 border-zinc-800 p-2 text-zinc-200 placeholder-zinc-700 focus:outline-none focus:border-emerald-400 transition-colors resize-none"></textarea>
            </div>

            <button type="submit" :disabled="isSubmitting"
                class="mt-4 w-full sm:w-auto self-start px-6 py-3 bg-zinc-1950 font-normal border border-emerald-400 text-emerald-400 text-sm rounded-sm hover:bg-emerald-400 hover:text-zinc-950 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex justify-center items-center gap-2">
                <span v-if="isSubmitting"
                    class="w-4 h-4 border-2 border-emerald-400 border-t-transparent hover:border-zinc-950 rounded-full animate-spin"></span>
                {{ isSubmitting ? 'Sending...' : 'Send Message' }}
            </button>

        </form>
    </div>
</template>