def shortestPath(source,destination,graph):
    maxHeap=dict()
    nodeDistance=dict()
    countOfNodes=len(graph)
    for eachNode in range(1,countOfNodes+1):
        maxHeap.update({eachNode:float('inf')})
    currentNode=source
    nodeDistance.update({currentNode:0})
    del maxHeap[currentNode]
    while maxHeap:
        if len(graph[currentNode])==0:
            break
        for eachEdge in graph[currentNode]:
            weightOfEdge=graph[currentNode][eachEdge]
            if eachEdge not in maxHeap:
                continue
            if maxHeap[eachEdge]>weightOfEdge+nodeDistance[currentNode]:
                maxHeap.update({eachEdge:weightOfEdge+nodeDistance[currentNode]})
        currentNode=min(maxHeap,key=maxHeap.get)
        nodeDistance.update({currentNode:maxHeap[currentNode]})
        del maxHeap[currentNode]
        if currentNode==destination:
            break
    if destination in maxHeap:
        shortPath=-1
    else:
        shortPath=nodeDistance[destination]
    return shortPath

#input   
numberOfNodes,numberOfEdges=map(int,(input().strip().split()))
directedGraph=dict()
for eachNode in range(1,numberOfNodes+1):
    directedGraph.update({eachNode:dict()}) 
for edge in range(numberOfEdges):
        startNode,endNode,weightOfEdge=map(int,(input().strip().split()))
        directedGraph[startNode].update({endNode:weightOfEdge})
queries=int(input())
recentQuery=dict()
for query in range(queries):
    
    source,dest=map(int,(input().strip().split()))
    if (source,dest) in recentQuery:
        shortDistance=recentQuery[(source,dest)]        
    elif source==dest:
        shortDistance=0
    else:
        shortDistance=shortestPath(source,dest,directedGraph)
        recentQuery.update({(source,dest):shortDistance})
    print(shortDistance)
