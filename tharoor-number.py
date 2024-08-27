import os
import sys



def calculate_tharoor_number(text: str):
	return 0


def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print(f"Usage:\n\tpython3 tharoor-number.py filepath")
		return

	filepaths = args
	for filepath in filepaths:
		tharoor_number = calculate_tharoor_number("Example")
		print(f"File {filepath} has a Tharoor Number of {tharoor_number}")


if __name__ == '__main__':
	main()
