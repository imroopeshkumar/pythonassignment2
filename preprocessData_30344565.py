import re

class postVariables:
    def __init__(self, postTypeId, creationDate, rowId, Body):
        self.postTypeId = postTypeId
        self.creationDate = creationDate
        self.rowId = rowId
        self.Body = Body

def preprocessLine(inputLine):
    # preprocess the data in each line
    # write your code here
    cleanre = re.compile('<.*?>')
    processedLine = re.sub(cleanre, '', inputLine)
    return processedLine
    pass


def lineSubber(var):
    postidtype = var.split('PostTypeId="')[1].split('"')[0]
    rowid = var.split('Id="')[1].split('"')[0]
    creationDate = var.split('CreationDate="')[1].split('"')[0]
    # creationDate = 0
    # print(postidtype)
    temp = var.replace('&amp;', '&').replace('&quot;', '"').replace('&apos;', '\'').replace('&gt;',
                                                                                            '>').replace('&lt;',
                                                                                                         '<').replace(
        '&#xA;', ' ').replace('&#xAD', ' ')
    # temp2 = temp.replace('<p>','').replace('<h3>', '').replace('<div>', '').replace('</p>','').replace('</h3>', '').replace('</div>', '')
    # var.replace('&lt;', '<')
    # print(temp)
    temp2 = preprocessLine(temp)
    temp2 = temp2.replace('/>', '').replace('"', '')
    # print(temp2)
    post = postVariables(postidtype, creationDate, rowid, temp2)
    # filtered_rows.append(temp2)
    # postObjects.append(post)
    return post;

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

        # with open('draftfile.txt', 'w+', encoding="utf-8") as x:
        #     # print(filtered_rows)
        #     for var in filtered_rows:
        #         x.write(y)
        # print(filtered_rows)

    print('done')
    x = 1
    for var in listofposts:
        x += 1
        print('pass:' + str(x))
        if (int(var.postTypeId) == 1):
            with open('draftquestions.txt', 'a', encoding='utf-8') as question_file:
                question_file.write(var.Body)
        elif(int(var.postTypeId) == 2):
            with open('draftanswers.txt', 'a', encoding='utf-8') as question_file:
                question_file.write(var.Body)
        else:
            pass


    pass


if __name__ == "__main__":
    f_data = "data.xml"
    f_question = "question.txt"
    f_answer = "answer.txt"
    splitFile(f_data, f_question, f_answer)
