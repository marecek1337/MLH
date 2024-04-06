<template>
      <router-link to="/">login</router-link> 
      <router-link to="/linkOfAssignments">list</router-link>
      <router-link to="/assignemntPreview">preview</router-link>
  <router-view />

</template>

<script>


export default {
  name: 'App',
  components: {
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
