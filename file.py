class MyFile:
    def __init__(self, _name, _size):
        self.name = _name
        self.size = _size
    
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size

    def set_name(self, new_name):
        self.name = new_name
    
    def set_size(self, new_size):
        self.size = new_size