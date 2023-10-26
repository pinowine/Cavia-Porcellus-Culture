import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import InnerHome from "@/views/InnerHome.vue";
import loginpage from "@/views/login.vue";

import a1 from "@/views/autumn-collection/1.vue"
import a2 from "@/views/autumn-collection/2.vue"
import a3 from "@/views/autumn-collection/3.vue"
import a4 from "@/views/autumn-collection/4.vue"
import a5 from "@/views/autumn-collection/5.vue"

const router = createRouter(
    {
        history: createWebHistory(),    
        routes: [
            { path: '/', component: Home},
            { path: '/inner', component: InnerHome},
            { path: "/loginpage", component: loginpage},
            { path: '/autumn-collection/1', component: a1},
            { path: '/autumn-collection/2', component: a2},
            { path: '/autumn-collection/3', component: a3},
            { path: '/autumn-collection/4', component: a4},
            { path: "/autumn-collection/5", component: a5},

        ]
    }
)

export default router;