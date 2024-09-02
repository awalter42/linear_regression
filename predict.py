from train import fillTab
import matplotlib.pyplot as plt
import numpy as np


def show_data(tab):
	fig, ax = plt.subplots()

	mileage = []
	for row in tab:
		mileage.append(row[0])
	price = []
	for row in tab:
		price.append(row[1])

	ma = np.arange(0, 250000, 1000)
	func = estimatePrice(ma, theta0, theta1)

	ax.scatter(mileage, price)
	ax.plot(ma, func)
	plt.show()


def estimatePrice(mileage, theta0, theta1):
	return (theta0 + (theta1 * mileage))


if __name__ == '__main__':
	tab = fillTab("data.csv")
	tab.sort()

	theta0 = float(input("theta0= "))
	theta1 = float(input("theta1= "))
	value = int(input("For what mileage? "))

	est = estimatePrice (value, theta0, theta1)
	print(est)

	show_data(tab)
