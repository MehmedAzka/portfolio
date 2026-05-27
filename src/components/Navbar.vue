<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<template>
  <div
    class="fixed top-5 left-1/2 -translate-x-1/2 
    max-w-xl w-19/20 sm:w-full bg-black/40 shadow-xl/5 shadow-white backdrop-blur-sm rounded-md h-16 flex items-center justify-between px-6 text-white font-[poppins] font-light z-100">

    <div class="text-xl font-bold tracking-tighter">
      LOGO<span class="text-emerald-400">.</span>
    </div>

    <div class="hidden md:flex items-center space-x-8">
      <RouterLink to="/" active-class="text-emerald-400" class="hover:text-emerald-400 duration-200">Home
      </RouterLink>
      <RouterLink to="/about" active-class="text-emerald-400" class="hover:text-emerald-400 duration-200">About
      </RouterLink>
      <RouterLink to="/porto" active-class="text-emerald-400" class="hover:text-emerald-400 duration-200">Portofolio
      </RouterLink>
    </div>

    <div class=" hidden md:block items-center space-x-8">
      <RouterLink
        class=" border border-emerald-400 text-emerald-400 rounded-sm px-4 py-2 font-medium hover:bg-emerald-400 hover:text-black transition-colors"
        to="/contact">Contact</RouterLink>
    </div>

    <button @click="toggleMenu"
      class="md:hidden flex flex-col justify-center items-center w-8 h-8 space-y-1.5 focus:outline-none">
      <span
        :class="['block w-6 h-0.5 bg-white transition-all duration-300', isMenuOpen ? 'rotate-45 translate-y-2' : '']"></span>
      <span :class="['block w-6 h-0.5 bg-white transition-opacity duration-300', isMenuOpen ? 'opacity-0' : '']"></span>
      <span
        :class="['block w-6 h-0.5 bg-white transition-all duration-300', isMenuOpen ? '-rotate-45 -translate-y-2' : '']"></span>
    </button>

    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100" leave-active-class="transition duration-150 ease-in"
      leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
      <div v-if="isMenuOpen"
        class="absolute top-20 right-0 w-48 bg-black/95 border border-gray-800 rounded-2xl py-4 px-6 flex flex-col space-y-4 md:hidden">
        <RouterLink @click="isMenuOpen = false" to="/" active-class="text-emerald-400"
          class="hover:text-emerald-400 transition-colors">Home</RouterLink>
        <RouterLink @click="isMenuOpen = false" to="/about" active-class="text-emerald-400"
          class="hover:text-emerald-400 transition-colors">About</RouterLink>
        <RouterLink @click="isMenuOpen = false" to="/porto" active-class="text-emerald-400"
          class="hover:text-emerald-400 transition-colors">Portofolio
        </RouterLink>
        <RouterLink @click="isMenuOpen = false"
          class=" border border-emerald-400 text-emerald-400 rounded-sm px-4 py-2 font-medium hover:bg-emerald-400 hover:text-black transition-colors"
          to="/contact">Contact</RouterLink>
      </div>
    </Transition>
  </div>
</template>