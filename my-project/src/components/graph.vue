<template>
  <div>
    <!-- <div class="controlBar">1</div>
     -->

    <div class="container">
      <div class="block">
        <span class="demonstration"></span>
        <el-date-picker
          v-model="start"
          type="year"
          placeholder="起始年1"
          value-format="yyyy"
        >
        </el-date-picker>
      </div>
      <div class="block">
        <span class="demonstration"></span>
        <el-date-picker
          v-model="end"
          type="year"
          placeholder="截止年"
          value-format="yyyy"
          @change="dateChoose"
        >
        </el-date-picker>
      </div>
      <el-input class="block" v-model="input" placeholder="请输入直径" style="width:15%;"></el-input>
      <el-button type="primary" @click="upload">生成<i class="el-icon-upload el-icon--right"></i></el-button>
    </div>
    <div id="graph"></div>
  </div>
</template>

<script>
import ForceGraph from "force-graph";

export default {
  name: "graph",
  data() {
    return {
      start: "",
      end: "",
      input:"",
      serverResponse: "res_test",
    };
  },
  mounted() {
    this.try();
  },
  methods: {
    async getData(s, e, d) {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = "http://127.0.0.1:5000/test";
      let data = await this.$axios.post(path, {
        startY: s,
        endY: e,
        diameter:d
      });
      console.log(data);
      return data;
    },

    try(res) {
      let tempData = res.data;
      // let startT = parseInt(stratYear);
      // let endT = parseInt(endYear);
      // let slideW = endT - startT + 1;
      // this.$axios.get("/static/" + stratYear + ".json").then((res) => {
      //   console.log(res.data);
      //   tempData = res.data;
      // });
      // for (let j = 1; j < slideW; j++) {
      //   let year = startT + j;
      //   console.log(year);
      //   year = year.toString();
      //   this.$axios.get("/static/" + year + ".json").then((res) => {
      //     console.log(res.data);
      //     // 边集
      //     for (let i = 0; i < res.data.links.length; i++) {
      //       tempData.links.push(res.data.links[i]);
      //     }
      //     // 点集
      //     for (let i = 0; i < res.data.nodes.length; i++) {
      //       tempData.nodes.push(res.data.nodes[i]);
      //     }
      //   });
      // }
      const width = document.getElementById("graph").offsetWidth
      const height = document.getElementById("graph").offsetHeight
      const Graph = ForceGraph()(document.getElementById("graph"))
        .linkDirectionalParticles(2)
        .width(width)
        .height(height)
        .graphData(tempData)
        .onNodeClick((node) =>{
          this.$store.state.id=node["id"]
          this.$store.state.title=node["标题"]
          this.$store.state.abstract=node["摘要"]
          this.$store.state.applicant=node["申请人"]
          this.$store.state.time=node["公开（公告）日"]
          this.$store.state.CPC=node["CPC"]
          this.$store.state.IPC=node["IPC主分类"]
          this.$store.state.citeNum=node["引证次数"]
          this.$store.state.beCiteNum=node["被引证次数"]
        })

      // setTimeout(() => {
      //   console.log(tempData);
      //   const Graph = ForceGraph()(document.getElementById("graph"))
      //     .linkDirectionalParticles(2)
      //     .graphData(tempData);
      // }, 1000);
    },

    async dateChoose() {
      // this.data = await this.getData(this.start, this.end);
      // console.log(this.data);
      // console.log(typeof(parseInt(this.end)))
      // if (this.end - this.start < 0) {
      //   alert("截止年不能小于起始年");
      // }else if(parseInt(this.end)>2021 || parseInt(this.start)<2002){
      //   alert("起始年最少为2002或截止年最多为2021")
      // }
      // else {
      //   this.try(this.data);
      // }
    },
    async upload(){
      this.data = await this.getData(this.start, this.end,this.input);
      console.log(this.data);
      console.log(typeof(parseInt(this.end)))
      if (this.end - this.start < 0) {
        alert("截止年不能小于起始年");
      }else if(parseInt(this.end)>2021 || parseInt(this.start)<2002){
        alert("起始年最少为2002或截止年最多为2021")
      }
      else {
        this.try(this.data);
      }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  display: flex;
  justify-content: left;
}
.container .block {
  padding-right: 15px;
  padding-left: 5px;
}
#graph {
  width: 100%;
  height: 87vh;
  overflow: hidden;
}
</style>
