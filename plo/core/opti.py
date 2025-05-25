from functools import lru_cache
from .items_matrix import *

def tsp_with_path(graph):
    n = len(graph)
    all_nodes = frozenset(range(n))
    
    @lru_cache(maxsize=None)
    def dp(current, visited):
        # Convert visited to a frozenset (if it's not already)
        visited = frozenset(visited)
        
        # Base case: all nodes are visited.
        if visited == all_nodes:
            # Return cost 0 and the path consisting only of the current node.
            return 0, [current]
        
        best_cost = float('inf')
        best_path = []
        
        # Try all nodes that haven't been visited.
        for next_node in range(n):
            if next_node not in visited:
                # Mark the next_node as visited using a new frozenset.
                new_visited = visited | {next_node}
                # Recursively get the best cost and path from next_node.
                cost, path = dp(next_node, new_visited)
                total_cost = graph[current][next_node] + cost
                # Update if a better (lower cost) path is found.
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = [current] + path
        return best_cost, best_path

    # Try starting from each possible node and choose the best overall.
    best_overall_cost = float('inf')
    best_overall_path = []
    for start in range(n):
        cost, path = dp(start, frozenset({start}))
        if cost < best_overall_cost:
            best_overall_cost = cost
            best_overall_path = path

    return best_overall_cost, best_overall_path


def createGraph(skuList):  
    graphDict = {}
    graph=[]
    n=len(skuList)

    for i in range(n):
      graphDict[i] = skuList[i]

    for i in range(n):
      newList = []

      for j in range(n):
        newList.append(refMatrix[graphDict[i]][graphDict[j]])

      graph.append(newList)
    
    # print(graph)
    # print(graphDict)
    return graphDict, graph

def optimiseSKUs(skuList):  
  graphDict, graph = createGraph(skuList)
  cost , path = tsp_with_path(graph)
  print("Optimal cost:", cost)
  print("Optimal path:", path)

  finalPath =  []
  for i in range(len(path)):
    finalPath.append(graphDict[path[i]])

  return finalPath