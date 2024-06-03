def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result


FORMULA_WIDTH = 1
FORMULA_HEIGHT = 1
RESULT_WIDTH = 1
RESULT_HEIGHT = 1
MARKER_OFFSET = 2.5

def getCode(layers):
	formulasCode = []
	resultsCode = []

	markerX = layers/2 * RESULT_WIDTH + MARKER_OFFSET
	for layer in range(0, layers + 1):
		for i in range(0, layer + 1):
			formulaX = -(i - layer/2) * FORMULA_WIDTH
			formulaY = -layer * FORMULA_HEIGHT
			resultX = -(i - layer/2) * RESULT_WIDTH
			resultY = -layer * RESULT_HEIGHT
			formulaCode = (
				'\\node at (' + str(formulaX) + ', '
				+ str(formulaY) + ') {$' + str(layer) + ' \choose ' + str(i) + '$};'
			)
			result = int(factorial(layer)/factorial(layer - i)/factorial(i))
			resultCode = (
				'\\node at (' + str(resultX) + ', '
				+ str(resultY) + ') {$' + str(result) + '$};'
			)
			formulasCode.append(formulaCode)
			resultsCode.append(resultCode)

		markerY = - layer * RESULT_HEIGHT
		markerCmd = (
			'\\node at (' + str(markerX) + ', ' + str(markerY) + ') {$n = ' + str(layer) + '$};'
		)
		resultsCode.append(markerCmd)
		formulasCode.append(markerCmd)
	
	return ['\n'.join(formulasCode), '\n'.join(resultsCode)]

code = getCode(10)

with open('formulas.tikz', 'w') as formulas_file:
	formulas_file.write(code[0])

with open('results.tikz', 'w') as results_file:
	results_file.write(code[1])
