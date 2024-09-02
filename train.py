from statistics import mean
import numpy as np


def fillTab(file_name):
	file = open(file_name, "r")
	file.readline()
	tab = []
	for line in file:
		splitted = line.split(",")
		splitted[0] = int(splitted[0])
		splitted[1] = int(splitted[1])
		# splitted[1] = 1000
		tab.append(splitted)
	return (tab)


def standardize(tab):
	mile = [tab[i][0] for i in range(len(tab))]
	price = [tab[i][1] for i in range(len(tab))]
	mean_val = mean(mile)

	variance = 0
	for i in range(len(mile)):
		variance += (mile[i] - mean_val)**2
	variance /= len(mile)

	stan_dev = variance**(1/2)

	for i in range(len(mile)):
		mile[i] = (mile[i] - mean_val)/stan_dev

	new_tab = [[mile[i], price[i]] for i in range(len(mile))]
	return new_tab, mean_val, stan_dev


def destandardize(est, mean_val, stan_dev):
	return est * stan_dev + mean_val


def estimatePrice(mileage):
	return (theta0 + (theta1 * mileage))


def meanSquareError(tab):
	mse = sum((estimatePrice(tab[i][0]) - tab[i][1]) ** 2 for i in range (len(tab)))
	mse /= 2 * len(tab)
	print(mse)


def training(tab):
	global theta0
	global theta1
	global nb_itter
	global nb_values

	nb_itter += 1


	tmpTheta0 = sum(estimatePrice(tab[i][0]) - tab[i][1] for i in range(len(tab)))
	tmpTheta1 = sum((estimatePrice(tab[i][0]) - tab[i][1]) * tab[i][0] for i in range(len(tab)))
	nb_values += len(tab)


	learningRate = 0.01
	tmpTheta0 /= len(tab)	
	tmpTheta1 /= len(tab)

	if nb_itter < 10:
		print (tmpTheta0, tmpTheta1)

	tmpTheta0 *= learningRate
	tmpTheta1 *= learningRate

	theta0 -= tmpTheta0
	theta1 -= tmpTheta1

	# theta0 = ((theta0 * (nb_values - len(tab))) + (tmpTheta0 * len(tab))) / nb_values
	# theta1 = ((theta1 * (nb_values - len(tab))) + (tmpTheta1 * len(tab))) / nb_values


if __name__ == '__main__':
	theta0 = 0
	theta1 = 0
	nb_values = 0
	nb_itter = 0

	tab = fillTab("data.csv")
	# tab.sort()
	# tab[0][1] = 1001
	stan_tab, mean_val, stan_dev = standardize(tab)

	for _ in range (1000):
		training(stan_tab)

	print (theta0, theta1)
