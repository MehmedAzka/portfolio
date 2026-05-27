<script setup>
import TodaysWords from './TodaysWords.vue';
</script>

<template>
    <footer class=" w-full min-h-100 h-auto flex flex-col justify-around p-7 xl:p-10 shadow-2xl shadow-emerald-400">

        <div class=" w-full h-full grid grid-cols-none sm:grid-cols-4 grid-rows-4 sm:grid-rows-2 gap-5">
            <div class=" sm:row-span-2">
                <div class="text-xl font-bold tracking-tighter">
                    LOGO<span class="text-emerald-400">.</span>
                </div>
            </div>
            <div class=" grid grid-rows-2 grid-cols-2 lg:grid-cols-3 gap-5
            sm:col-span-2 row-span-2">

                <div class=" flex flex-col gap-2">
                    <h1 class=" text-emerald-400 text-md font-normal mb-1">Guides</h1>
                    <p class=" text-md font-normal">Privacy Policy</p>
                    <p class=" text-md font-normal">Terms of Service</p>
                    <p class=" text-md font-normal">Cookie Policy</p>
                </div>
                <div class=" flex flex-col gap-2">
                    <h1 class=" text-emerald-400 text-md font-normal mb-1">Features</h1>
                    <p class=" text-md font-normal">Blog</p>
                    <p class=" text-md font-normal">Help Center</p>
                    <p class=" text-md font-normal">Contact Support</p>
                </div>
                <div class=" flex flex-col gap-2">
                    <h1 class=" text-emerald-400 text-md font-normal mb-1">Profile</h1>
                    <p class=" text-md font-normal">About Us</p>
                    <p class=" text-md font-normal">Careers</p>
                    <p class=" text-md font-normal">Portfolio</p>
                </div>

            </div>
            <div class=" pt-5 sm:pt-0">
                <p class=" text-sm font-normal text-gray-700 mt-2">Have a nice day!!</p>
            </div>
            <div class=" flex flex-row justify-start sm:justify-end items-start sm:items-end">

                <div class=" flex flex-row">
                    <a href="https://instagram.com/mhmdzkaa._" class=" w-10 h-10 border border-emerald-400 rounded-sm shadow-xl/50 hover:shadow-emerald-400 transition-all mx-1
                    flex items-center justify-center">
                        <img class=" w-5 h-5 colored-png" src="./../assets/logos/instagram.svg" alt="">
                    </a>
                    <a href="https://github.com/MehmedAzka" class=" w-10 h-10 border border-emerald-400 rounded-sm shadow-xl/50 hover:shadow-emerald-400 transition-all mx-1
                    flex items-center justify-center">
                        <img class=" w-5 h-5 colored-png" src="./../assets/logos/github.svg" alt="">
                    </a>
                    <a href="#" class=" w-10 h-10 border border-emerald-400 rounded-sm shadow-xl/50 hover:shadow-emerald-400 transition-all mx-1
                    flex items-center justify-center">
                        <img class=" w-5 h-5 colored-png" src="./../assets/logos/linkedin.svg" alt="">
                    </a>
                    <a href="#" class=" w-10 h-10 border border-emerald-400 rounded-sm shadow-xl/50 hover:shadow-emerald-400 transition-all mx-1
                    flex items-center justify-center">
                        <img class=" w-5 h-5 colored-png" src="./../assets/logos/link.svg" alt="">
                    </a>
                </div>
            </div>
        </div>

        <div class=" w-full h-10 mt-5 sm:mt-0 flex flex-row justify-between items-end sm:items-center">
            <p class=" text-center text-sm text-gray-600">&copy; 2026 Moxka. All rights reserved.</p>
            <p class=" text-center text-sm text-gray-600">Contact Me!</p>
        </div>

    </footer>
</template>