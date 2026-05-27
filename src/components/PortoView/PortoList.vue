<script setup>
import { ref, computed } from 'vue'

const isModalOpen = ref(false)
const selectedProject = ref(null)

const projects = ref([
    {
        id: 1,
        title: 'Bunaya School',
        desc: 'A website for a school located in Bogor. Built using Vue and Tailwind, I created this as my personal project.',
        img: 'https://res.cloudinary.com/dg620epmv/image/upload/v1773416411/bunaya_xezki5.jpg',
        github: 'https://github.com/MehmedAzka/sdibunaya.git',
        year: '2022',
        tech: [
            'https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg',
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg'
        ],
        contributors: ['Moxka']
    },
    {
        id: 2,
        title: 'HealthScope',
        desc: 'A website for finding information about diseases and their symptoms. This website is perfect for those who want to learn about diseases without having to ask a doctor or someone else',
        img: 'https://res.cloudinary.com/dg620epmv/image/upload/v1773418295/noPreview_jaghr7.jpg',
        github: 'https://github.com/MehmedAzka/healthScope.git',
        year: '2021',
        tech: [
            'https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg',
            'https://upload.wikimedia.org/wikipedia/commons/5/5f/Html-1.svg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9f/CSS3_logo_square.svg',
            'https://upload.wikimedia.org/wikipedia/commons/3/3b/Javascript_Logo.png',
        ],
        contributors: ['Moxka', 'Al-banna11', 'mustafidh08']
    },
    {
        id: 3,
        title: "Portfolio Web Profile",
        desc: "This is a website showcasing my professional profile. Here, you can see the projects I’ve worked on, the technologies I’ve used, and my level of expertise in those areas.",
        img: "https://res.cloudinary.com/dg620epmv/image/upload/v1773419376/webPortfolio_irkzlp.jpg",
        github: "https://github.com/MehmedAzka/portfolio.git",
        year: "2026",
        tech: [
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg',
            "https://upload.wikimedia.org/wikipedia/commons/f/fd/Firebase_Logo_%28No_wordmark%29_%282024-%29.svg"
        ],
        contributors: ['Moxka']
    },
    {
        id: 4,
        title: "Qarnayn Picture Profile",
        desc: "This is a profile website designed to introduce a startup called “Qarnayn Picture.” The website is already hosted and has its own domain. You can visit it at qarnaynpicture.com",
        img: "https://res.cloudinary.com/dg620epmv/image/upload/v1779862252/cbd1be52-ed6a-4da5-9431-2a1fcc909b69.png",
        github: "https://github.com/MehmedAzka/qarnaynPicture.git",
        year: "2026",
        tech: [
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg'
        ],
        contributors: ['Moxka']
    }
])

const selectedYear = ref('All')

const availableYears = computed(() => {
    const years = [...new Set(projects.value.map(p => p.year))].sort((a, b) => b - a)
    return ['All', ...years]
})

const filteredProjects = computed(() => {
    let filtered = projects.value
    if (selectedYear.value !== 'All') {
        filtered = projects.value.filter(p => p.year === selectedYear.value)
    }
    return [...filtered].sort((a, b) => b.year - a.year)
})

const openModal = (project) => {
    selectedProject.value = project
    isModalOpen.value = true
}

const closeModal = () => {
    isModalOpen.value = false
    setTimeout(() => { selectedProject.value = null }, 300)
}
</script>

