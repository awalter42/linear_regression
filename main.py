from train import Model
from predict import estimatePrice
import sys

WARNING = '\033[93m'
ENDC = '\033[0m'


if __name__ == '__main__':
	models = {}
	nb_trained = 0

	print(WARNING + "WARNING: if you want to show the data plot, remember to export QT_QPA_PLATFORM=wayland\n\n" + ENDC)

	try:
		while True:
			print ("""What do you want to do?
				1 - Create and train a model
				2 - Train a model for more iterations
				3 - Use a model to predict a value
				4 - Get the plot of a model
				5 - Get the values of a model
				6 - Save the thetas of a model
				7 - Exit the program
				""")
			action = int(input('> '))

			match action:
				case 1:
					new_model = Model()
					if new_model.error:
						print('\nThere has been a problem with the training\n')
						continue
					models[nb_trained] = new_model
					nb_trained += 1

				case 2:
					keys = list(models.keys())
					keys.sort()
					if keys == []:
						print('A model has yet to be created')
						continue

					print('Please select a model: \n')
					for k in keys:
						m = models[k]
						print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

					index = int(input('\n> '))
					if index not in keys:
						print('Next time, please choose an index that match an existing model')
						continue

					itter = int(input('Number of iterations: '))
					models[index].loopTrain(itter)

				case 3:
					keys = list(models.keys())
					keys.sort()
					if keys == []:
						print('A model has yet to be created')
						continue

					print('Please select a model: \n')
					for k in keys:
						m = models[k]
						print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

					index = int(input('\n> '))
					if index not in keys:
						print('Next time, please choose an index that match an existing model')
						continue

					mileage = int(input('mileage of the car: '))
					if mileage < 0:
						print ("A mileage cannot be negative")
						continue
					t0 = models[index].getTheta0()
					t1 = models[index].getTheta1()
					mTab, pTab = models[index].getOriginalTabs()
					est = estimatePrice(mileage, t0, t1, mTab, pTab)
					if est < 0:
						print('\nThis is probably a bad purchase')
					print(f'The price is estimated to be {est} units (no intel on the currency)\n')


				case 4:
					keys = list(models.keys())
					keys.sort()
					if keys == []:
						print('A model has yet to be created')
						continue

					print('Please select a model: \n')
					for k in keys:
						m = models[k]
						print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

					index = int(input('\n> '))
					if index not in keys:
						print('Next time, please choose an index that match an existing model')
						continue

					models[index].showData()


				case 5:
					keys = list(models.keys())
					keys.sort()
					if keys == []:
						print('A model has yet to be created')
						continue

					print('Please select a model: \n')
					for k in keys:
						m = models[k]
						print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

					index = int(input('\n> '))
					if index not in keys:
						print('Next time, please choose an index that match an existing model')
						continue
					print(models[index])


				case 6:
					keys = list(models.keys())
					keys.sort()
					if keys == []:
						print('A model has yet to be created')
						continue

					print('Please select a model: \n')
					for k in keys:
						m = models[k]
						print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

					index = int(input('\n> '))
					if index not in keys:
						print('Next time, please choose an index that match an existing model')
						continue
					models[index].saveThetas()

				case 7:
					sys.exit()

				case _:
					print('Make sure to use a number that is valid')

	except SystemExit:
		sys.exit()
	except:
		print('\nThere has been a problem in the inputs you gave\n')
		sys.exit()