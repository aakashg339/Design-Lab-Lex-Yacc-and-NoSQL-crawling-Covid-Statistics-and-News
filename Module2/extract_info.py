import ply.lex as lex
import ply.yacc as yacc

###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN', 'OPENPARA', 'CLOSEPARA', 'OPENH3','CLOSEH3',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV','OPENUL','CLOSEUL','OPENLI','CLOSELI','GARBAGE')
t_ignore = '\t'

###############Tokenizer Rules################
def t_CONTENT(t):
    r'[A-Za-z0-9, ]+'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

def t_OPENLI(t):
    r'<li[^>]*>'
    return t

def t_OPENPARA(t):
    r'<p[^>]*>'
    return t

def t_CLOSEPARA(t):
    r'</p[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</h3[^>]*>'
    return t

def t_OPENSPAN(t):
    r'<span[^>]*>'
    return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    return t

def t_CLOSELI(t):
    r'</li[^>]*>'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : orderedlist'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : OPENHREF skiptag
               | CLOSEHREF skiptag
               | CONTENT skiptag
               | empty'''


def p_handleheader(p):
    '''handleheader : OPENHEADER OPENSPAN CONTENT CLOSESPAN CLOSEHEADER
                    | '''
    if(len(p)==6):
        print(p[3])
        


def p_dataCell(p):
    '''dataCell : OPENPARA OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF OPENHREF CONTENT CONTENT CONTENT CLOSEHREF OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CLOSEPARA
                | OPENPARA CONTENT OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CLOSEHREF CONTENT CONTENT CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CLOSEPARA
                | OPENPARA CONTENT CONTENT CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CONTENT CONTENT CONTENT CONTENT OPENHREF OPENSPAN CONTENT CLOSESPAN CLOSEHREF CONTENT CLOSEPARA
                | OPENPARA CONTENT CONTENT OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF OPENHREF CONTENT CONTENT CONTENT CLOSEHREF OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CONTENT CONTENT CLOSEHREF CLOSEPARA'''
    if(len(p)==26):
        print(p[3]+p[5]+p[7]+p[9])
    elif(len(p)==27):
        print(p[2]+p[4]+p[10]+p[16]+p[17]+p[18])
    elif(len(p)==39):
        print(p[2]+p[3]+p[5]+p[7]+p[9]+p[11]+p[12]+p[13]+p[14]+p[15]+p[16]+p[32])
        
def p_orderedlist(p):
    '''orderedlist : handleheader dataCell'''

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

def main():
    file_obj= open('webpage_download.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
         print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

if __name__ == '__main__':
    main()