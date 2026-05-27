<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue'
import TypeWriter from '@/components/HomeView/TypeWriter.vue';
import Carousel from '@/components/HomeView/Carousel.vue';
import GifSlideShow from '@/components/HomeView/GifSlideShow.vue';

const isLoaded = ref(false)

onMounted(() => {
    setTimeout(() => {
        isLoaded.value = true
    }, 100)
})
</script>

<template>
    <main class=" pt-20 min-h-screen">

        <section class=" w-full h-150 flex justify-center
            pt-10 md:pt-0 px-10 lg:px-0
            transition-all duration-700 ease-out"
            :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
            <div class=" w-full h-full flex flex-row items-start md:items-center justify-center 2xl:w-2/3">

                <!-- TEXT -->
                <div class=" w-full flex flex-col lg:w-1/2 lg:px-0 lg:pr-5">
                    <h1 class=" text-center lg:text-left text-5xl font-bold tracking-tighter mb-6">
                        Hey there! I'm
                        <span class=" text-emerald-400">Moxka</span>
                    </h1>
                    <p class=" text-center lg:text-left text-xl mb-4">a <span class=" text-emerald-400 font-normal">
                            <TypeWriter />
                        </span></p>
                    <p class=" text-center lg:text-left text-lg mb-8">I'm a passionate frontend developer with a knack
                        for
                        crafting beautiful and
                        functional web experiences. With a strong foundation in HTML, CSS, and JavaScript, I specialize
                        in
                        creating responsive and user-friendly interfaces that bring ideas to life.</p>

                    <RouterLink
                        class="self-center lg:self-start border border-emerald-400 text-emerald-400 rounded-sm px-6 py-3 font-medium hover:bg-emerald-400 hover:text-black hover:shadow-lg hover:shadow-emerald-400 transition-all"
                        to="/about">About my self</RouterLink>

                </div>

                <!-- IMAGE -->
                <div class=" w-2/6 xl:w-1/4 2xl:w-1/3 h-full hidden lg:flex items-center justify-end">
                    <img src="./../assets/logo.svg" alt="Profile Image"
                        class=" w-80 h-80 rounded-full object-cover shadow-xl shadow-emerald-400" draggable="false">
                </div>

            </div>


        </section>

        <section class=" w-full h-auto flex flex-col items-center justify-center mb-12 relative">
            <div class=" bg-linear-to-r from-zinc-950 to-transparent w-2/10 h-full absolute left-0 z-50"></div>
            <Carousel />
            <div class=" bg-linear-to-l from-zinc-950 to-transparent w-2/10 h-full absolute right-0 z-50"></div>
        </section>

        <section class=" w-full h-auto flex flex-col items-center justify-center py-20 px-0 md:px-20 bg-emerald-400">
            <h1 class=" text-3xl font-bold tracking-tighter mb-6 text-center | transition-all duration-700 ease-out delay-200"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                Welcome to my portfolio!</h1>
            <p class=" text-center text-lg mb-8 px-10 | transition-all duration-700 ease-out delay-200"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">
                Explore my projects, skills, and experiences as a frontend
                developer. I'm passionate about creating beautiful and functional web applications that provide
                exceptional user experiences. Feel free to browse through my work and get in touch if you'd like to
                collaborate or learn more about my journey in the world of frontend development.</p>
            <RouterLink
                class=" border border-white text-white rounded-sm px-6 py-3 font-medium hover:bg-white hover:text-emerald-400 transition-all"
                to="/porto">Check this out!</RouterLink>
        </section>

        <section class=" w-full h-auto flex flex-col items-center justify-center py-20">
            <div class=" max-w-270 min-h-100 h-auto bg-zinc-950 border border-emerald-400 p-5 sm:p-10 mx-4 shadow-xl/50 shadow-emerald-400
            flex flex-col-reverse lg:flex-row items-center justify-center rounded-xl | transition-all duration-700 ease-out delay-500"
                :class="isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-24 opacity-0'">

                <div class=" w-full lg:w-1/2 h-full  flex flex-col mt-10 lg:mt-0">
                    <p class=" text-md text-white text-center lg:text-left mb-3">Become a partner</p>
                    <h1 class=" text-3xl text-white font-bold text-center lg:text-left mb-3">Make a Partnership</h1>
                    <p class=" text-lg text-white text-center lg:text-left mb-5">Interested in collaborating? Let's
                        discuss
                        how we can work together to bring your ideas to life.</p>
                    <RouterLink
                        class=" self-center lg:self-start mt-2 lg:mt-6 border border-emerald-400 text-emerald-400 rounded-sm px-6 py-3 font-medium hover:bg-emerald-400 hover:text-black hover:shadow-lg hover:shadow-emerald-400 transition-all"
                        to="/contact">Tell Me!</RouterLink>
                </div>
                <div class=" w-full lg:w-1/2 h-75 flex items-center justify-center">
                    <div class="w-full h-full max-w-100 shadow-lg shadow-emerald-400 rounded-2xl">
                        <GifSlideShow />
                    </div>
                </div>

            </div>
        </section>

    </main>
</template>