<template>
  <div class="myApp">
    <el-row>
      <el-col :span="4" class="pilot" :offset="1">
        <a href="#01"><el-col><el-button type="primary" plain>事件简介</el-button></el-col></a>
        <a href="#02"><el-col><el-button type="primary" plain>事件走势</el-button></el-col></a>
        <a href="#03"><el-col><el-button type="primary" plain>网站统计</el-button></el-col></a>
        <a href="#04"><el-col><el-button type="primary" plain>数据类型</el-button></el-col></a>
        <a href="#05"><el-col><el-button type="primary" plain>关键词云</el-button></el-col></a>
        <a href="#06"><el-col><el-button type="primary" plain>热门信息</el-button></el-col></a>
        <a href="#07"><el-col><el-button type="primary" plain>热点网民</el-button></el-col></a>
        <!-- <a href="#08"><el-col><el-button type="primary" plain>传播路径</el-button></el-col></a> -->
        <a href="#09"><el-col><el-button type="primary" plain>网民观点</el-button></el-col></a>
        <a href="#10"><el-col><el-button type="primary" plain>舆论总结</el-button></el-col></a>
      </el-col>
      <el-col :span="16" class="content" :offset="4">
        <h1>{{ title }}</h1>
        <div class="textShow" id="01">
          <!-- <el-step v-for="(item, index) in steps.step"
                    :key="item.ti"></el-step> -->
          <div class="smallTitle">
            <h2>事件简介</h2>
          </div>
          <div class="introduce">
            {{ results.content }}
          </div>
        </div>
        <div class="textShow" id="02">
          <div class="smallTitle">
            <h2>事件走势</h2>
          </div>
          <div class="block">
            <el-timeline>
              <el-timeline-item
                v-for="(trendItem, index) in results.trend"
                :key="index"
                :timestamp="trendItem.timestamp">
                {{ trendItem.trendContent }}
                <!-- {{ trendItem }} -->
              </el-timeline-item>
            </el-timeline>
          </div>
          <div class="textShow" id="03">
            <div class="smallTitle">
              <h2>网站统计</h2>
            </div>
            <div :style="{width: '800px', height: '390px'}">
              <ve-line :data="results.chartData"></ve-line>
              <!-- <div id="myChart" :style="{width: '1000px', height: '300px'}"></div> -->
            </div>
          </div>
          <div class="textShow" id="04">
            <div class="smallTitle">
              <h2>数据类型</h2>
            </div>
            <div>
              <el-row>
                <el-col :span="10" :offset="1">
                  <div :style="{width: '300px', height: '450px'}">
                    <h3>情感分析</h3>
                    <ve-ring :data="results.typeData1"></ve-ring>
                  </div>
                </el-col>
                <el-col :span="10" :offset="2">
                  <div :style="{width: '300px', height: '450px'}">
                    <h3>境内外分布</h3>
                    <ve-ring :data="results.typeData2"></ve-ring>
                  </div>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="10" :offset="1">
                  <div :style="{width: '300px', height: '450px'}">
                    <h3>媒体来源占比</h3>
                    <ve-pie :data="results.typeData3"></ve-pie>
                  </div>
                </el-col>
                <el-col :span="10" :offset="2">
                  <div :style="{width: '300px', height: '450px'}">
                    <h3>媒体活跃度</h3>
                    <ve-histogram :data="results.typeData4"></ve-histogram>
                  </div>
                </el-col>
              </el-row>
              <h3>地域分析</h3>
              <el-col :offset="4">
                <div><ve-map :data="results.mapData" :style="{width: '500px', height: '350px'}"></ve-map></div>
              </el-col>
              <el-row></el-row>
            </div>
          </div>
          <div class="textShow" id="05">
            <div class="smallTitle">
              <h2>关键词云</h2>
            </div>
            <div>
              <div><ve-wordcloud :data="results.wordData"></ve-wordcloud></div>
            </div>
          </div>
          <div class="textShow" id="06">
            <div class="smallTitle">
              <h2>热门信息</h2>
            </div>
            <div>
              <div class="hotMessage">
                <el-table :data="results.popular" style="width: 100%">
                  <el-table-column prop="hotTitle" label="标题" width="450"></el-table-column>
                  <el-table-column prop="hotSource" label="来源" width="130"></el-table-column>
                  <el-table-column prop="hotTime" label="时间" width="140"></el-table-column>
                  <el-table-column prop="hotNumber" label="转发数" width="120"></el-table-column>
                </el-table>
              </div>
            </div>
          </div>
          <div class="textShow" id="07">
            <div class="smallTitle">
              <h2>热点网民</h2>
            </div>
            <div>
              <el-tabs v-model="activeName" @tab-click="handleClick">
                <el-tab-pane label="全部" name="first">
                  全部
                </el-tab-pane>
                <el-tab-pane label="微博" name="second">
                  微博
                </el-tab-pane>
                <el-tab-pane label="论坛" name="third">
                  论坛
                </el-tab-pane>
                <el-tab-pane label="博客" name="fourth">
                  博客
                </el-tab-pane>
              </el-tabs>
            </div>
          </div>
          <!-- <div class="textShow" id="08">
            <div class="smallTitle">
              <h2>传播路径</h2>
            </div>
            <div>
              <div><ve-tree :data="results.treeData"></ve-tree></div>
            </div>
          </div> -->
          <!-- <div class="textShow">
            <div class="smallTitle">
              <h2>相关词语</h2>
            </div>
            <div>
              <div></div>
            </div>
          </div> -->
          <div class="textShow" id="09">
            <div class="smallTitle">
              <h2>网民观点</h2>
            </div>
            <div>
              <h3>新闻观点</h3>
              <div><ve-bar :data="results.newsPoint"></ve-bar></div>
              <h3>微博观点</h3>
              <div><ve-bar :data="results.weiboPoint"></ve-bar></div>
              <h3>网民观点</h3>
              <div><ve-pie :data="results.forumPoint"></ve-pie></div>
            </div>
          </div>
          <div class="textShow" id="10">
            <div class="smallTitle">
              <h2>舆论总结</h2>
            </div>
            <div>
              <div>{{ results.summary }}</div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// const treeData = {
