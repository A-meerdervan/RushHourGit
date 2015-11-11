

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

def getSolutionPaths():
	for solution in SOLUTIONS:
		path = [solution[0]]
		parent = solution[1]
		notAtRoot = True
		# find the parent of the parent until the root is reached
		while notAtRoot:
			#find parent state
			parentOfParrent = STATES_ARCHIVE.getParent(parent) # dit is [ding zelf, zijn pap]
			path.append(parent)
			if parentIsRoot():
				notAtRoot = False
			parent = parentOfParrent
		SOLUTION_PATHS.append(path)