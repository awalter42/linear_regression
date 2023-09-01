from math import exp
import matplotlib.pyplot as plt

theta0 = 0
theta1 = 0
learningRate = 1
nb_values = 0

def fillTab(file_name):
	file = open(file_name, "r")
	file.readline()
	tab = []
	for line in file:
		splitted = line.split(",")
		splitted[0] = int(splitted[0])
		splitted[1] = int(splitted[1][:-1])
		tab.append(splitted)
	return (tab)

def estimatePrice(mileage):
	return (theta0 + (theta1 * mileage))

def training(tab):
	global theta0
	global theta1
	global nb_values
	global learningRate
	tmpTheta0 = 0
	tmpTheta1 = 0

	for mileage, price in tab:
		tmpTheta0 += estimatePrice(mileage) - price
		tmpTheta1 += (estimatePrice(mileage) - price) * mileage
		nb_values += 1

	# print (learningRate, tmpTheta0, tmpTheta1)
	# learningRate = 1 * (1 **((1 + nb_values) // 1))
	learningRate = 0.5 * exp(-(1 * nb_values))
	tmpTheta0 = (1 / len(tab)) * tmpTheta0
	tmpTheta0 *= learningRate
	tmpTheta1 = (1 / len(tab)) * tmpTheta1
	tmpTheta1 *= learningRate

	theta0 = ((theta0 * (nb_values - len(tab))) + (tmpTheta0 * len(tab))) / nb_values
	theta1 = ((theta1 * (nb_values - len(tab))) + (tmpTheta1 * len(tab))) / nb_values

if __name__ == '__main__':
	tab = fillTab("data.csv")
	training(tab)
	print (estimatePrice (20000))
