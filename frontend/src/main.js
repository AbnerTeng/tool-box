import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './styles/global.css'
// import i18n from './lang'

// new Vue({
//     router,
//     i18n,
//     render: h => h(App)
// }).$mount('#app')
createApp(App).use(router).mount('#app')
