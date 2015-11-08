
from Stack import Stack

# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTIONS = []
# This contains the path to the solution backwards. 
SOLUTION_PATHS = []


def main():
	initialState = 10
	algorithm(initialState)
	# print results
	print SOLUTIONS
	print SOLUTION_PATHS
	print STATES_ARCHIVE


def algorithm(initialState):
	stack = Stack()
	# add first state
	stack.push(initialState)
	STATES_ARCHIVE.append([initialState, 0])
	# loop all possible moves
	count = 0
	while stack.isNotEmpty():
		count += 1
		option = stack.pop();
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				continue
			elif optionIsSolution(newOption):
				SOLUTIONS.append([newOption, option])
				continue
			else:
				# add the option to the stack for later evaluation
				stack.push(newOption)
				# add the option to the states archive
				STATES_ARCHIVE.append([newOption, option])
	getSolutionPaths()

def getSolutionPaths():
	for solution in SOLUTIONS:
		path = [solution[0]]
		parent = solution[1]
		notAtRoot = True
		# find the parent of the parent until the root is reached
		while notAtRoot:
			#find parent state
			for state in STATES_ARCHIVE:
				if state[0] == parent: 
					path.append(parent)
					if state[1] == 0:
						notAtRoot = False
					parent = state[1]
					break
		SOLUTION_PATHS.append(path)

#recursive version (not used because memory will run out faster)
def dfs(option):
	#count = count + 1
	# Stop the loop if option is a repeat or the solution
	print option
	if optionIsNotNew(option):
		return
	if optionIsSolution(option):
		SOLUTIONS.append(option)
		return
	# add option to statelist
	STATES_ARCHIVE.append(option)
	# Loop all options while recusevely going deeper in 
	# the "tree" of possibilities
	for newOption in allMoves(option):
		dfs(newOption)

def allMoves(option):
	return [option +1, option - 1]
	
def optionIsNotNew(option):
	# kijk in de tree van Pim
	# BS:
	for state in STATES_ARCHIVE:
		if state[0] == option: 
			return True
	return False


def optionIsSolution(option):
	# Verzin hier iets voor, gewoon als alle dingen van rode auto tot uitgang
	# vrij zijn. 
	if option in [8,13]:
		return True
	return False
	
if __name__ == '__main__':
	main()