import Vue from 'vue'
import App from './App.vue'
import store from './store'
import axios from "axios"


Vue.config.productionTip = false
var $https = axios.create({
  baseURL: "/api",
  timeout: '3000'
})

Vue.prototype.$https = $https;

new Vue({
  store,
  axios,
  render: h => h(App)
}).$mount('#app')

