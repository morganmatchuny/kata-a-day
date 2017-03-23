#Description:

#The input is a string str of digits. Cut the string into chunks 
#(a chunk here is a substring of the initial string) of size sz 
#(ignore the last chunk if its size is less than sz).

#If a chunk represents an integer such as the sum of the cubes 
#of its digits is divisible by 2, reverse that chunk; otherwise 
#rotate it to the left by one position. Put together these 
#modified chunks and return the result as a string.

def revrot(string, size):
    if not size:
        return ''

    chunks = [string[i:i + size] for i in range(0, len(string), size)]
    if len(chunks[-1]) != size:
        chunks.pop()

    result = []
    for chunk in chunks:
        if sum(int(digit)**3 for digit in chunk) % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])

    return ''.join(result)
