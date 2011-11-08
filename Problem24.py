# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

permutations = []

def getLexicographicPermutationsOf(digits, state):
	if len(digits) == 0:
		permutations.append("".join([str(x) for x in state]))

	for i in range(len(digits)):
		state.append(digits[i])
		rest = digits[:i] + digits[i+1:]
		getLexicographicPermutationsOf(rest, state)
		state.pop()

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
getLexicographicPermutationsOf(digits, [])
print(permutations[999999])
