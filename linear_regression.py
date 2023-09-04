from math import exp
import matplotlib.pyplot as plt
import numpy as np

theta0 = 0
theta1 = 0
learningRate = 1
nb_values = 0

def show_data(tab):
	fig, ax = plt.subplots()

	mileage = []
	for row in tab:
		mileage.append(row[0])
	price = []
	for row in tab:
		price.append(row[1])

	ma = np.arange(0, 250000, 1000)
	func = estimatePrice(ma)
	# func = no(ma)

	ax.scatter(mileage, price)
	ax.plot(ma, func)
	plt.show()

def fillTab(file_name):
	file = open(file_name, "r")
	file.readline()
	tab = []
	for line in file:
		splitted = line.split(",")
		splitted[0] = int(splitted[0])
		splitted[1] = int(splitted[1][:-1])
		# splitted[1] = 1000
		tab.append(splitted)
	return (tab)

def estimatePrice(mileage):
	return (theta0 + (theta1 * mileage))

# def no(mileage):
	# return (9000 + (-0.025 * mileage))

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

	learningRate0 = (1.4 * (1 **((1 + nb_values) // 1))) / len(tab)
	learningRate1 = (0.4 * (0.4 **((1 + nb_values) // 1))) / len(tab)
	tmpTheta0 *= learningRate0
	tmpTheta1 *= learningRate1

	tmpTheta0 = abs(tmpTheta0)
	print (tmpTheta0)

	theta0 = ((theta0 * (nb_values - len(tab))) + (tmpTheta0 * len(tab))) / nb_values
	theta1 = ((theta1 * (nb_values - len(tab))) + (tmpTheta1 * len(tab))) / nb_values

if __name__ == '__main__':
	tab = fillTab("data.csv")
	tab.sort()
	training(tab)

	print (estimatePrice (240000))

	show_data(tab)
