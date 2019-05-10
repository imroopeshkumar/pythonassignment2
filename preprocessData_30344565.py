import re

def preprocessLine(inputLine):
	#preprocess the data in each line
	#write your code here
	pass


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def splitFile(inputFile, outputFile_question, outputFile_answer):
	#preprocess the original file, and split them into two files.
	#please call preprocessLine() function within this function
	#write you code here


	with open(inputFile, 'r', encoding='utf-8') as f:
		rows_with_header = f.readlines()
		# print(len(lines))lines
		rows_without_header = rows_with_header[1:5447]
		# print(lines1[5446])
		filtered_rows = [];
		for var in rows_without_header:
			# print(var)
			temp = var.replace('&amp;', '&').replace('&quot;', '"').replace('&apos;', '\'').replace('&gt;','>').replace('&lt;','<').replace('&#xA;', ' ').replace('&#xAD', ' ')
			# temp2 = temp.replace('<p>','').replace('<h3>', '').replace('<div>', '').replace('</p>','').replace('</h3>', '').replace('</div>', '')
			# var.replace('&lt;', '<')
			# print(temp)
			temp2 = cleanhtml(temp)
			print(temp2)
			filtered_rows.append(temp2)
		# with open('draftfile.txt', 'w+') as x:
		# 	print(filtered_rows)
		# 	for y in filtered_rows:
		# 		x.write(y)
		# print(filtered_rows)

	pass





if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"
	splitFile(f_data, f_question, f_answer)
