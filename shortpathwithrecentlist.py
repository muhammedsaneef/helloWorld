def shortestPath(source,destination,graph):
    maxHeap=dict()
    nodeDistance=dict()
    countOfNodes=len(graph)
    for eachNode in range(1,countOfNodes+1):
        maxHeap.update({eachNode:float('inf')})
    currentNode=source
    nodeDistance.update({currentNode:0})
    #print(maxHeap)
    #print(nodeDistance)
    #print('Cr',currentNode)
    #print(graph[currentNode])
    #u=input()
    while maxHeap and currentNode!=destination:
        if len(graph[currentNode])==0:
            break
        for eachEdge in graph[currentNode]:
            #print('CurrentNode',currentNode)
            #print('graph',graph[currentNode])
            weightOfEdge=graph[currentNode][eachEdge]
            if eachEdge not in maxHeap:
                maxHeap.update({eachEdge:float('inf')})
            if maxHeap[eachEdge]>weightOfEdge+nodeDistance[currentNode]:
                maxHeap.update({eachEdge:weightOfEdge+nodeDistance[currentNode]})
        currentNode=min(maxHeap,key=maxHeap.get)
        
        #o=input()
        nodeDistance.update({currentNode:maxHeap[currentNode]})
        #print('nodedist',nodeDistance)
        #print('maxHeap',maxHeap)
        del maxHeap[currentNode]
        if currentNode==source:
            break
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
#fin=open('input001.txt','r')
for edge in range(numberOfEdges):
        startNode,endNode,weightOfEdge=map(int,(input().strip().split()))
        if endNode in directedGraph[startNode]:
            if weightOfEdge<directedGraph[startNode][endNode]:
                directedGraph[startNode].update({endNode:weightOfEdge})
        else:
            directedGraph[startNode].update({endNode:weightOfEdge})
#fin.close()
#print(directedGraph)
queries=int(input())
#fin=open('input01.txt','r')
recentQuery=dict()
for query in range(queries):
    
    source,dest=map(int,(input().strip().split()))
    if (source,dest) in recentQuery:
        shortDistance=recentQuery[(source,dest)]        
    #print(source,dest)
    #q=input()
    elif source==dest:
        shortDistance=0
    else:
        shortDistance=shortestPath(source,dest,directedGraph)
        recentQuery.update({(source,dest):shortDistance})
    print(shortDistance)
    #n=input()
#fin.close()
