import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

def generateBucketGraph(buckets):
    
    bucketGraph = dict()
    for key, entities in buckets.items():
        if (len(entities))>1:
            bucketGraph[key] = set()
            for k,b in bucketGraph.items():
                if k != key and not(buckets[k].isdisjoint(entities)):
                    bucketGraph[key].add(k)
    return bucketGraph


def plot_graph(graph_dict):
    """
    Plots a graph represented by a dictionary.
    
    Parameters:
        graph_dict (dict): A dictionary where keys are nodes and values are lists of connected nodes.
    """
    # Create a NetworkX graph object
    G = nx.Graph()
    
    # Add edges to the graph
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, 
        with_labels=True, 
        node_color='lightblue', 
        edge_color='gray', 
        node_size=500, 
        font_size=10
    )
    plt.title("Bucket Graph Visualization")
    plt.show()

