message = "Bom dia!"
pattern = "*~*~*~*~*~*~*~*~"

for char in message:
    print(char, end=f"{pattern[0]} ")
    pattern = pattern[1:] + pattern[0]

print()
