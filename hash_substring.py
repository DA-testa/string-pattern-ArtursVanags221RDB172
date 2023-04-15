# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type = input().strip()

    if input_type == "I":
        pattern = input().strip()
        text = input().strip()

    elif input_type == "F":
        with open("input.txt", "r") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the 
    pr = 10**9 + 7
    return algorithm(pattern, text, pr)

def algorithm(pattern, text, pr):
    U, N, e, g, r, x, d, result = len(pattern), len(text), 256, pr, pow(256, len(pattern)-1, pr), 0, 0, []
    for i in range(U):
        x = (x * e + ord(pattern[i])) % g
        d = (d * e + ord(text[i])) % g
    for i in range(N - U + 1):
        if x == d and pattern == text[i:i + U]:
            result.append(i)
        if i < N - U:
            d = (e * (d - ord(text[i]) * r) + ord(text[i + U])) % g
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

