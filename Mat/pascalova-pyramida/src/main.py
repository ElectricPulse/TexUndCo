def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result


LATEX_FORMULA_WIDTH = 0.7
LATEX_FORMULA_HEIGHT = 1

def getCode(layers):
	formulasCode = []
	resultsCode = []
	xOffset = 0
	yOffset = 0

	for layer in range(0, layers + 1):
		layerOffset = xOffset
		for i in range(0, layer + 1):
			formulaCode = (
			'\\node at (' + str(layerOffset) + ', '
			+ str(yOffset) + ') {$' + str(layer) + ' \choose ' + str(i) + '$};'
			)
			result = factorial(layer)/factorial(layer - i)/factorial(i)
			resultCode = (
			'\\node at (' + str(layerOffset) + ', '
			+ str(yOffset) + ') {$' + str(result) + '$};'
			)
			formulasCode.append(formulaCode)
			resultsCode.append(resultCode)
			layerOffset += LATEX_FORMULA_WIDTH
		xOffset -= LATEX_FORMULA_WIDTH/2
		yOffset -= LATEX_FORMULA_HEIGHT
	
	return ['\n'.join(formulasCode), '\n'.join(resultsCode)]

code = getCode(10)

with open('results.tikz', 'w') as results_file:
	results_file.write(code[0])

with open('formulas.tikz', 'w') as formulas_file:
	formulas_file.write(code[1])
