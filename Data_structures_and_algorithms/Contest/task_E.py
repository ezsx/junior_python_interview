def total_spell_power(N, K, S, p, d):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_map = {char: idx for idx, char in enumerate(alphabet)}
    total_power = 0

    for start_pos in range(N):
        for spell_len in range(1, K + 1):
            unique_chars = set()
            current_pos = start_pos
            for _ in range(spell_len):
                current_char = S[current_pos]
                unique_chars.add(current_char)
                current_pos = p[current_pos] - 1
                current_char_index = alphabet_map[current_char]
                current_char_index = (current_char_index + d[current_pos]) % 26
                S[current_pos] = alphabet[current_char_index]
            total_power += len(unique_chars)
    return total_power


# Read input
N, K = map(int, input().split())
S = list(input().strip())  # Convert string to list of characters
p = list(map(int, input().split()))
d = list(map(int, input().split()))

# Calculate total power of all spells
result = total_spell_power(N, K, S, p, d)

# Print output
print(result)
