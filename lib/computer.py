import ipdb
class Computer:
    def __init__(self,brand,model):
        self._brand = brand
        self._model = model
        self._memory_GB = 8
        self._storage_free = 1000
    
    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model
    
    @property
    def memory_GB(self):
        return self._memory_GB
    
    @memory_GB.setter
    def memory_GB(self,memory):
        self._memory_GB = memory

    @property
    def storage_free(self):
        return self._storage_free
    
    @storage_free.setter
    def storage_free(self,storage):
        if storage < 1000 and storage > 0:
            self._storage_free = storage 

    def upgrade_memory(self,RAM):
        self._memory_GB += RAM.get("size",0)
    
    def is_disk_full(self, file_size):
        return self.storage_free < file_size
    
    def save_file(self, file):
        file_size = file.get("size",0)
        if self.is_disk_full(file_size):
            return f"There is not enough space on disk to save {file['name']}."
        else:
            self.storage_free -= file_size
            return f"{file['name']} has been saved!"


comp = Computer("Dell","Inspiron")
#ipdb.set_trace()
#comp.brand("HP")

print(f"Storage Before: {comp.storage_free}")
comp.storage_free = 500
print(f"Storage After: {comp.storage_free}")
comp.storage_free = 1500
print(f"Storage After2: {comp.storage_free}")

print(f"Memory Before: {comp.memory_GB}")
comp.memory_GB = 10
print(f"Memory After: {comp.memory_GB}")

comp.upgrade_memory({"model": "HP", "size": 8})
print(f"Memory After Upgrade: {comp.memory_GB}")

print(comp.save_file({"name": "sample.py", "size": 100}))
print(comp.save_file({"name": "sample.py", "size": 1000000}))


if __name__ == "__main__":
    # you can write test code here
    # or in debug.py
    pass
