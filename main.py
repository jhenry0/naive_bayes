import json
import js
import math

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities

def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

with open('json_temp.json') as json_file:
    data = json.load(json_file)
    input = js.document.querySelector("#predicao").value
    inputVector = input.split(",")

    for x in range(len(inputVector)):
	    inputVector[x] = float(inputVector[x])
	 
    inputVector.append("?")
    result = predict(data, inputVector)
    print('Prediction: {0}'.format(result)) 

    html = js.document.querySelector(".predicao")
    if not html:
        html = js.document.createElement("div")
        html.classList.add("predicao")
        html.innerHTML = "<p>A prediçao é: "+ result+"</p>"
        js.document.body.append(html)  
    html.innerHTML = "<p>A prediçao é: "+ result+"</p>"