//   name: 'f',
//   value: 1,
//   link: 'https://ele.me',
//   children: [
//     {
//       name: 'a',
//       value: 1,
//       link: 'https://ele.me',
//       children: [
//         {
//           name: 'a-a',
//           link: 'https://ele.me',
//           value: 2
//         },
//         {
//           name: 'a-b',
//           link: 'https://ele.me',
//           value: 2
//         }
//       ]
//     },
//     {
//       name: 'b',
//       value: 1,
//       link: 'https://ele.me',
//       children: [
//         {
//           name: 'b-a',
//           link: 'https://ele.me',
//           value: 2
//         },
//         {
//           name: 'b-b',
//           link: 'https://ele.me',
//           value: 2
//         }
//       ]
//     },
//     {
//       name: 'c',
//       value: 3,
//       link: 'https://ele.me',
//       children: [
//         {
//           name: 'c-a',
//           link: 'https://ele.me',
//           value: 4
//         },
//         {
//           name: 'c-b',
//           link: 'https://ele.me',
//           value: 2
//         }
//       ]
//     },
//     {
//       name: 'd',
//       value: 3,
//       link: 'https://ele.me',
//       children: [
//         {
//           name: 'd-a',
//           link: 'https://ele.me',
//           value: 4
//         },
//         {
//           name: 'd-b',
//           link: 'https://ele.me',
//           value: 2
//         }
//       ]
//     }
//   ]
// }
export default {
  name: 'myApp',
  props: {
    title: String,
    description: String,
  },
  data() {
    return {
      results: [{
        content: null
      },{
        trend: null
      },{
        chartData: null
      },{
        typeData1: null
      },{
        typeData2: null
      },{
        typeData3: null
      },{
        typeData4: null
      },{
        mapData: null
      },{
        wordData: null
      },{
        tableData: null
      },{
        treeData: null
      },{
        newaPoint: null
      },{
        weiboPoint: null
      },{
        forumPoint: null
      }]
    }
  },
  mounted() {
    this.axios
      .get('http://127.0.0.1:8000/query/?name=haojin')
      .then(response => (
        this.results = response.data
      ))
  },
  // data() {
  //   return {
  //     wordData: {
  //         columns: ['word', 'count'],
  //         rows: getRows()
  //     },
  //     treeData: {
  //       columns: ['name', 'value'],
  //       rows: [
  //         {
  //           name: 'tree1',
  //           value: [treeData]
  //         }
  //       ]
  //     },
  //     viewData: {
  //       columns: ['日期', '访问用户', '下单用户', '下单率'],
  //       rows: [
  //         { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
  //         { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
  //         { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
  //         { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
  //         { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
  //         { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
  //       ]
  //     },
  //     newsPoint: {

  //     },
  //     forumpoint: {

  //     },
  //     weibopoint: {

  //     },
  //     activeName: 'first',
  //     summary: 'test'
  //   }
  // },
}
// function getRows () {
//   return [{
//     'word': 'visualMap',
//     'count': 22199
//   }, {
//     'word': 'continuous',
//     'count': 10288
//   }, {
//     'word': 'contoller',
//     'count': 620
//   }, {
//     'word': 'series',
//     'count': 274470
//   }, {
//     'word': 'gauge',
//     'count': 12311
//   }, {
//     'word': 'detail',
//     'count': 1206
//   }, {
//     'word': 'piecewise',
//     'count': 4885
//   }, {
//     'word': 'textStyle',
//     'count': 32294
//   }, {
//     'word': 'markPoint',
//     'count': 18574
//   }, {
//     'word': 'pie',
//     'count': 38929
//   }, {
//     'word': 'roseType',
//     'count': 969
//   }, {
//     'word': 'label',
//     'count': 37517
//   }, {
//     'word': 'emphasis',
//     'count': 12053
//   }, {
//     'word': 'yAxis',
//     'count': 57299
//   }, {
//     'word': 'name',
//     'count': 15418
//   }, {
//     'word': 'type',
//     'count': 22905
//   }, {
//     'word': 'gridIndex',
//     'count': 5146
//   }, {
//     'word': 'normal',
//     'count': 49487
//   }, {
//     'word': 'itemStyle',
//     'count': 33837
//   }, {
//     'word': 'min',
//     'count': 4500
//   }, {
//     'word': 'silent',
//     'count': 5744
//   }, {
//     'word': 'animation',
//     'count': 4840
//   }, {
//     'word': 'offsetCenter',
//     'count': 232
//   }, {
//     'word': 'inverse',
//     'count': 3706
//   }, {
//     'word': 'borderColor',
//     'count': 4812
//   }, {
//     'word': 'markLine',
//     'count': 16578
//   }, {
//     'word': 'line',
//     'count': 76970
//   }, {
//     'word': 'radiusAxis',
//     'count': 6704
//   }, {
//     'word': 'radar',
//     'count': 15964
//   }, {
//     'word': 'data',
//     'count': 60679
//   }, {
//     'word': 'dataZoom',
//     'count': 24347
//   }, {
//     'word': 'tooltip',
//     'count': 43420
//   }, {
//     'word': 'toolbox',
//     'count': 25222
//   }, {
//     'word': 'geo',
//     'count': 16904
//   }, {
//     'word': 'parallelAxis',
//     'count': 4029
//   }]
// }
</script>

<style scoped>
.textShow {
  text-align: left
}
.content {
  padding: 10px 50px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
}
.dataList {
  float: left;
  list-style: none;
}
.pilot {
  position: fixed;
  top: 30px;
  z-index: 0;
  min-width: 100px;
}
h2 {
  border-bottom: 3px #eee solid;
  margin: 15px 0px;
}
a {
  color: #51A8DD;
  text-decoration : none
}
a:hover {
  color: #eee;
}
</style>
