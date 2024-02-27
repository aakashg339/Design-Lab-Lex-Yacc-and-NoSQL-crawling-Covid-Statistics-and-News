import ply.lex as lex
import ply.yacc as yacc
import re
import os
import sys

###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE', 
'OPENHTWO', 'CLOSEHTWO', 'OPENHTHREE', 'CLOSEHTHREE', 'OPENUL', 'CLOSEUL',
'OPENLI', 'CLOSELI', 'OPENP', 'CLOSEP')
t_ignore = '\t'

###############Tokenizer Rules################
def t_BEGINTABLE(t):
     r'<caption.class="infobox-title.summary">Games.of.the.XXXII.Olympiad</caption>'
     return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'


def t_CLOSEROW(t):
    r'</tr[^>]*>'


def t_OPENHEADER(t):
    r'<th[^>]*>'


def t_CLOSEHEADER(t):
    r'</th[^>]*>'


def t_OPENHREF(t):
    r'<a[^>]*>'

def t_CLOSEHREF(t):
    r'</a[^>]*>'

def t_OPENDATA(t):
    r'<td[^>]*>'


def t_CLOSEDATA(t):
    r'</td[^>]*>'


def t_CONTENT(t):
    r'[A-Za-z0-9,\u2013\-. ]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'

def t_CLOSESTYLE(t):
    r'</style[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_OPENHTWO(t):
    r'<h2[^>]*>'
    return t

def t_CLOSEHTWO(t):
    r'</h2[^>]*>'
    return t

def t_OPENHTHREE(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEHTHREE(t):
    r'</h3[^>]*>'
    return t

def t_OPENUL(t):
    r'<ul[^>]*>'
    return t

def t_CLOSEUL(t):
    r'</ul[^>]*>'
    return t

def t_OPENLI(t):
    r'<li[^>]*>'
    return t

def t_CLOSELI(t):
    r'</li[^>]*>'
    return t

def t_OPENP(t):
    r'<p[^>]*>'
    return t

def t_CLOSEP(t):
    r'</p[^>]*>'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
text = ""
textList = []
textDict = {}

def p_start(p):
    '''start : month
             | monthDataul
             | monthDateData
             | empty'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | empty'''
    
def p_month(p):
    '''month : OPENHTWO CONTENT CONTENT CLOSEHTWO empty
                | OPENHTWO CONTENT CONTENT CLOSEHTWO monthDataul 
                |'''
    
    global text

    if len(p) == 6:
        # print(p[2])
        text = p[2] + "\n" + text

def p_monthDateData(p):
    '''monthDateData : OPENHTHREE CONTENT CONTENT CLOSEHTHREE openpData'''
    #print("-> monthDateData parsed")
    # if len(p) == 6:
    #     print(p[2])

    global text
    text = p[2] + "," + text + ","

def p_openpData(p):
    '''openpData : OPENP dataInEachLi CLOSEP monthDataul'''
    print("-> openpData parsed")

def p_monthDataul(p):
    '''monthDataul : OPENUL dataLi CLOSEUL monthDataul
                   | empty'''
    print("-> monthDataul parsed")

def p_dataLi(p):
    '''dataLi : OPENLI dataInEachLi CLOSELI dataLi
              | empty'''
    #print("-> dataLi parsed")dataInEachLi
    global text
    if len(p) == 5:
        textList.append(text)
        text = ""

def p_dataInEachLi(p):
    '''dataInEachLi : CONTENT dataInEachLi
                    | empty'''
    
    global text
    if len(p) == 3:
        text = p[1] + text

    #print("-> dataInEachLi parsed")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    pass

#########DRIVER FUNCTION#######
def readAndParse(filename):
    try:
        # Opening file India_Timeline_of_the_COVID-19_pandemic_in_India_(January%E2%80%93May_2020).html in folder webpages
        urls = "webpages/"+filename+".html"
        file_obj= open(urls, "r")
        data=file_obj.read()
        file_obj.close()
        lexer = lex.lex()
        lexer.input(data)

        # Writing the tokens to a file
        with open("tokens.txt", "a") as file:
            for tok in lexer:
                file.write(str(tok) + "\n")
            file.close()
        # for tok in lexer:
        #     print(tok)
        parser = yacc.yacc(write_tables=0)
        parser.parse(data)
        #parser.parse(data)
    except IOError:
        print("Error opening file webpage.html")

    global text
    global textList
    
    # Create folder  if not exists name 'extractedData'
    if not os.path.exists("extractedData"):
        os.makedirs("extractedData")
    # write data to file
    filename = "extractedData/"+filename+".txt"
    with open(filename, "w") as file:
        for i in textList:
            # Seperate each i as per a regex pattern. Pattern would be something like On 7 March, <some text> In place of march and date there can be other months and dates as well. In place of some text there can be other valid sentences.
            regexSeperateSentence = re.compile(r'On\s\d+\s\w+')
            matches = regexSeperateSentence.findall(i)

            if len(matches) == 0:
                file.write(i + "\n")
                continue

            # write the matches to file in reverse order
            for match in matches[::-1]:
                # find the complete sentence and write it to file
                regexEachSentence = re.compile(r''+match+'.*')
                match = regexEachSentence.findall(i)[0]
                file.write(match + "\n")
                # remove the sentence from i
                i = i.replace(match, "")

        file.close()

    text = ""
    textList = []

def main():
    # Reading filename from argument
    filename = sys.argv[1]

    filename = filename.strip()

    # Read keys from filename (key) dataUrls.txt
    fileNames = []

    fileNames.append(filename)

    print(fileNames)

    # for each filename, read and parse the file
    for filename in fileNames:
        readAndParse(filename)

if __name__ == '__main__':
    main()