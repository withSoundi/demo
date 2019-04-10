import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import echarts from 'echarts';
import App from './App.vue'
import VueRouter from 'vue-router';
import VCharts from 'v-charts';
import VueResource from 'vue-resource';
import axios from 'axios';
// import routeConfig from './router-config'

Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(VueRouter);
// Vue.component('v-chart', Echarts);
Vue.use(echarts);
Vue.use(VCharts);
Vue.use(VueRouter);
Vue.use(VueResource);
// Vue.use(axios);
Vue.prototype.$echarts = echarts;
Vue.prototype.axios = axios;

// const router = new VueRouter({
//   routes: routeConfig
// })

new Vue({
  // router,
  // store,
  render: h => h(App),
}).$mount('#app')
