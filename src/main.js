import { createApp } from 'vue';
import App from './App.vue';

import JsppUI from '@/libs/jspp-ui';

import router from './router'

import PerfectScrollbar from 'vue3-perfect-scrollbar'
import 'vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css'

createApp(App).use(JsppUI).use(router).use(PerfectScrollbar, {
    watchOptions: true,
    options: {
        suppressScrollY: true
    }
}).mount('#app');