<template>

    <div
        class="w-full h-auto pb-4 mb-6 flex flex-col sm:flex-row justify-center sm:justify-between items-center sm:items-end">
        <div>
            <h1 class="text-5xl font-bold tracking-tighter text-zinc-200 mb-5 sm:mb-0">
                <span class="text-emerald-400">My </span>Project.
            </h1>
        </div>

        <div class="relative inline-block">
            <select v-model="selectedYear"
                class="w-40 h-10 bg-zinc-950 rounded-sm text-center text-white shadow-xl shadow-emerald-400/10 border-x-2 border-emerald-400 appearance-none select-none transition-all cursor-pointer font-normal focus:outline-none">
                <option v-for="year in availableYears" :key="year" :value="year">
                    {{ year === 'All' ? 'All' : year }}
                </option>
            </select>
        </div>
    </div>

    <div class=" flex items-center">

        <transition-group name="porto" tag="div" class=" w-full grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

            <div v-for="project in filteredProjects" :key="project.id" @click="openModal(project)"
                class=" max-w-103 cursor-pointer group relative overflow-hidden bg-zinc-900 border border-emerald-500/20 rounded-xl shadow-lg 
                    hover:border-emerald-400 hover:shadow-[0_0_20px_rgba(52,211,153,0.2)] transition-all flex flex-col min-h-62.5">

                <div class="h-40 w-full overflow-hidden shrink-0">
                    <img :src="project.img"
                        class="w-full h-full object-cover transition-transform duration-500 grayscale group-hover:grayscale-0 opacity-70 group-hover:opacity-100"
                        alt="Project Thumbnail">
                </div>

                <div class="p-4 flex flex-col flex-1">
                    <div class="flex justify-between items-start mb-2 gap-2">
                        <h2
                            class="text-lg font-semibold text-zinc-100 group-hover:text-emerald-400 line-clamp-1 transition-colors">
                            {{ project.title }}
                        </h2>
                        <span class="text-emerald-400 font-mono text-xs">{{ project.year }}</span>
                    </div>
                    <p class="text-zinc-400 text-sm line-clamp-2">{{ project.desc }}</p>
                </div>

            </div>

        </transition-group>
    </div>

    <Teleport to="body">
        <transition name="fade">
            <div v-if="isModalOpen" @click.self="closeModal"
                class="fixed inset-0 z-100 flex items-center justify-center bg-black/80 backdrop-blur-md p-4 sm:p-0">

                <div
                    class="w-full max-w-3xl bg-zinc-950 border border-emerald-500/50 rounded-md shadow-[0_0_50px_rgba(16,185,129,0.2)] overflow-hidden relative flex flex-col max-h-[90vh]">

                    <button @click="closeModal" class="absolute top-4 right-4 z-10 w-8 h-8 flex items-center justify-center bg-black/50 text-zinc-400 hover:text-emerald-400 rounded-full 
                            border border-zinc-700 hover:border-emerald-400 transition-all backdrop-blur-sm">✕</button>

                    <div class="w-full h-58 sm:h-94 relative border-b border-zinc-800 shrink-0">
                        <img :src="selectedProject.img" class="w-full h-full object-contain" alt="Detail Image">
                        <div class="absolute inset-0 bg-linear-to-t from-zinc-950 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 pr-6">
                            <span
                                class="inline-block px-3 py-1 bg-emerald-400 text-black font-mono text-xs font-bold rounded-full mb-2">
                                {{ selectedProject.year }}
                            </span>
                            <h2 class="text-3xl font-semibold text-zinc-100 tracking-tight drop-shadow-lg">
                                {{ selectedProject.title }}
                            </h2>
                        </div>
                    </div>

                    <div class="p-6 overflow-y-auto custom-scrollbar flex flex-col gap-6">
                        <div>
                            <h3 class="text-emerald-400 font-mono text-xs uppercase tracking-widest mb-2">
                                Description</h3>
                            <p class="text-zinc-300 leading-relaxed">{{ selectedProject.desc }}</p>
                        </div>

                        <div>
                            <h3 class="text-emerald-400 font-mono text-xs uppercase tracking-widest mb-2">Tech Stack
                            </h3>
                            <div class="flex flex-wrap gap-3">
                                <img v-for="(logo, index) in selectedProject.tech" :key="index" :src="logo"
                                    draggable="false"
                                    class="w-8 h-8 object-contain drop-shadow-[0_0_5px_rgba(255,255,255,0.2)]">
                            </div>
                        </div>

                        <div>
                            <h3 class="text-emerald-400 font-mono text-xs uppercase tracking-widest mb-2">
                                Contributors</h3>
                            <div class="flex flex-wrap gap-2">
                                <span v-for="(email, idx) in selectedProject.contributors" :key="idx"
                                    class="px-3 py-1 bg-zinc-900 border border-zinc-700 text-zinc-400 text-sm font-mono rounded-md">
                                    {{ email }}
                                </span>
                            </div>
                        </div>

                        <div class="pt-4 mt-auto border-t border-zinc-800">
                            <a :href="selectedProject.github" target="_blank"
                                class="inline-flex items-center bg-zinc-200 text-black hover:bg-emerald-400 px-4 py-2 rounded-sm font-normal transition-colors">
                                View on GitHub
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </Teleport>
</template>

<style scoped>
.porto-move,
.porto-enter-active,
.porto-leave-active {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.porto-enter-from,
.porto-leave-to {
    opacity: 0;
    transform: scale(0.9);
}

.porto-leave-active {
    position: absolute;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: scale(0.95);
}

.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background-color: #3f3f46;
    border-radius: 20px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background-color: #10b981;
}
</style>