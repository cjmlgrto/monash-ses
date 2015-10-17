__author__ = 'xav_work'


def promptCommand(lowest,highest):
	valid = False
	while not valid:
		try:
			command = input("\nEnter a number to choose from above: ")
			if command != "" and int(command) >= lowest and int(command) <= highest:
				return command
				valid = True
			else:
				print("\nError! Please try again.")
		except ValueError:
			print("\nError! Please try again.")