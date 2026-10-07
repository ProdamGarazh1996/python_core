def recursive_pass_count(statuses, index=0, count=0):
    if len(statuses) == index:
        return count
    if statuses[index] == 'PASS':
        count = count + 1
    return recursive_pass_count(statuses, index + 1, count)


status_array = ['FAIL', 'SKIP', 'PASS', 'SKIP', 'PASS']

result = recursive_pass_count(status_array)
print(result)
