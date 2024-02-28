import os
import ply.lex as lex
import ply.yacc as yacc
import re
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENH3', 'CLOSEH3', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN', 'OPENPARA', 'CLOSEPARA', 'OPENH2','CLOSEH2',
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

def t_OPENH2(t):
    r'<h2[^>]*>'
    return t

def t_CLOSEH2(t):
    r'</h2[^>]*>'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
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

para = ''

####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : handleheader dataCell
             | handleheader dataLI
             | empty'''
    p[0] = p[1]


def p_dataContent(p):
    '''dataContent : CONTENT
                   | CONTENT CONTENT
                   | CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT
                   | CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT CONTENT'''
    global para
    if(len(p)==2):
        if(not re.search(r'edit|tibet|see also|references', p[1],re.IGNORECASE)):
            para+=(p[1]+'\n')
    elif(len(p)==3):
        para+=(p[1]+p[2]+'\n')
    elif(len(p)==4):
        para+=(p[1]+p[2]+p[3]+'\n')
    elif(len(p)==5):
        para+=(p[1]+p[2]+p[3]+p[4]+'\n')
    elif(len(p)==6):
        para+=(p[1]+p[2]+p[3]+p[4]+p[5]+'\n')
    elif(len(p)==7):
        para+=(p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+'\n')
    elif(len(p)==8):
        para+=(p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+'\n')
        

def p_reLI(p):
    '''reLI : dataContent dataHREF reLI
            | dataHREF dataContent reLI
            | '''

def p_dataLI(p):
    '''dataLI : OPENLI reLI CLOSELI dataLI
              | '''

def p_skiptag(p):
    '''skiptag : OPENHREF skiptag
               | CLOSEHREF skiptag
               | CONTENT skiptag
               | empty'''
def p_dataSpan(p):
    '''dataSpan : OPENSPAN CLOSESPAN
                | OPENSPAN dataContent CLOSESPAN
                | OPENSPAN
                | CLOSESPAN'''

def p_dataHREF(p):
    '''dataHREF : OPENHREF dataContent CLOSEHREF
                | OPENHREF CONTENT CONTENT CONTENT CLOSEHREF
                | OPENHREF dataSpan CLOSEHREF'''

def p_dataCell(p):
    '''dataCell : OPENPARA dataContent dataHREF dataContent dataHREF CLOSEPARA 
                | OPENPARA dataContent dataHREF CLOSEPARA
                |'''

def p_handleheader(p):
    '''handleheader : OPENH2 dataSpan dataSpan dataSpan dataSpan dataHREF dataSpan dataSpan CLOSEH2
                    | OPENH3 dataSpan dataSpan dataSpan dataHREF dataSpan dataSpan CLOSEH3
                    '''
    

        
def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

def main():
    if not os.path.exists('extracted'):
        os.makedirs('extracted')

    for file in os.listdir('response'):
        if(file.endswith('.html')):
            match = re.match(r'R_(\w+)_(\d{4})', file)
            if match:
                month = match.group(1)
                year = match.group(2)
                year_folder = os.path.join('extracted',year)
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                
                file_path = os.path.join('response', file)
                output_file_path = os.path.join(year_folder, f"{month}.txt")                    


                file_obj= open(file_path,'r',encoding="utf-8")
                data=file_obj.read()
                lexer = lex.lex()
                lexer.input(data)
                for tok in lexer:
                    print(tok)
                parser = yacc.yacc()
                parser.parse(data)
                file_obj.close()

                global para
                with open(output_file_path,'w') as output_file:
                    output_file.write(para)
                    para=''

if __name__ == '__main__':
    main()