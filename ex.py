def can_form_permutation(T, test_cases):
    results = []
    for i in range(T):
        N = test_cases[i][0]
        A = test_cases[i][1]
        
        # Frequency array to count occurrences of each element in A
        freq = [0] * (N + 1)
        for num in A:
            freq[num] += 1
            
        # Check if we can form a permutation of [1, N]
        possible = True
        for x in range(1, N + 1):
            if freq[x] == 0:  # If x is not present in A, it must be constructed
                found = False
                for j in range(1, N + 1):
                    if freq[j] > 1 and j + (freq[j] - 1) >= x:
                        freq[j] -= 1
                        found = True
                        break
                if not found:
                    possible = False
                    break
                    
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Example Input
T = 4
test_cases = [
    (5, [4, 1, 3, 2, 1]),   # Example: N=5, A=[4, 1, 3, 2, 1]
    (5, [2, 4, 3, 4, 2]),   # Example: N=5, A=[2, 4, 3, 4, 2]
    (1, [1]),               # Example: N=1, A=[1]
    (6, [1, 1, 1, 1, 6, 6]) # Example: N=6, A=[1, 1, 1, 1, 6, 6]
]

# Calculate if a permutation can be formed for each test case
results = can_form_permutation(T, test_cases)

# Output the results
for result in results:
    print(result)
