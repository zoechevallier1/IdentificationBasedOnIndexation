import rdflib


class TargetFile:
    def __init__(self, path):
        self.path = path

        # Get a RDF graph from the source file
        self.graph = rdflib.Graph()
        self.graph.parse(path, format="n3") 

        self.candidateDescriptions = dict()

        # Generating descriptions from a source file : the distinct property sets represented
        queryElts = "SELECT distinct ?c WHERE { ?c rdf:type ?o . FILTER (?o IN (rdfs:Class, owl:Class))}"
        resultsElements = self.graph.query(queryElts)

        
        
        desc = dict()
        for r in resultsElements:
            self.candidateDescriptions[str(r['c'])] = set()
            queryProperties = "SELECT distinct ?p WHERE { <" + str(r['c']) + "> ?p ?o. FILTER (?p NOT IN (rdf:type))}" 
            resProperties = self.graph.query(queryProperties)
            properties = set()
            for resProp in resProperties:
                properties.add(str(resProp['p']))
            if frozenset(properties) in desc.keys():
                desc[frozenset(properties)].add(frozenset(properties))
            else:
                desc[frozenset(properties)] = set(frozenset(properties))

            
            self.candidateDescriptions[str(r['c'])].add(frozenset(properties))

        self.descriptions = desc

        print("descriptions de départ :")
        for key, description in self.candidateDescriptions.items():
            print(key)
            print(description)

       
    def printCandidateDescriptions(self, C):
        for description in self.candidateDescriptions[str(C)]:
            print(description)