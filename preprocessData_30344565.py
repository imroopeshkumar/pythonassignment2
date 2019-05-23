import re


# class to hold variables after processing line to make task 2 easy
class postVariables:
    def __init__(self, postTypeId, creationDate, rowId, Body):
        self.postTypeId = postTypeId
        self.creationDate = creationDate
        self.rowId = rowId
        self.Body = Body

#pre process line and remove only clean body using regex
def preprocessLine(inputLine):
    # preprocess the data in each line
    # write your code here
    cleanre = re.compile('<.*?>') #regex to remove all html tags
    processedLine = re.sub(cleanre, '', inputLine)
    return processedLine

# substitute given substitutions and extract data to make task2 easy
def lineSubber(var):
    postidtype = var.split('PostTypeId="')[1].split('"')[0]
    rowid = var.split('Id="')[1].split('"')[0]
    creationDate = var.split('CreationDate="')[1].split('"')[0]

    temp = var.replace('&amp;', '&').replace('&quot;', '"').replace('&apos;', '\'').replace('&gt;',
                                                                                            '>').replace('&lt;',
                                                                                                         '<').replace(
        '&#xA;', ' ').replace('&#xAD', ' ')

    temp2 = preprocessLine(temp)
    temp2 = temp2.replace('/>', '').replace('"', '')
    post = postVariables(postidtype, creationDate, rowid, temp2)
    return post;

# split file into two files question and answer
def splitFile(inputFile, outputFile_question, outputFile_answer):
    # preprocess the original file, and split them preprocessLineinto two files.
    # please call preprocessLine() function within this function
    # write you code here

    with open(inputFile, 'r', encoding='utf-8') as f:
        rows_with_header = f.readlines()
        # print(len(lines))lines
        rows_without_header = rows_with_header[1:5447]
        # # print(lines1[5446])
        listofposts = [];
        # postObjects = []
        for var in rows_without_header:
            try:
                # print(var)
                post = lineSubber(var)
                listofposts.append(post)
            except Exception as e:
                print(e)
                continue;

    x = 1
    for var in listofposts:
        x += 1
        print('pass:' + str(x))
        if (int(var.postTypeId) == 1):
            with open(outputFile_question, 'a', encoding='utf-8') as question_file:
                question_file.write(var.Body)
        elif(int(var.postTypeId) == 2):
            with open(outputFile_answer, 'a', encoding='utf-8') as answer_file:
                answer_file.write(var.Body)
        else:
            pass


#main function
if __name__ == "__main__":
    f_data = "data.xml"
    f_question = "question.txt"
    f_answer = "answer.txt"
    splitFile(f_data, f_question, f_answer)
