import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from "../views/Dashboard"
import Projects from  "../views/Projects"
import Team from "../views/Team"
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard
  },
    {
      path: '/projects',
      name: 'projects',
      component:Projects
    },
  {
    path: '/team',
    name: 'team',
    component: Team
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
