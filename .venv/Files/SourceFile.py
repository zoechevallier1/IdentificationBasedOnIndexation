import rdflib


class SourceFile:
    def __init__(self, path):
        self.path = path

        # Get a RDF graph from the source file
        self.graph = rdflib.Graph()
        self.graph.parse(path, format="n3") 

        # Generating descriptions from a source file : the distinct property sets represented
        queryElts = "SELECT distinct ?e WHERE { ?e ?p ?o .}"
        resultsElements = self.graph.query(queryElts)
        i = 0
        desc = dict()
        for r in resultsElements:
            queryProperties = "SELECT distinct ?p WHERE { <" + str(r['e']) + "> ?p ?o. FILTER (?p NOT IN (rdf:type))}" 
            resProperties = self.graph.query(queryProperties)
            properties = set()
            for resProp in resProperties:
                properties.add(str(resProp['p']))
            queryType = "SELECT ?c WHERE { <" + str(r['e']) + "> rdf:type ?c}"
            resType = self.graph.query(queryType)
            type = set()
            if resType is not None:
                for rType in resType:
                    type.add(str(rType['c']))
            if frozenset(properties) in desc:
                desc[frozenset(properties)].update(type)
            else:
                desc[frozenset(properties)] = set(type)

        self.descriptions = desc

        for description, type in self.descriptions.items():
            print(description)
            print(type)
        


