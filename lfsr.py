lfsr_state = [1, 1, 0, 1, 0, 0, 0, 1]
mask = [1, 3]

print("Inintial State")
print(lfsr_state)
print("mask")
print(mask)
print("\n")

def lfsr(state, mask):
    tmp = 0
    for i in mask:
        tmp = tmp ^ state[i]

    return [tmp] + state[:-1]

print(lfsr(lfsr_state, mask))