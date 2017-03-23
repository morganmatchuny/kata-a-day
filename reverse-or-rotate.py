def revrot(string, size):
    if not size:
        return ''

    chunks = [string[i:i+size] for i in range(0, len(string), size)]
    if len(chunks[-1]) != size:
        chunks.pop()

    result = []
    for chunk in chunks:
        if sum(int(digit)**3 for digit in chunk) % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])

    return ''.join(result)
