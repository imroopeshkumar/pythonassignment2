import preprocessData_30344565 as PD
import parser_30344565 as PS
import matplotlib.pyplot as plt
import numpy as np

# plot graph to visualize word distribution
def visualizeWordDistribution(inputFile, outputImage):
    # write your code here
    with open(inputFile, 'r', encoding='utf-8') as f:
        rows_with_header = f.readlines()
        rows_without_header = rows_with_header[1:5447]
        vocsizeindicator = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # initialize array to count vocabulary size for each interval
        for var in rows_without_header:
            try:
                parser = PS.Parser(var)
                parsedvar = parser.getVocabularySize()

                x = parsedvar // 10
                if (x >= 10):
                    vocsizeindicator[10] += 1
                else:
                    vocsizeindicator[x] += 1
            except:
                continue

    print(vocsizeindicator)
    y_pos = np.arange(len(vocsizeindicator))
    plt.clf()

    plt.bar(y_pos, vocsizeindicator, align='center', alpha=0.5)
    plt.xticks(y_pos,
               ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', 'others'])
    plt.ylabel('Number of Posts')
    plt.title('Vocabulary size distribution')
    plt.xlabel('Vocabulary Size')

    plt.savefig(outputImage)

# visualize number of questions and answers over the quarters
def visualizePostNumberTrend(inputFile, outputImage):
    # write your code here
    q1a = 0
    q2a = 0
    q3a = 0
    q4a = 0
    q1q = 0
    q2q = 0
    q3q = 0
    q4q = 0
    with open(inputFile, 'r', encoding='utf-8') as f:
        rows_with_header = f.readlines()
        rows_without_header = rows_with_header[1:5447]
        for var in rows_without_header:
            try:
                parser = PS.Parser(var)
                parsedvar = parser.getDateQuarter()
                parsedvar = parsedvar[4:6]
                if parsedvar == 'Q1':
                    if (parser.getPostType() == 'Question'):
                        q1q += 1;
                    elif (parser.getPostType() == 'Answer'):
                        q1a += 1;
                    pass;
                elif parsedvar == 'Q2':
                    if (parser.getPostType() == 'Question'):
                        q2q += 1;
                    elif (parser.getPostType() == 'Answer'):
                        q2a += 1;
                    pass;
                elif parsedvar == 'Q3':
                    if (parser.getPostType() == 'Question'):
                        q3q += 1;
                    elif (parser.getPostType() == 'Answer'):
                        q3a += 1;
                    pass;
                elif parsedvar == 'Q4':
                    if (parser.getPostType() == 'Question'):
                        q4q += 1;
                    elif (parser.getPostType() == 'Answer'):
                        q4a += 1;
                    pass;
                else:
                    raise TypeError
            except Exception as e:
                print(e)
                continue;

        qs = [q1q,q2q,q3q,q4q]
        ans = [q1a,q2a,q3a,q4a]
        x = [0,1,2,3]
        y_pos = np.arange(len(qs))

        plt.clf()
        questions = plt.plot(x, qs, color = 'red', label = 'Questions')
        answers = plt.plot(x, ans, color = 'blue', label = 'Answers')
        # plt.xticks(y_pos, ['Q1', 'Q2', 'Q3', 'Q4'])
        plt.xticks(y_pos,['Q1', 'Q2', 'Q3', 'Q4'])
        plt.xlabel('Year Quarters')
        leg = plt.legend(framealpha=1, frameon=True)
        plt.savefig(outputImage)

# main function
if __name__ == "__main__":
    f_data = "data.xml"
    f_wordDistribution = "wordNumberDistribution.png"
    f_postTrend = "postNumberTrend.png"

    visualizeWordDistribution(f_data, f_wordDistribution)
    visualizePostNumberTrend(f_data, f_postTrend)
