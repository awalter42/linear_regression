from train import normalizeElem, denormalizeElem


def getData(file):
	try:
		file = open(file, "r")
		file.readline()
	except:
		print(f'There has been a problem when fetching the file {file}')
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
	value = theta0 + (theta1 * toEst)
	est = denormalizeElem(price, value)
	return est


if __name__ == '__main__':
	file = input('Where is the data? ')
	mileage, price = getData(file)
	theta0, theta1 = getData('thetas.csv')
	theta0, theta1 = theta0[0], theta1[0]

	toEst = int(input('mileage to estimate: '))
	if toEst < 0:
		print('mileage cannot be negative')
		exit()

	est = estimatePrice(toEst, theta0, theta1, mileage, price)
	if est < 0:
		print('\nThis is probably a bad purchase')
	print(f'The price is estimated to be {est} units (no intel on the currency)\n')
