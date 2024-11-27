import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LogIn.vue')
  },
  {
    path: '/signin',
    component: () => import('../views/SignIn.vue')
  },
  {
    path: '/analysis',
    component: () => import('../views/AnalysisPage.vue')
  },
  {
    path: '/request',
    component: () => import('../views/RequestPage.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
