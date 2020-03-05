"""
加权表的最短路径问题
"""
# python表示无穷大的数
infinity = float("inf")
# graph start a b fin之间的距离 定义途中的各个邻居节点
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3
graph["fin"] = {}

# costs: 起点到a b fin的开销 首尾已知点的代价
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents 存储父节点 记录最短路径 首尾已知点的父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# processed 记录处理过的几点 避免重复处理
processed = []


# 找到开销最低的点
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


# Dijkstra implement
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbor = graph[node]
    for n in neighbor.keys():
        new_cost = cost + neighbor[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# 结果路径
result = []
begin = "fin"
while begin != "start":
    result.insert(0, begin)
    begin = parents[begin]
result.insert(0, "start")
print(result, costs["fin"])