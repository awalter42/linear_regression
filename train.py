import matplotlib.pyplot as plt
from statistics import mean
import numpy as np


def estimatePrice(mileage, model):
	return (model.getTheta0() + (model.getTheta1() * mileage))


class Model:

	def __init__(self):
		self.theta0 = 9000
		self.theta1 = -0.1
		self.learningRate = 0.01
		self.nb_itter = 0

		self.file = input('File with dataset: ')
		try:
			self.originalTab = self._fillTab()
		except:
			print("There has been a problem with the file you sent")
			return -1
		self.tab = self._standardize()

		self.loopTrain(1000)


	def __str__(self):
		return(f"""
file = {self.file}
theta0 = {self.theta0}
theta1 = {self.theta1}
learning rate = {self.learningRate}
iteration = {self.nb_itter}
""")


	def getNbItter(self):
		return (self.nb_itter)

	def getFile(self):
		return (self.file)

	def getTheta0(self):
		return (self.theta0)


	def getTheta1(self):
		return (self.theta1)


	def _fillTab(self):
		file = open(self.file, "r")
		file.readline()
		tab = []
		for line in file:
			splitted = line.split(",")
			splitted[0] = int(splitted[0])
			splitted[1] = int(splitted[1])
			# splitted[1] = 1000
			tab.append(splitted)
		return (tab)


	def _standardize(self):
		mile = [self.originalTab[i][0] for i in range(len(self.originalTab))]
		price = [self.originalTab[i][1] for i in range(len(self.originalTab))]
		mean_val = mean(mile)

		variance = 0
		for i in range(len(mile)):
			variance += (mile[i] - mean_val)**2
		variance /= len(mile)
		stan_dev = variance**(1/2)
		for i in range(len(mile)):
			mile[i] = (mile[i] - mean_val)/stan_dev

		print(mean_val, stan_dev)

		new_tab = [[mile[i], price[i]] for i in range(len(mile))]
		return new_tab


	def meanSquareError(self):
		mse = sum((estimatePrice(self.tab[i][0], self) - self.tab[i][1]) ** 2 for i in range (len(self.tab)))
		mse /= 2 * len(self.tab)
		return (mse)


	def loopTrain(self, iterations):
		for _ in range(iterations):
			self._training()


	def _training(self):
		tmpTheta0 = sum(estimatePrice(self.tab[i][0], self) - self.tab[i][1] for i in range(len(self.tab)))
		tmpTheta1 = sum((estimatePrice(self.tab[i][0], self) - self.tab[i][1]) * self.tab[i][0] for i in range(len(self.tab)))

		tmpTheta0 /= len(self.tab)	
		tmpTheta1 /= len(self.tab)

		# if self.nb_itter % 10 == 0:
		# 	print (tmpTheta0, tmpTheta1)

		tmpTheta0 *= self.learningRate
		tmpTheta1 *= self.learningRate

		self.theta0 -= tmpTheta0
		self.theta1 -= tmpTheta1

		self.nb_itter += 1

		# theta0 = ((theta0 * (nb_values - len(tab))) + (tmpTheta0 * len(tab))) / nb_values
		# theta1 = ((theta1 * (nb_values - len(tab))) + (tmpTheta1 * len(tab))) / nb_values


	def showData(self, show_func):
		fig, ax = plt.subplots()

		mileage = []
		price = []
		for row in self.originalTab:
			mileage.append(row[0])
			price.append(row[1])

		ma = np.arange(0, 250000, 1000)
		func = estimatePrice(ma, self)

		ax.scatter(mileage, price)
		if show_func is True:
			ax.plot(ma, func)
		plt.show()
