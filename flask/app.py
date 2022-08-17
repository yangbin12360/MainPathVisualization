from flask import Flask, request, jsonify
from flask_cors import *
import json
import networkx as nx
import threading
import math


app = Flask(__name__)
CORS(app, support_credentials=True)
exitFlag = 0


@app.route('/test', methods=['POST', 'GET'])
def hello_world():
    val = request.get_json()
    sY = int(val["startY"])
    eY = int(val["endY"])
    diameter = int(val["diameter"])
    tempDict = {}
    with open("./static/" + val["startY"] + ".json", "r", encoding="utf-8") as f:
        tempDict = json.load(f)
    for i in range(sY + 1, eY + 1):
        with open("./static/" + str(i) + ".json", "r", encoding="utf-8") as f:
            tempData = json.load(f)
            tempDict["nodes"] = tempData["nodes"] + tempDict["nodes"]
            tempDict["links"] = tempData["links"] + tempDict["links"]
    print(len(tempDict["nodes"]))
    print(len(tempDict["links"]))
    newDict = node_sift(tempDict, diameter)
    # print(newDict)
    return newDict


def node_sift(nodeDict, d):
    tempNodes = nodeDict["nodes"]
    tempLinks = nodeDict["links"]
    nodesList = []
    linksList = []
    # 点处理
    for i in tempNodes:
        tempTum = (i["id"], {"标题": i["标题"],
                             "摘要": i["摘要"],
                             "申请人": i["申请人"],
                             "IPC主分类": i["IPC主分类"],
                             "CPC": i["CPC"],
                             "引证次数": i["引证次数"],
                             "被引证次数": i["被引证次数"],
                             "公开（公告）日": i["公开（公告）日"]})
        nodesList.append(tempTum)
    # 边处理
    for j in tempLinks:
        tempTum = ()
        tempTum = (j["source"], j["target"])
        linksList.append(tempTum)
    print(nodesList)
    G = nx.Graph()
    G.add_nodes_from(nodesList)
    G.add_edges_from(linksList)
    print("1", G.number_of_nodes())
    print("2", G.number_of_edges())
    min_net_size = d
    # components = list(nx.connected_components(G))
    # for component in components:
    #     if len(component) < min_net_size:  # remove small networks
    #         for node in component:
    #             G.remove_node(node)
    components = list(nx.connected_components(G))
    if len(components) < 10:
        epoch = len(components)
    else:
        epoch = math.ceil(len(components) / 10)

    print('主程序开始运行...')
    threadList = []
    for i in range(0, 10):
        t = threading.Thread(target=gSubset, args=(G, components, min_net_size, i*epoch, (i+1)*epoch))
        threadList.append(t)
        t.start()

    print('主程序运行中...')
    for t in threadList:
        t.join()
    print("所有线程任务完成")
    print("components", list(nx.connected_components(G)))
    connectList = list(nx.connected_components(G))
    nodesJson = {"nodes": [], "links": []}
    for i in G.nodes.data():
        nodesJson["nodes"].append({"id": i[0], "标题": i[1]["标题"],
                                   "摘要": i[1]["摘要"],
                                   "申请人": i[1]["申请人"],
                                   "IPC主分类": i[1]["IPC主分类"],
                                   "CPC": i[1]["CPC"], "引证次数": i[1]["引证次数"],
                                   "被引证次数": i[1]["被引证次数"],
                                   "公开（公告）日": i[1]["公开（公告）日"]})
    for i in G.edges:
        nodesJson["links"].append({"source": i[0], "target": i[1]})
    # print(nodesJson)
    return nodesJson


def gSubset(G, components, min_net_size, start, end):
    if end > len(components):
        end = None
    for c in components[start: end]:
        if nx.diameter(G.subgraph(c)) < min_net_size:  # remove small networks
            for node in c:
                G.remove_node(node)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
