import rdflib


class TargetFile:
    def __init__(self, path):
        self.path = path

        # Get a RDF graph from the source file
        self.graph = rdflib.Graph()
        self.graph.parse(path, format="n3") 

        self.classes = set()

        # Generating descriptions from a source file : the distinct property sets represented
        queryElts = "SELECT distinct ?c WHERE { ?c rdf:type ?o . FILTER (?o IN (rdfs:Class, owl:Class))}"
        resultsElements = self.graph.query(queryElts)
        
        desc = dict()
        for r in resultsElements:
            self.classes.add(r['c'])
            queryProperties = "SELECT distinct ?p WHERE { <" + str(r['c']) + "> ?p ?o. FILTER (?p NOT IN (rdf:type))}" 
            resProperties = self.graph.query(queryProperties)
            properties = set()
            for resProp in resProperties:
                properties.add(str(resProp['p']))
            
            if frozenset(properties) in desc:
                desc[frozenset(properties)] = desc[frozenset(properties)] + r['c']
            else:
                desc[frozenset(properties)] = r['c']

        self.descriptions = desc

        for c in self.classes:
            print(c)
        for description, value in self.descriptions.items():
            print(description)
            print(value)
                