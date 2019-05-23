import preprocessData_30344565 as PD
import pandas as pd
import re


class Parser:
    """docstring for ClassName"""
    # class initializer
    def __init__(self, inputString):
        self.inputString = inputString
        self.ID = self.getID()
        self.type = self.getPostType()
        self.dateQuarter = self.getDateQuarter()
        self.cleanBody = self.getCleanedBody()

    # modify print method according to specification
    def __str__(self):
        # print ID, Question/Answer/Others, creation date, the main content
        # write your code here
        result = 'ID: ' + str(self.getID()) + '\n' + 'Post Type: ' + str(
            self.getPostType()) + '\n' + 'Creation Date Quarter: ' + str(
            self.getDateQuarter()) + '\n' + 'The Cleaned Content: ' + str(self.getCleanedBody())
        return result
        pass

    # get id of post
    def getID(self):
        # write your code here
        id = self.inputString.split('Id="')[1].split('"')[0]
        return id;

    # get post type id of post
    def getPostType(self):
        # write your code here
        posttype = '';
        postidtypeid = self.inputString.split('PostTypeId="')[1].split('"')[0]
        postidtypeid = int(postidtypeid)
        if (postidtypeid == 1):
            posttype = 'Question'
        elif (postidtypeid == 2):
            posttype = 'Answer'
        elif (postidtypeid > 2):
            posttype = 'Other'
        else:
            raise ValueError

        return posttype;

    #get date quarter
    def getDateQuarter(self):
        # write your code here
        creationdate = self.inputString.split('CreationDate="')[1].split('"')[0]
        dateasdate = pd.to_datetime(creationdate)
        quarter = '';
        if (dateasdate.month < 4):
            quarter = 'Q1';
        elif (dateasdate.month > 3 and dateasdate.month < 7):
            quarter = 'Q2';
        elif (dateasdate.month > 6 and dateasdate.month < 10):
            quarter = 'Q3'
        elif (dateasdate.month > 9):
            quarter = 'Q4';
        else:
            raise TypeError

        result = str(dateasdate.year) + quarter
        return result;

    # use function from task1 to clean
    def getCleanedBody(self):
        # write your code here
        postobj = PD.lineSubber(self.inputString)
        return postobj.Body

    # get vocabulary size of line
    def getVocabularySize(self):
        # write your code here
        bodystring = self.getCleanedBody();
        subbedbodystring = re.sub(r'[^\w\s]', '', bodystring)

        bodystringlist = subbedbodystring.split()
        bodystringlist = list(dict.fromkeys(bodystringlist))

        return len(bodystringlist)


# to check if function is working
x = r'<row Id="2481" PostTypeId="1" CreationDate="2016-04-07T18:11:33.793" Body="&lt;p&gt;In $200 price range, should I be looking at cards from AMD or Nvidia?&lt;/p&gt;&#xA;” />'
y = Parser(x)
# print('done')
# print(y.getVocabularySize())
# print(y.getID())
# print(y.getPostType())
# print(y.getDateQuarter())
# print(y.getCleanedBody())
#
# print(y)
