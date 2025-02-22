def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence
n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence(n)}")
