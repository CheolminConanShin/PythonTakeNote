class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def step(self, value):
        self.sum += value
        self.cnt += 1

    def finalize(self):
        return self.sum / self.cnt
    
