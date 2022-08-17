<template>
  <div class="layout">
    <div class="title">Main Path Analysis System</div>
    <div class="box">
      <div class="left">
        <div class="title1">Information display</div>
        <info-list></info-list>
      </div>
      <div class="right">
        <div class="title1">Main path map</div>
        <graph></graph>
      </div>
    </div>
  </div>
</template>

<script>
import graph from './graph.vue'
import infoList from './infoList.vue'

export default {
  name: "layout",
  data() {
    return {};
  },
  mounted() {},
  methods: {},
  components:{
    graph,infoList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.layout {
  height: 100vh;
  width: 100%;
  margin: 0 auto;
  background-color: rgb(241, 241, 241);
}

.title {
  height: 3%;
  color: black;
  text-shadow: 0 0 20px white;
  font-size: 22px;
  font-weight: bold;
  background-color: rgb(255, 255, 255);
  box-sizing: border-box;
  margin-left: 3px;
  margin-right: 3px;
  padding-bottom: 3px;
}
.title1 {
  height: 3.5%;
  font-weight: bold;
  color: black;
  text-shadow: 0 0 20px white;
  font-size: 20px;
  border-width: 3px;
  border-style: solid;
  border-color: rgb(255, 255, 255);
  background-color: rgb(230, 228, 228);
}
.box {
  display: flex;
  height: 95%;
}
.box .left {
  background-color: rgb(255, 255, 255);
  flex: 3;
  height: 100%;
  margin-top: 3px;
  margin-bottom: 3px;
  margin-left: 3px;
  margin-right: 3px;
}
.box .right {
  background-color: rgb(255, 255, 255);
  flex: 7;
  height: 100%;
  margin-top: 3px;
  margin-bottom: 3px;
  margin-left: 3px;
  margin-right: 3px;
}
</style>
