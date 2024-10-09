from train import normalizeElem
import sys


def getData(file):
	try:
		file = open(file, "r")
		file.readline()
	except:
		sys.exit()
	mileage = []
	price = []
	for line in file:
		splitted = line.split(",")
		mileage.append(float(splitted[0]))
		price.append(float(splitted[1]))
	file.close()
	return mileage, price


def estimatePrice(toEst, theta0, theta1, mileage, price):
	toEst = normalizeElem(mileage, float(toEst))
	est = theta0 + (theta1 * toEst)
	return round(est, 2)


if __name__ == '__main__':
	file = input('Where is the data? ')
	try:
		mileage, price = getData(file)
	except:
		print("There has been a problem fetching the datas")
		sys.exit()
	try:
		theta0, theta1 = getData('thetas.csv')
		theta0, theta1 = theta0[0], theta1[0]
	except SystemExit:
		theta0, theta1 = 0, 0
		print("Default values (0, 0) will be used, make sure to train a model to get predictions\n")
	except:
		print("Unexpected error occured")

	toEst = int(input('mileage to estimate: '))
	if toEst < 0:
		print('mileage cannot be negative')
		exit()

	est = estimatePrice(toEst, theta0, theta1, mileage, price)
	if est < 0:
		print('\nThis is probably a bad purchase')
	print(f'\nThe price is estimated to be {est} units (no intel on the currency)')
