<script setup>
import { RouterView } from 'vue-router';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
import Avaible from './components/Avaible.vue';

</script>

<template>
  <main class=" w-full h-auto min-h-screen bg-zinc-950 text-white font-normal overflow-x-hidden">
    <Navbar />
    <RouterView />
    <Footer />
  </main>
</template>
