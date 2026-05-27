<script setup>
import { ref, computed } from 'vue'

const selectedYear = ref('All')

const experiences = [
    {
        year: '2025',
        title: 'Campus Committee',
        role: 'Member & Coordinator',
        desc: 'Serving as a member or coordinator of an organizing committee for events such as workshops, professional development sessions, organizational kickoffs, and leadership training for members',
        tech: ['Leadership', 'Event Management', 'Problem Solving']
    },
    {
        year: '2025',
        title: 'Himpunan Mahasiswa Informatika (HMIF) Amikom Yogyakarta',
        role: 'Public Relations Division',
        desc: 'Served as a member of a student organization from 2025 to 2027, progressing from the trainee level to the Public Relations division. Was responsible for social media and industry visits.',
        tech: ['Design', 'Industri', 'Management', 'Leader']
    },
    {
        year: '2022',
        title: 'Student Council',
        role: 'Secretary',
        desc: 'Served on the Student Council to organize various events and activities for high school students. Served as secretary in the organization’s core leadership',
        tech: ['Management', 'Correspondence', 'Event']
    },
]

const availableYears = ['All', ...[...new Set(experiences.map(e => e.year))].sort((a, b) => b - a)]

const filteredExperiences = computed(() => {
    let filtered = experiences

    if (selectedYear.value !== 'All') {
        filtered = experiences.filter(exp => exp.year === selectedYear.value)
    }

    return [...filtered].sort((a, b) => b.year - a.year)
})
</script>

<template>
    <div
        class="w-full h-auto pb-4 mb-6 flex flex-col sm:flex-row justify-center sm:justify-between items-center sm:items-end">
        <h1 class="text-5xl font-bold tracking-tighter text-zinc-200 mb-5 sm:mb-0">
            <span class="text-emerald-400">Experience</span> Log
        </h1>

        <div class="relative inline-block">
            <select v-model="selectedYear"
                class="w-40 h-10 bg-zinc-950 rounded-sm text-center text-white shadow-xl shadow-emerald-400/10 border-x-2 border-emerald-400 appearance-none select-none transition-all cursor-pointer font-normal focus:outline-none">
                <option v-for="year in availableYears" :key="year" :value="year">
                    {{ year === 'All' ? 'All' : year }}
                </option>
            </select>
        </div>
    </div>

    <transition-group name="timeline" tag="div" class="relative w-full">
        <div v-for="exp in filteredExperiences" :key="exp.title" class="mb-12 relative group">

            <div class="bg-zinc-900/50 border border-emerald-500/10 hover:border-emerald-500/40 p-6 rounded-xl shadow-lg backdrop-blur-sm transition-all
                hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(52,211,153,0.15)]">

                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-2 gap-2">
                    <h2
                        class="text-xl font-medium text-zinc-100 tracking-tight group-hover:text-emerald-400 transition-colors">
                        {{ exp.title }}
                    </h2>
                    <span
                        class="px-3 py-1 bg-emerald-950/50 text-emerald-400 text-xs font-mono font-medium rounded-full border border-emerald-500/20 shadow-inner">
                        {{ exp.year }}
                    </span>
                </div>

                <h3 class="text-emerald-400/80 text-sm font-medium mb-4">{{ exp.role }}</h3>
                <p class="text-zinc-400 text-sm leading-relaxed mb-6">{{ exp.desc }}</p>

                <div class="flex flex-wrap gap-2">
                    <span v-for="tech in exp.tech" :key="tech"
                        class="text-xs font-mono px-2 py-1 bg-zinc-950 text-zinc-500 border border-zinc-800 rounded shadow-sm">
                        {{ tech }}
                    </span>
                </div>

            </div>

        </div>
    </transition-group>
</template>

<style scoped>
.timeline-move,
.timeline-enter-active,
.timeline-leave-active {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.timeline-enter-from,
.timeline-leave-to {
    opacity: 0;
    transform: translateY(30px) scale(0.95);
}

.timeline-leave-active {
    position: absolute;
    width: calc(100% - 3rem);
}
</style>