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
    area = {
        "beijing":random.randint(0,9), 
        "shanghai":random.randint(0,9),
        "tianjin":random.randint(0,9),
        "chongqing":random.randint(0,9),
        "xianggang":random.randint(0,9),
        "aomen":random.randint(0,9),
        "anhui":random.randint(0,9),
        "fujian":random.randint(0,9),
        "guangdong":random.randint(0,9),
        "guangxi":random.randint(0,9),
        "guizhou":random.randint(0,9),
        "gansu":random.randint(0,9),
        "hainan":random.randint(0,9),
        "hebei":random.randint(0,9),
        "henan":random.randint(0,9),
        "heilongjiang":random.randint(0,9),
        "hubei":random.randint(0,9),
        "hunan":random.randint(0,9),
        "jilin":random.randint(0,9),
        "jiangsu":random.randint(0,9),
        "jiangxi":random.randint(0,9),
        "liaoning":random.randint(0,9),
        "neimenggu":random.randint(0,9),
        "ningxia":random.randint(0,9),
        "qinghai":random.randint(0,9),
        "shanxi":random.randint(0,9),
        "shaanxi":random.randint(0,9),
        "shandong":random.randint(0,9),
        "sichuan":random.randint(0,9),
        "taiwan":random.randint(0,9),
        "xizang":random.randint(0,9),
        "xinjiang":random.randint(0,9),
        "yunnan":random.randint(0,9),
        "zhejiang":random.randint(0,9)
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
    rows = []
    for i in range(2):
        rows.append(
            {
                "name":name,
                "num":random.randint(0,9)
            }
        )
    popular = {
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
