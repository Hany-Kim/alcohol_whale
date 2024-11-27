import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import router from './router'

createApp(App).use(router).use(Quasar, quasarUserOptions).use(store).mount('#app')
