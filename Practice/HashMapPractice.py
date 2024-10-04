class HashMap:
    def __init__(self): 
        self.hashMap = {}

    def insert(self, key, value):
        self.hashMap[key] = value

    def display(self):
        for key, value in self.hashMap.items():
            print(f"{key}: {value}")

def main():
    s = HashMap()
    s.insert("apple", 5)
    s.insert("pear", 4)
    s.insert("john", 3)
    s.display()

main()