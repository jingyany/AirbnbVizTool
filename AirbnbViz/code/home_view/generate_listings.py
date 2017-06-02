import pandas as pd

def generate_listings():
	data1 = pd.read_csv("../../data/listings.csv")
	listing = data1.to_json(orient='records')
	file = open("../../html/js/listings.js", "w")
	file.write( "var listings = " + listing)

def main():
	generate_listings()

if __name__ == '__main__':
	main()