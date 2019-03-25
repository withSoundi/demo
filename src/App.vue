<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <myApp title="舆情分析报告"/>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import myApp from './components/myApp.vue'
// import test from './components/test.vue'

export default {
  name: 'app',
  components: {
    myApp,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
}
</style>
