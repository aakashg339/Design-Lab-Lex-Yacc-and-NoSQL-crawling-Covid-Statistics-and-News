import ply.lex as lex
import ply.yacc as yacc
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

valueString = ''
valueList = []

def p_start(p):
    '''start : portionToExtract'''
    p[0] = p[1]

def p_portionToExtract(p):
    '''portionToExtract : OPENHTWO CONTENT CONTENT CLOSEHTWO dataToExtract'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_dataToExtract(p):
    '''dataToExtract : OPENP content CLOSEP dataToExtract
                        | empty'''
    p[0] = p[1] + p[2]


def p_content(p):
    '''content : CONTENT
                | CONTENT CONTENT
                | CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT'''
    p[0] = p[1]
    
    global valueString
    valueString = ""

    for i in range(1, len(p)):
        valueString += p[i] + " "

    valueList.append(valueString)

def p_empty(p):
    'empty :'
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
        with open("tokens.txt", "w") as file:
            for tok in lexer:
                file.write(str(tok) + "\n")
            file.close()
        # for tok in lexer:
        #     print(tok)
        parser = yacc.yacc()
        parser.parse(data)
    except IOError:
        print("Error opening file webpage.html")

    

    # Appending the extracted data to a file
    filename = "extractedData/"+filename+".txt"
    with open(filename, "a") as file:
        for value in valueList:
            file.write(value + "\n")
        file.close()

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