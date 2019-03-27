import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import echarts from 'echarts';
import App from './App.vue'
import VueRouter from 'vue-router';
import VCharts from 'v-charts'

Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(VueRouter);
// Vue.component('v-chart', Echarts);
Vue.use(echarts);
Vue.use(VCharts);
Vue.prototype.$echarts = echarts;

new Vue({
  render: h => h(App),
}).$mount('#app')
