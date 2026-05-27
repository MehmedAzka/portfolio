<script setup>
import { ref, onMounted } from 'vue'
import { auth, db } from '../firebaseConfig'
import { signInWithPopup, GoogleAuthProvider, signOut } from "firebase/auth"
import { doc, getDoc, updateDoc, onSnapshot } from "firebase/firestore"

const isAvailable = ref(true)
const isAdmin = ref(false)
const clickCount = ref(0)
let clickTimer = null

const ADMIN_UID = "omuu64gUgbPEv9ejFBbSu6GCUAK2"

onMounted(() => {
    const statusRef = doc(db, 'portfolio', 'status')
    onSnapshot(statusRef, (doc) => {
        if (doc.exists()) {
            isAvailable.value = doc.data().isAvailable
        }
    })
})

const handleSecretClick = async () => {
    if (isAdmin.value) return

    clickCount.value++

    if (clickTimer) clearTimeout(clickTimer)
    clickTimer = setTimeout(() => { clickCount.value = 0 }, 500)

    if (clickCount.value === 20) {
        clickCount.value = 0

        try {
            const provider = new GoogleAuthProvider()
            const result = await signInWithPopup(auth, provider)

            if (result.user.uid === ADMIN_UID) {
                isAdmin.value = true
                alert("Welcome back")
            } else {
                alert("Error!")
                await signOut(auth)
            }
        } catch (error) {
            console.error("Failed to login:", error)
        }
    }
}

const toggleStatus = async () => {
    if (!isAdmin.value) return

    const newStatus = !isAvailable.value
    const statusRef = doc(db, 'portfolio', 'status')

    try {
        await updateDoc(statusRef, { isAvailable: newStatus })
    } catch (error) {
        console.error("Failed to update status:", error)
    }
}
</script>

<template>
    <div class="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 flex flex-col items-center gap-3">

        <main @click="handleSecretClick" class="h-10 rounded-full p-0.5 select-none" :class="[
            isAvailable ? 'bg-linear-to-r from-emerald-400 to-emerald-600 shadow-[0_0_20px_rgba(52,211,153,0.3)]' : 'bg-linear-to-r from-gray-500 to-gray-700 shadow-[0_0_20px_rgba(54, 65, 83, 0.3)]'
        ]">
            <div class="w-fit h-full bg-zinc-950 rounded-full flex flex-row justify-center items-center px-5 gap-3">
                <span class="w-2.5 h-2.5 rounded-full animate-pulse transition-colors duration-500"
                    :class="isAvailable ? 'bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.8)]' : 'bg-gray-500 shadow-[0_0_8px_rgba(54, 65, 83, 0.8)]'"></span>
                <p class="font-mono text-xs sm:text-sm font-normal tracking-wide transition-colors duration-500"
                    :class="isAvailable ? 'text-emerald-400' : 'text-gray-500'">
                    {{ isAvailable ? 'Available' : 'Not Available' }}
                </p>
            </div>
        </main>

        <div v-if="isAdmin"
            class="bg-zinc-900 border border-zinc-700 p-2 rounded-lg shadow-xl flex gap-2 animate-pulse">
            <button @click="toggleStatus" class="px-4 py-1 bg-zinc-800 text-zinc-200 text-xs font-mono rounded">
                Change to "{{ isAvailable ? 'Not Available' : 'Available' }}"
            </button>
        </div>

    </div>
</template>