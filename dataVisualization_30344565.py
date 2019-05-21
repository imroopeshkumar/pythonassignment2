import preprocessData_30344565 as PD
import parser_30344565 as PS



def visualizeWordDistribution(inputFile, outputImage):
	#write your code here
	with open(inputFile, 'r', encoding='utf-8') as f:
		rows_with_header = f.readlines()
		rows_without_header = rows_with_header[1:5447]
		vocsizeindicator = [0,0,0,0,0,0,0,0,0,0,0]
		for var in rows_without_header:
			try:
				parser = PS.Parser(var)
				parsedvar = parser.getVocabularySize()

				x = parsedvar // 10
				if(x>=10):
					vocsizeindicator[10]+=1
				else:
					vocsizeindicator[x]+=1
			except:
				continue

	print(vocsizeindicator)


def visualizePostNumberTrend(inputFile, outputImage):
	#write your code here
	pass;


if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"

	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
