import rdflib

def printResultsFile(path, source, classe, candidateInstances):
    resultGraph = rdflib.Graph()

    for description in candidateInstances[classe]:

        query = "CONSTRUCT { ?e ?p ?o . ?e rdf:type <" + classe + "> . \n"
        for property in description:
            query += "?e <" + property + "> ?o_" + property.split("#")[-1] + ". \n"
        query += "} \n WHERE {"
        filter = ""
        for property in description:
            query += "?e <" + property + "> ?o_" + property.split("#")[-1] + ". \n"
            filter += "<" + property + ">, "
        query += "MINUS { ?e ?prop ?o FILTER (?prop NOT IN ( " + filter[0:-2]+"))}"
        query += "}"
        print(query)

        results = source.graph.query(query)
        graph = rdflib.Graph()
        for triple in results:
            graph.add(triple)

        resultGraph += graph

    resultGraph.serialize(destination=path, format="n3")

    