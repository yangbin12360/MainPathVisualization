<template>
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="id:">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="标题:">
            <span>{{ props.row.title }}</span>
          </el-form-item>
          <!-- <el-form-item label="摘要:">
            <span>{{ props.row.abstract }}</span>
          </el-form-item> -->
          <el-form-item label="申请人:">
            <span>{{ props.row.applicant}}</span>
          </el-form-item>
          <el-form-item label="IPC主分类:">
            <span>{{props.row.IPC }}</span>
          </el-form-item>
          <el-form-item label="CPC:">
            <span>{{ props.row.CPC }}</span>
          </el-form-item>
          <el-form-item label="引证次数:">
            <span>{{ props.row.citeNum }}</span>
          </el-form-item>
             <el-form-item label="被引证次数:">
            <span>{{ props.row.beCiteNum }}</span>
          </el-form-item>
             <el-form-item label="公开(公告)日:">
            <span>{{ props.row.time }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="专利 ID"
      prop="id">
    </el-table-column>
    <el-table-column
      label="专利标题"
      prop="title">
    </el-table-column>
    <!-- <el-table-column
      label="描述"
      prop="desc">
    </el-table-column> -->
  </el-table>
</template>

<script>
export default {
  name: "infoList",
  data() {
    return {
    tableData:[{
        id: null,
      title: null,
      abstract: null,
      applicant: null,
      time: null,
      CPC: null,
      IPC: null,
      citeNum: null,
      beCiteNum: null,
    }]
       
    };
  },
  watch:{
    "$store.state.id"(oldVal,newVal){
        this.tableData[0]["id"] = this.$store.state.id
        this.tableData[0]["title"] = this.$store.state.title
        this.tableData[0]["abstract"] = this.$store.state.abstract
        this.tableData[0]["applicant"] = this.$store.state.applicant
        this.tableData[0]["time"] = this.$store.state.time
        this.tableData[0]["CPC"] = this.$store.state.CPC
        this.tableData[0]["IPC"] = this.$store.state.IPC
        this.tableData[0]["citeNum"] = this.$store.state.citeNum
        this.tableData[0]["beCiteNum"] = this.$store.state.beCiteNum
    }
  },
  methods: {

  },
};
</script>
<style scoped>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
