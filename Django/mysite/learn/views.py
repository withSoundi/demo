# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import json
import random
 
 
def index(request):
    return HttpResponse(u"fuck")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def get_data(name):
    introduction = name
    # 事件简介
    trend = []
    for i in range(5):
        trend.append({
            "trendContent":name,
            "timestamp":i + 1
        })
    # 事件走势
    rows = []
    for i in range(10):
        rows.append({
            "date":i + 1, 
            "all":random.randint(0,9),
            "client":random.randint(0,9),
            "press":random.randint(0,9),
            "blog":random.randint(0,9),
            "media":random.randint(0,9),
            "forum":random.randint(0,9),
            "video":random.randint(0,9),
            "weibo":random.randint(0,9),
            "site":random.randint(0,9),
            "news":random.randint(0,9),
            "gov":random.randint(0,9)
        })
    statistics = {
        "columns":[
            "date", 
            "all",
            "client",
            "press",
            "blog",
            "media",
            "forum",
            "video",
            "weibo",
            "site",
            "news",
            "gov"
            ],
        "rows":rows
    }
    
    # 网站统计
    rows = [{
        "type":"sensitive",
        "value":random.randint(0,9)
        },{
        "type":"insensitive",
        "value":random.randint(0,9)
        }
        ]
    emotion = {
        "columns": ["type","value"],
        "rows":rows
    }
    rows = [{
        "type":"overseas",
        "value":random.randint(0,9)
        },{
        "type":"inland",
        "value":random.randint(0,9)
    }]
    # 情感分析
    overseas = {
        "columns": ["type","value"],
        "rows":rows
    }
    # 境内外分布

    rows = [{
        "type":"all","value":random.randint(0,9)},{ 
        "type":"client","value":random.randint(0,9)},{ 
        "type":"press","value":random.randint(0,9)},{
        "type":"blog","value":random.randint(0,9)},{
        "type":"media","value":random.randint(0,9)},{
        "type":"forum","value":random.randint(0,9)},{
        "type":"video","value":random.randint(0,9)},{
        "type":"weibo","value":random.randint(0,9)},{
        "type":"site","value":random.randint(0,9)},{
        "type":"news","value":random.randint(0,9)},{
        "type":"gov","value":random.randint(0,9)}
    ] 
    mediasource = {
        "columns" : [
            "type",
            "value"
            ],
            "rows":rows
        }
    rows = []
    # 媒体来源占比
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }
        )
    activity = {
        "columns": [
            "name",
            "num"
        ],
        "rows":rows
    }
    rows = [{
        "type":"beijing","value":random.randint(0,9)},{
        "type":"shanghai","value":random.randint(0,9)},{
        "type":"tianjin","value":random.randint(0,9)},{
        "type":"chongqing","value":random.randint(0,9)},{
        "type":"xianggang","value":random.randint(0,9)},{
        "type":"aomen","value":random.randint(0,9)},{
        "type":"anhui","value":random.randint(0,9)},{
        "type":"fujian","value":random.randint(0,9)},{
        "type":"guangdong","value":random.randint(0,9)},{
        "type":"guangxi","value":random.randint(0,9)},{
        "type":"guizhou","value":random.randint(0,9)},{
        "type":"gansu","value":random.randint(0,9)},{
        "type":"hainan","value":random.randint(0,9)},{
        "type":"hebei","value":random.randint(0,9)},{
        "type":"henan","value":random.randint(0,9)},{
        "type":"heilongjiang","value":random.randint(0,9)},{
        "type":"hubei","value":random.randint(0,9)},{
        "type":"hunan","value":random.randint(0,9)},{
        "type":"jilin","value":random.randint(0,9)},{
        "type":"jiangsu","value":random.randint(0,9)},{
        "type":"jiangxi","value":random.randint(0,9)},{
        "type":"liaoning","value":random.randint(0,9)},{
        "type":"neimenggu","value":random.randint(0,9)},{
        "type":"ningxia","value":random.randint(0,9)},{
        "type":"qinghai","value":random.randint(0,9)},{
        "type":"shanxi","value":random.randint(0,9)},{
        "type":"shaanxi","value":random.randint(0,9)},{
        "type":"shandong","value":random.randint(0,9)},{
        "type":"sichuan","value":random.randint(0,9)},{
        "type":"taiwan","value":random.randint(0,9)},{
        "type":"xizang","value":random.randint(0,9)},{
        "type":"xinjiang","value":random.randint(0,9)},{
        "type":"yunnan","value":random.randint(0,9)},{
        "type":"zhejiang","value":random.randint(0,9)
    }]
    area = {
        "columns":[
            "type",
            "value"
        ],
        "rows":rows
    }
    rows = []
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }
        )
    words = {
        "columns":[
            "name",
            "num"
        ],
        "rows":rows
    }
    popular = []
    for i in range(2):
        popular.append({
            "hotTitle":name,
            "hotSource":name,
            "hotTime":random.randint(0,9),
            "hotNumber":random.randint(0,9)
        })
    rows = []
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }
        ) 
    newspoint = {
        "columns":[
            "name",
            "num"
        ],
        "rows":rows
    }
    rows = []
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }     
        )
    forumpoint = {
        "columns":[
            "name",
            "num"
        ],
        "rows":rows
    }
    rows = []
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }   
        )  
    weibopoint = {
        "columns":[
            "name",
            "num"
        ],
        "rows":rows
    }
    summary = name
    return json.dumps({
        "name":name,
        "content":introduction,
        "trend":trend,
        "chartData":statistics,
        "typeData1":emotion,
        "typeData2":overseas,
        "typeData3":mediasource,
        "typeData4":activity,
        "mapData":area,
        "wordData":words,
        "popular":popular,
        "newsPoint":newspoint,
        "forumPoint":forumpoint,
        "weiboPoint":weibopoint,
        "summary":summary
    })
    

def query(request):
    name = request.GET['name']
    data = get_data(name)
    return HttpResponse(data)
