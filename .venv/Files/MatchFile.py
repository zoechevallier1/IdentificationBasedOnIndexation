import xml.etree.ElementTree as ET

class MatchFile:
    def __init__(self, path):
        self.path = path
        # Parse the XML file
        tree = ET.parse(self.path)
        root = tree.getroot()

        # Define namespaces (if needed)
        namespaces = {
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        }

        # Initialize a list to hold all matches
        self.matches = []

        # Iterate over all match elements in the XML
        for match_element in root.findall(".//match"):
            match_type = match_element.attrib.get('type', 'unknown')  # Get match type (class or property)
            
            if match_type == 'class':
                classeSource = match_element.find('classeSource').text
                classeCible = match_element.find('classeCible').text
                match = {
                    "type": "class",
                    "source_class": classeSource,
                    "target_class": classeCible,
                }
                
            elif match_type == 'property':
                propSource = match_element.find('propSource').text
                propCible = match_element.find('propCible').text
                match = {
                    "type": "property",
                    "source_property": propSource,
                    "target_property": propCible,
                }
            
            self.matches.append(match)

    def printMatches(self):
        for m in self.matches:
            print(m)

    def class_matches_with_C(self, C):
        equivalent_classes = set()
        for match in self.matches:
            if match["type"] == "class" and (str(C) == match["target_class"]):
                equivalent_classes.add(match["source_class"])
        return equivalent_classes