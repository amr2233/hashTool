import hashlib
class hashtext:
    def hashingtext(self,text,hash_type):
        text = text.encode("utf-8")
        hash_hash = hashlib.new(hash_type)
        hash_hash.update(text)
        return hash_hash.hexdigest()

class readw:
    def readwlist(self,wordlist):
        Or = open(wordlist,"r")
        return Or.readlines()
