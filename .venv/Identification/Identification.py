from collections import deque
import Files
import os

def identification(matchs, source, target, grapheBuckets, buckets, c):
    
    ## matchs 
    equiv_classes = matchs.class_matches_with_C(c)
    for cl in equiv_classes:
        for desc in source.getDescriptionsType(cl):
            target.candidateDescriptions[str(c)].add(desc)
    
    ## Similarité extensionnelle
    nodesToExplore = set()

    for key, descriptions in buckets.items():
        
        if not(target.candidateDescriptions[str(c)].isdisjoint(descriptions)):
            nodesToExplore.add(key)
    exploredNodes = set()

    while len(nodesToExplore) > 0:
        fifo = deque()
        node = nodesToExplore.pop()
        fifo.append(node)
        
        while len(fifo) > 0 :
            s = fifo.popleft()
            for d in buckets[s]:
                target.candidateDescriptions[str(c)].add(d)
            exploredNodes.add(s)
            for succ in grapheBuckets[s]:
                fifo.append(succ)   
     




