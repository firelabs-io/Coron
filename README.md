# Coron
An pointer based database (idk why)

# what is
basically (norally i will make in binary or smt but i will over simplfy)
so it works using pointers instead of index etc, like if we have 2 bit pointer (00, 01, 10, 11, though not best) then we can just jmp to that address
however normally will not work, cuz well, there no hash map or smt, so we just separate into chunks, where each one has an beggining and end, and each one has own chunk
so for this exaple, 4 chunks, 2 bit pointer or smt, and each chunk is 32 bits
so in total we should have 128 bits, and yeah it works

# next
- [ ] put in binary (not normal text, it will be like ascii or smt)
- [ ] allow chunks data may point to toher chunks
- [ ] add first part of data just for the pointers
- [ ] more ideas
