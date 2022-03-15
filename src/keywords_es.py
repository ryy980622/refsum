# Name: keywords_es
# Author: Reacubeth
# Time: 2021/4/21 17:14
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from elasticsearch import Elasticsearch
import time
import json


def es_paper(keywords):
    """
    :param keywords: it is a list containing all types of keywords, example: ['Xiumian Hu', 'SJTU']
    :return: json of query
    """
    match_ls = []

    for kw in keywords:
        item = {
            "multi_match": {
                "query": kw,
                "type": "best_fields",
                "operator": "or",  # 完全匹配改成and
                "fields": ["title^2", 'abstract'],
                "tie_breaker": 0.3,
                "minimum_should_match": "30%"
            },
        }
        match_ls.append(item)

    query = {
        "query": {
            "bool": {
                "should": match_ls,
                "minimum_should_match": 1
            }
        },
        "size": 5,
    }
    return query

def keyword2papers(keyword):
    es = Elasticsearch([{'host': '10.10.10.10', 'port': 9200}])
    query = es_paper([keyword])   # 同时匹配多个短语或者单词，返回Top10
    res = es.search(index="paper", body=query)['hits']['hits']
    papers, abs = [], []
    for item in res:
        if 'abstract' in item['_source'].keys() and len(item['_source']['abstract']) > 100:
            papers.append(item['_source']['title'])
            abs.append(item['_source']['abstract'])
        # print(item['_source'])
    return papers, abs