import random
import hashlib

class Indexation:
    def __init__(self, elements, k, b, r):
        self.elements = elements
        self.buckets = dict()
        self.signatures = dict()
        self.generateSignature(elements, k)
        self.indexationLSH( k, b, r)
        self.printBuckets()

    def generate_minhash_functions(self, num_hashes: int, max_hash: int = (2**32 - 1)):
        hash_functions = []
        for i in range(num_hashes):
            a = random.randint(1, max_hash - 1)
            b = random.randint(0, max_hash - 1)
            hash_functions.append((a, b))
        return hash_functions


    def apply_minhash(self, hash_functions, data_set, max_hash: int = (2**32 - 1)):
        signature = []
        for a, b in hash_functions:
            min_hash = min(((a * hash(x) + b) % max_hash) for x in data_set)
            signature.append(min_hash)
        return signature


    def generateSignature(self,elements, k):
        hash_functions = self.generate_minhash_functions(k)
        for description, value in elements.items():
            if len(description) != 0:
                signature = self.apply_minhash(hash_functions, description)
                self.signatures[tuple(signature)] = frozenset(description)
                
        
    def getBande(self, signature, r, i):
        return signature[i*r:i*r+r-1]


    def indexationLSH(self, k, b, r):

        bucket = dict()
        
        for signature, elements in self.signatures.items():
            for i in range (0,b):
                bande = self.getBande(signature, r, i)
                keystr = str(i) + str(bande)
                if keystr not in bucket:
                    bucket[keystr] = set()
                bucket[keystr].add(elements)
                    
        bucket = {key: value for key, value in bucket.items() if len(value) > 1}
        seen_sets = {}
        self.buckets = {}

        for key, value in bucket.items():
            # Convert the set to a frozenset so it can be used as a dictionary key
            frozen_value = frozenset(value)
            if frozen_value not in seen_sets:
                seen_sets[frozen_value] = key
                self.buckets[key] = value

    def printBuckets(self):
        for bucketName, values in self.buckets.items():
            print(bucketName)
            print(values)

    
