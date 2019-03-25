<template>
  <div class="myApp">
    <el-row>
      <el-col :span="4">
        <el-col :offset="8"><el-button type="primary" plain>事件简介</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>事件走势</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>网站统计</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>数据类型</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>关键词云</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>热门信息</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>热点网民</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>传播路径</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>相关词语</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>网民观点</el-button></el-col>
        <el-col :offset="8"><el-button type="primary" plain>舆论总结</el-button></el-col>
      </el-col>
      <el-col :span="16" class="content">
        <h1>{{ title }}</h1>
        <div class="textShow">
          <div class="smallTitle">
            <h2>事件简介</h2>
          </div>
          <div class="introduce">
            "本报告围绕关键词“问题隧道|16亿扶贫路|考勒隧道|折达公路|((甘肃+(质量问题|整改|曝光|刷涂料|偷工减料)+隧道))”，对2018/04/01 00:00~2018/04/09 23:59期间，互联网上采集到的179457条信息进行了深入分析。全网声量最高峰出现在2018/04/02 00:00:00，共产生108555篇相关讯息；事件源头于2018/04/01 00:48分发布在微信上，题名为『：怒！钢筋双层变单层，“整改”只是刷涂料，...』。后续报道主要来源于: 新浪微博、微信、人民政协报、搜狐网等几大站点。总体来说，整个事件的发展趋势较为突出，详细报告如下。"
          </div>
        </div>
        <div class="textShow">
          <div class="smallTitle">
            <h2>事件走势</h2>
          </div>
          <div class="block">
            <el-timeline>
              <el-timeline-item
                v-for="(trendItem, index) in trend"
                :key="index"
                :timestamp="trendItem.timestamp">
                {{ trendItem.trendContent}}
              </el-timeline-item>
            </el-timeline>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>网站统计</h2>
            </div>
            <div>
              <!-- <div class=""></div> -->
              <!-- <h2 id="bar">
                <a href="#bar">Bar chart <small>(with async data &amp; custom theme)</small></a>
                <button :class="{
                  round: true,
                  expand: expand.bar
                }" @click="expand.bar = !expand.bar" aria-label="toggle"></button>
              </h2>
              <section v-if="expand.bar">
                <figure>
                  <chart
                    :options="bar"
                    :init-options="initOptions"
                    ref="bar"
                    theme="ovilia-green"
                    autoresize
                  />
                </figure>
                <p v-if="seconds <= 0"><small>Loaded.</small></p>
                <p v-else><small>Data coming in <b>{{ seconds }}</b> second{{ seconds > 1 ? 's' : '' }}...</small></p>
                <p><button @click="refresh" :disabled="seconds > 0">Refresh</button></p>
              </section> -->
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>数据类型</h2>
            </div>
            <div>
              <li class="dataList">
                
              </li>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>关键词云</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>热门信息</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>热点网民</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>传播路径</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>相关词语</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>网民观点</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>舆论总结</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'myApp',
  components: {
    // chart: Echarts
  },
  props: {
    title: String,
    description: String,
  },
  data() {
    // let options = qs.parse(location.search, { ignoreQueryPrefix: true })
    return {
      trend: [{
        trendContent: '【#16亿扶贫路偷工减料# 整改就是刷遍涂料？[怒]】国家投资近16亿的甘肃扶贫路，竟遭偷工减料！双层钢筋变单层，路基裂缝随处可见！隧道上方是大山，隐患不堪设想！整改就是刷了遍涂料…甘肃公路管理局副处长杨爱明称，我没空上去看去…甘肃交通运输厅领导不见记者，想待着就待着，不想待着就走”？！[微信]',
        timestamp: '2019-03-20 10:00'
      }, {
        trendContent: '怒！钢筋双层变单层，“整改”只是刷涂料，这就是16亿建成的“扶贫路”？！[微信]',
        timestamp: '2019-03-20 10:00'
      }]
    }
  },
  mounted: function() {
    let that = this;
    let myChart = this.$echarts.init(document.getElementById('myChart'));
    that.myChart = myChart;
    that.initCharts();
    // let dataChart1 = this.$echarts.init(document.getElementById('dataChart1'));
    // let dataChart2 = this.$echarts.init(document.getElementById('dataChart2'));
    // let dataChart3 = this.$echarts.init(document.getElementById('dataChart3'));
    // let dataChart4 = this.$echarts.init(document.getElementById('dataChart4'));
    // that.myChart.on('legendselectchanged', function (params) {
        // 获取点击图例的选中状态
        // let isSelected = params.selected[params.name];
        // that.selected = params.selected;
        // 在控制台中打印
        // console.log((isSelected ? '选中了' : '取消选中了') + '图例' + params.name);
        // 打印所有图例的状态
        // console.log(params.selected);
    // });
  },
  methods: {
    initCharts: function() {
      let option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一','周二','周三','周四','周五','周六','周日']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'邮件营销',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'联盟广告',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'视频广告',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'直接访问',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'搜索引擎',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};
      this.myChart.setOption(option);
    }
  }
}
</script>

<style scoped>
.textShow {
  text-align: left
}
.content {
  /* border: 2px #b5d6fc solid; */
  padding: 10px 50px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
}
.dataList {
  float: left;
  list-style: none;
}
/* .smallTitle {
  
  padding: 0px
} */
h2 {
  border-bottom: 3px #eee solid;
  margin: 15px 0px;
}
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
