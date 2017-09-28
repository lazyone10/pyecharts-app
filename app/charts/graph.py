import os
import json

from pyecharts import Graph, Page


def graph_charts():
    page = Page()

    nodes = [{"name": "结点1", "symbolSize": 10},
             {"name": "结点2", "symbolSize": 20},
             {"name": "结点3", "symbolSize": 30},
             {"name": "结点4", "symbolSize": 40},
             {"name": "结点5", "symbolSize": 50},
             {"name": "结点6", "symbolSize": 40},
             {"name": "结点7", "symbolSize": 30},
             {"name": "结点8", "symbolSize": 20}]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    chart = Graph("关系图-力引导布局")
    chart.add("", nodes, links, repulsion=8000, line_color='#aaa')
    page.add(chart)

    chart = Graph("关系图-环形布局")
    chart.add("", nodes, links, is_label_show=True, graph_repulsion=8000,
              graph_layout='circular', label_text_color=None)
    page.add(chart)

    with open(os.path.join(".", "static", "json", "weibo.json"), "r", encoding="utf-8") as f:
        j = json.load(f)

    nodes, links, categories, cont, mid, _ = j
    chart = Graph("关系图-微博转发", width=1200, height=600)
    chart.add("", nodes, links, categories, label_pos="right", graph_repulsion=50,
              is_legend_show=False, line_curve=0.2, label_text_color=None)
    page.add(chart)

    return page
