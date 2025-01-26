import sys

class coron:
    def __init__(self, chunksize=32, pointer=2):
        self.data = [-1 for i in range(0, 2**7)]

        self.chunks = chunksize # each chunk size, in total of 4
        self.pointers = pointer # pointer size, we need 2 cuz 2^2 = 4
    def set(self, pointer, data):
        if pointer > 0 and pointer < 2**2:
            j = 0
            for i in range(pointer*self.chunks, pointer*self.chunks + len(data)):
                self.data[i] = data[j]
                j += 1
    def get(self, pointer):
        if pointer > 0 and pointer < 2**2:
            data = []
            i = pointer*self.chunks
            while self.data[i] != -1:
                data.append(self.data[i])
                i += 1
            return data
    def testchunk(self, pointer):
        p1 = pointer*self.chunks
        p2 = (pointer+1)*self.chunks
        for i in range(p1, p2):
            if self.data[i] != -1:
                print(self.data[i], end='|')
        print(" ")
if __name__ == '__main__':
    c = coron()
    _ = []
    for i in "hello!":
        _.append(ord(i))
    c.set(2, _)
    c.testchunk(2)
