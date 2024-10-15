def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result


FORMULA_WIDTH = 3.1
FORMULA_HEIGHT = 2.15
RESULT_WIDTH = 1.3
RESULT_HEIGHT = 1
MARKER_OFFSET = 2.5

def getCode(layers):
	formulasCode = []
	resultsCode = []

	markerX = layers/2 * FORMULA_WIDTH + MARKER_OFFSET
	for layer in range(0, layers + 1):
		for i in range(0, layer + 1):
			formulaX = (i - layer/2) * FORMULA_WIDTH
			formulaY = -layer * FORMULA_HEIGHT
			resultX = (i - layer/2) * RESULT_WIDTH
			resultY = -layer * RESULT_HEIGHT
			result = int(factorial(layer)/factorial(layer - i)/factorial(i))
			scale = 1.7 - len(str(result)) * 0.1
			formulaCode = (
				'\\node[anchor=center] at (' + str(formulaX) + ', '
				+ str(formulaY)
				+ ') {\scalebox{' + str(scale) + '}{$\\binom{'
				+ str(layer) + '}{'
				 + str(i) + '}${\\raisebox{.3ex}{\\footnotesize=}$'
				+ str(result) + '$}}};'
			)
			resultCode = (
				'\\node[anchor=center] at (' + str(resultX) + ', '
				+ str(resultY) + ') {$' + str(result) + '$};'
			)
			formulasCode.append(formulaCode)
			resultsCode.append(resultCode)

		markerY = -layer * FORMULA_HEIGHT + 0.12
		markerCmd = (
			'\\node[anchor=center] at ('
			+ str(markerX) + ', ' + str(markerY) + ') {\scalebox{1.2}{$n = ' 
			+ str(layer) + '$}};'
		)
		resultsCode.append(markerCmd)
		formulasCode.append(markerCmd)
	
	return ['\n'.join(formulasCode), '\n'.join(resultsCode)]

code = getCode(15)

with open('formulas.tikz', 'w') as formulas_file:
	formulas_file.write(code[0])

with open('results.tikz', 'w') as results_file:
	results_file.write(code[1])
