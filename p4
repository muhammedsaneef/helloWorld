
def shortestPath(source,destination,graph):
    maxHeap=dict()
    nodeDistance=dict()
    countOfNodes=len(graph)
    for eachNode in range(1,countOfNodes+1):
        maxHeap.update({eachNode:float('inf')})
    print(maxHeap)
    currentNode=source
    nodeDistance.update({currentNode:0})
    while maxHeap:
        for (eachEdge,weight) in graph[currentNode]:
            if maxHeap[eachEdge]>weight:
                maxHeap.update({eachEdge:weight+nodeDistance[currentNode]})
        currentNode=min(maxHeap,key=maxHeap.get)
        nodeDistance.update({currentNode:maxHeap[currentNode]})
        del maxHeap[currentNode]
    if destination in maxHeap:
        shortPath=-1
    else:
        shortPath=nodeDistance[destination]
    return shortPath
    
numberOfNodes,numberOfEdges=map(int,(input().split()))
#print(numberOfNodes,numberOfEdges)
directedGraph=dict()
#maxHeap=dict()
for eachNode in range(1,numberOfNodes+1):
#    maxHeap.update({eachNode:float('inf')})
    directedGraph.update({eachNode:[]}) 
#print(maxHeap)
for eachEdge in range(numberOfEdges):
    startNode,endNode,weightOfEdge=map(int,(input().split()))
    #print(startNode,endNode,weightOfEdge)
    if startNode in directedGraph:
        directedGraph[startNode].append((endNode,weightOfEdge))
    else:
        directedGraph.update({startNode:[(endNode,weightOfEdge)]})
print(directedGraph)
queries=int(input())
for eachQuery in range(queries):
    source,dest=map(int,(input().split()))
    print(source,dest)
    shortDistance=shortestPath(source,dest,directedGraph)
    print(shortDistance)
