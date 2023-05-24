def return_char(chars: list[str]) -> str:
    l, r = 0, len(chars) - 1
    m = l + (r - l) // 2
    char_vals = [ord(c) for c in chars]
    while l < m:
        if char_vals[l]+1 != char_vals[l+1]:
            return chr(char_vals[l]+1)
        l += 1
    while r >= m:
        if char_vals[r]-1 != char_vals[r-1]:
            return chr(char_vals[r]-1)
        r -= 1
