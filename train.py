import matplotlib.pyplot as plt
from statistics import mean


def estimatePrice(mileage, model):
	return (model.getTheta0() + (model.getTheta1() * mileage))


def	normalizeElem(list, elem):
	return ((elem - min(list)) / (max(list) - min(list)))


class Model:

	def __init__(self):
		self.theta0 = 0
		self.theta1 = 0
		self.learningRate = 0.1
		self.nb_itter = 0

		self.file = input('File with dataset: ')
		self.error = False
		try:
			self.originalTab = self.__fillTab()
		except:
			self.error = True
			return None
		self.tab = self.__normalize()

		self.loopTrain(1000)


	def __str__(self):
		return(f"""
file = {self.file}
learning rate = {self.learningRate}
iteration = {self.nb_itter}
accuracy = {self.R2Score()}
""")

	def getOriginalTabs(self):
		mileage = [self.originalTab[i][0] for i in range(len(self.originalTab))]
		price = [self.originalTab[i][1] for i in range(len(self.originalTab))]

		return mileage, price


	def getNbItter(self):
		return (self.nb_itter)

	def getFile(self):
		return (self.file)

	def getTheta0(self):
		return (self.theta0)


	def getTheta1(self):
		return (self.theta1)


	def __fillTab(self):
		file = open(self.file, "r")
		file.readline()
		tab = []
		for line in file:
			splitted = line.split(",")
			splitted[0] = int(splitted[0])
			splitted[1] = int(splitted[1])
			tab.append(splitted)
		return (tab)


	def __normalize(self):
		mileages = [self.originalTab[i][0] for i in range(len(self.originalTab))]
		prices = [self.originalTab[i][1] for i in range(len(self.originalTab))]

		x = []
		y = []
		minM = min(mileages)
		maxM = max(mileages)
		for mileage in mileages:
			x.append((mileage - minM) / (maxM - minM))
		# minP = min(prices)
		# maxP = max(prices)
		for price in prices:
			y.append(price)
		new_tab = [[x[i], y[i]] for i in range(len(x))]
		return new_tab


	def R2Score(self):
		prices = [self.tab[i][1] for i in range(len(self.tab))]
		meanVal = mean(prices)
		RSS = sum((p - estimatePrice(m, self))**2 for m, p in self.tab)
		TSS = sum((p - meanVal)**2 for m, p in self.tab)
		return (1 - RSS/TSS)


	def loopTrain(self, iterations):
		for _ in range(iterations):
			self.__training()


	def __training(self):
		tmpTheta0 = sum((estimatePrice(m, self) - p) for m, p in self.tab)
		tmpTheta1 = sum(((estimatePrice(m, self) - p) * m) for m, p in self.tab)
		
		tmpTheta0 /= len(self.tab)	
		tmpTheta1 /= len(self.tab)

		tmpTheta0 *= self.learningRate
		tmpTheta1 *= self.learningRate

		self.theta0 -= tmpTheta0
		self.theta1 -= tmpTheta1

		self.nb_itter += 1


	def saveThetas(self):
		try:
			f = open('thetas.csv', 'w')
			f.write('theta0,theta1\n')
			f.write(f'{self.theta0},{self.theta1}')
			f.close()
		except:
			print('there has been a problem saving the thetas')


	def showData(self):
		fig, ax = plt.subplots()

		mileage = []
		price = []
		for row in self.originalTab:
			mileage.append(row[0])
			price.append(row[1])

		funcLineX = [float(min(mileage)), float(max(mileage))]
		funcLineY = []
		for e in funcLineX:
			e = estimatePrice(normalizeElem(mileage, e), self)
			funcLineY.append(e)

		ax.plot(mileage, price, 'bo', funcLineX, funcLineY, 'r-')
		plt.show()
