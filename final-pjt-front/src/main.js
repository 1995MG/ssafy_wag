import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';
import VueFilterDateParse from '@vuejs-community/vue-filter-date-parse';


Vue.config.productionTip = false
Vue.use(VueFilterDateFormat);
Vue.use(VueFilterDateParse);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
