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
            <div :style="{width: '800px', height: '390px'}">
              <ve-line :data="chartData"></ve-line>
              <!-- <div id="myChart" :style="{width: '1000px', height: '300px'}"></div> -->
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>数据类型</h2>
            </div>
            <div>
              <el-row>
                <el-col :span="12">
                  <div :style="{width: '300px', height: '350px'}">
                    <ve-ring :data="typeData1"></ve-ring>
                  </div>
                </el-col>
                <el-col :span="12">
                  <div :style="{width: '300px', height: '350px'}">
                    <ve-ring :data="typeData1"></ve-ring>
                  </div>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="12">
                  <div :style="{width: '300px', height: '350px'}">
                    <ve-pie :data="typeData3" :settings="chartSettings"></ve-pie>
                  </div>
                </el-col>
                <el-col :span="12">
                  <div :style="{width: '300px', height: '350px'}">
                    <ve-histogram :data="typeData4"></ve-histogram>
                  </div>
                </el-col>
              </el-row>
              <h3>地域分析</h3>
              <div><ve-map :data="mapData"></ve-map></div>
              <el-row></el-row>
            </div>
          </div>
          <div class="textShow">
            <div class="smallTitle">
              <h2>关键词云</h2>
            </div>
            <div>
              <div><ve-wordcloud :data="wordData"></ve-wordcloud></div>
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
              <div><ve-tree :data="treeData"></ve-tree></div>
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
const treeData = {
  name: 'f',
  value: 1,
  link: 'https://ele.me',
  children: [
    {
      name: 'a',
      value: 1,
      link: 'https://ele.me',
      children: [
        {
          name: 'a-a',
          link: 'https://ele.me',
          value: 2
        },
        {
          name: 'a-b',
          link: 'https://ele.me',
          value: 2
        }
      ]
    },
    {
      name: 'b',
      value: 1,
      link: 'https://ele.me',
      children: [
        {
          name: 'b-a',
          link: 'https://ele.me',
          value: 2
        },
        {
          name: 'b-b',
          link: 'https://ele.me',
          value: 2
        }
      ]
    },
    {
      name: 'c',
      value: 3,
      link: 'https://ele.me',
      children: [
        {
          name: 'c-a',
          link: 'https://ele.me',
          value: 4
        },
        {
          name: 'c-b',
          link: 'https://ele.me',
          value: 2
        }
      ]
    },
    {
      name: 'd',
      value: 3,
      link: 'https://ele.me',
      children: [
        {
          name: 'd-a',
          link: 'https://ele.me',
          value: 4
        },
        {
          name: 'd-b',
          link: 'https://ele.me',
          value: 2
        }
      ]
    }
  ]
}
export default {
  name: 'myApp',
  props: {
    title: String,
    description: String,
  },
  data() {
    return {
      trend: [{
        trendContent: '【#16亿扶贫路偷工减料# 整改就是刷遍涂料？[怒]】国家投资近16亿的甘肃扶贫路，竟遭偷工减料！双层钢筋变单层，路基裂缝随处可见！隧道上方是大山，隐患不堪设想！整改就是刷了遍涂料…甘肃公路管理局副处长杨爱明称，我没空上去看去…甘肃交通运输厅领导不见记者，想待着就待着，不想待着就走”？！[微信]',
        timestamp: '2019-03-20 10:00'
      }, {
        trendContent: '怒！钢筋双层变单层，“整改”只是刷涂料，这就是16亿建成的“扶贫路”？！[微信]',
        timestamp: '2019-03-20 10:00'
      }],
      chartData: {
          columns: ['日期', '访问用户', '下单用户', '下单率'],
          rows: [
            { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
            { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
            { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
            { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
            { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
            { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
          ]
      },
      typeData1: {
          columns: ['日期', '访问用户'],
          rows: [
            { '日期': '1/1', '访问用户': 1393 },
            { '日期': '1/2', '访问用户': 3530 },
            { '日期': '1/3', '访问用户': 2923 },
            { '日期': '1/4', '访问用户': 1723 },
            { '日期': '1/5', '访问用户': 3792 },
            { '日期': '1/6', '访问用户': 4593 }
          ]
      },
      typeData3: {
        columns: ['日期', '访问用户'],
          rows: [
            { '日期': '1/1', '访问用户': 1393 },
            { '日期': '1/2', '访问用户': 3530 },
            { '日期': '1/3', '访问用户': 2923 },
            { '日期': '1/4', '访问用户': 1723 },
            { '日期': '1/5', '访问用户': 3792 },
            { '日期': '1/6', '访问用户': 4593 }
          ]
      },
      typeData4: {
        columns: ['日期', '访问用户', '下单用户', '下单率'],
          rows: [
            { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
            { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
            { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
            { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
            { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
            { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
          ]
      },
      wordData: {
          columns: ['word', 'count'],
          rows: getRows()
      },
      mapData: {
        columns: ['位置', '税收', '人口', '面积'],
          rows: [
            { '位置': '吉林', '税收': 123, '人口': 123, '面积': 92134 },
            { '位置': '北京', '税收': 1223, '人口': 2123, '面积': 29234 },
            { '位置': '上海', '税收': 2123, '人口': 1243, '面积': 94234 },
            { '位置': '浙江', '税收': 4123, '人口': 5123, '面积': 29234 }
          ]
      },
      treeData: {
        columns: ['name', 'value'],
        rows: [
          {
            name: 'tree1',
            value: [treeData]
          }
        ]
      }
    }
  },
}
function getRows () {
  return [{
    'word': 'visualMap',
    'count': 22199
  }, {
    'word': 'continuous',
    'count': 10288
  }, {
    'word': 'contoller',
    'count': 620
  }, {
    'word': 'series',
    'count': 274470
  }, {
    'word': 'gauge',
    'count': 12311
  }, {
    'word': 'detail',
    'count': 1206
  }, {
    'word': 'piecewise',
    'count': 4885
  }, {
    'word': 'textStyle',
    'count': 32294
  }, {
    'word': 'markPoint',
    'count': 18574
  }, {
    'word': 'pie',
    'count': 38929
  }, {
    'word': 'roseType',
    'count': 969
  }, {
    'word': 'label',
    'count': 37517
  }, {
    'word': 'emphasis',
    'count': 12053
  }, {
    'word': 'yAxis',
    'count': 57299
  }, {
    'word': 'name',
    'count': 15418
  }, {
    'word': 'type',
    'count': 22905
  }, {
    'word': 'gridIndex',
    'count': 5146
  }, {
    'word': 'normal',
    'count': 49487
  }, {
    'word': 'itemStyle',
    'count': 33837
  }, {
    'word': 'min',
    'count': 4500
  }, {
    'word': 'silent',
    'count': 5744
  }, {
    'word': 'animation',
    'count': 4840
  }, {
    'word': 'offsetCenter',
    'count': 232
  }, {
    'word': 'inverse',
    'count': 3706
  }, {
    'word': 'borderColor',
    'count': 4812
  }, {
    'word': 'markLine',
    'count': 16578
  }, {
    'word': 'line',
    'count': 76970
  }, {
    'word': 'radiusAxis',
    'count': 6704
  }, {
    'word': 'radar',
    'count': 15964
  }, {
    'word': 'data',
    'count': 60679
  }, {
    'word': 'dataZoom',
    'count': 24347
  }, {
    'word': 'tooltip',
    'count': 43420
  }, {
    'word': 'toolbox',
    'count': 25222
  }, {
    'word': 'geo',
    'count': 16904
  }, {
    'word': 'parallelAxis',
    'count': 4029
  }]
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
