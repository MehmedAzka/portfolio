import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import PortoView from '../views/PortoView.vue'
import ContactView from '../views/ContactView.vue'
import { patchProp } from 'vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: '/porto',
        name: 'portofolio',
        component: PortoView
    },
    {
        path: "/contact",
        name: "contact",
        component: ContactView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }

    if (to.hash) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            el: to.hash,
            behavior: 'smooth',
          })
        }, 100)
      })
    }
    return { top: 0, behavior: 'smooth' }
  }
})

export default router