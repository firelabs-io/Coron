import sys

class coron:
    def __init__(self, chunksize=64, pointer=4):
        self.data = [0 for i in range(0, 2**14)]
        self.pointarr = [0 for i in range(pointer**2)]
        self.chunks = chunksize # each chunk size, in total of 4
        self.pointers = pointer # pointer size, we need 2 cuz 2^2 = 4
    def set(self, pointer, data):
        if pointer > 0 and pointer < 2**4:
            j = 0
            for i in range(pointer*self.chunks, pointer*self.chunks + len(data)):
                self.data[i] = data[j]
                j += 1
            self.pointarr[pointer-1] = 1
    def get(self, pointer):
        if pointer > 0 and pointer < 2**4:
            data = []
            i = pointer*self.chunks
            while self.data[i] != 0:
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
    def savePointer(self, pointer, remove=False):
        if remove:
            self.pointarr[pointer-1] = 0
        else:
            self.pointarr[pointer-1] = 1

if __name__ == '__main__':
    c = coron()
    _ = []
    for i in "Obj John 1100":
        _.append(ord(i))
    c.set(2, _)
    c.set(15, [76])
    c.testchunk(2)
    print(c.pointarr)
    with open(sys.argv[1], 'wb') as file:
        for v in c.pointarr:
            file.write(bytes([v]))
        for value in c.data:
            file.write(bytes([value]))
