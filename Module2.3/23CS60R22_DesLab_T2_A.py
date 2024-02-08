import ply.lex as lex
import ply.yacc as yacc

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

def p_start(p):
    '''start : month
             | monthDataul
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
        text = p[2] + "\n" + text

def p_monthDateData(p):
    '''monthDateData : OPENHTHREE CONTENT CONTENT CLOSEHTHREE empty '''
    print("-> monthDateData parsed")

def p_monthDataul(p):
    '''monthDataul : OPENUL dataLi CLOSEUL monthDataul
                   | empty'''
    #print("-> monthDataul parsed")

def p_dataLi(p):
    '''dataLi : OPENLI dataInEachLi CLOSELI dataLi
              | empty'''
    #print("-> dataLi parsed")
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



# def p_handleheader(p):
#     '''handleheader : OPENHEADER CONTENT CLOSEHEADER handleheader
#                     | OPENHEADER CONTENT CLOSEHEADER dataCell
#                     | OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER dataCell
#                     | OPENHEADER CONTENT CLOSEHEADER dataCell2
#                     | empty'''
#     # if len(p) == 5:
#     #   print(p[2], end =" ")

# def p_dataCell(p):
#     '''dataCell : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA dataCell
#     		    | OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA dataCell
#                 | OPENDATA CONTENT CLOSEDATA dataCell
#                 | OPENDATA CLOSEDATA dataCell
#                 | OPENDATA OPENHREF CONTENT CLOSEHREF CONTENT CLOSEDATA dataCell
#                 | OPENDATA CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CLOSEDATA dataCell
#                 | OPENDATA CONTENT CONTENT OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CLOSEDATA dataCell
#                 | OPENDATA CONTENT CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CLOSEDATA dataCell
#                 | OPENDATA skiptag CLOSEDATA dataCell
#                 | empty'''
#     global isOpening
#     if len(p) == 5 and p[2] is not None:
#         if isOpening:
#             print("Opening: ", p[2])
#             isOpening = False
#         else:
#             print("Closing: ", p[2])
#     if len(p) == 8:
#         print("Host city: ",p[3], p[5])
#     if len(p) == 10:
#         print("Motto: ", p[2])
#     if len(p) == 11:
#         print("Athletes: ", p[2], '(', p[3], ')')
#     if len(p) == 14:
#         print("Nations: ", p[2], p[3], p[5], p[7], p[9], p[11])
 
# def p_dataCell2(p):
#     '''dataCell2 : OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CONTENT CLOSEDATA dataCell2
#                 | empty'''
#     if len(p) == 10:
#         print("Events: ", p[2], p[4], p[6], '(',p[7], ')')

# def p_handlerow(p):
#     '''handlerow : OPENROW handleheader CLOSEROW handlerow 
#                  | OPENROW dataCell CLOSEROW handlerow
#                  | empty'''
#     print("-> handlerow parsed")

# def p_table(p):
#     '''table : BEGINTABLE skiptag OPENTABLE handlerow '''
#     print("-> table parsed")

def p_empty(p):
    '''empty :'''
    pass

# def p_content(p):
#     '''content : CONTENT
#                | empty'''
#     p[0] = p[1]
#     print("-> content parsed")

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def main():
    try:
        # Opening file India_Timeline_of_the_COVID-19_pandemic_in_India_(January%E2%80%93May_2020).html in folder webpages
        file_obj= open("webpages/India_Timeline_of_the_COVID-19_pandemic_in_India_(January%E2%80%93May_2020).html", "r")
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

    global text
    global textList
    print(textList)

if __name__ == '__main__':
    main()