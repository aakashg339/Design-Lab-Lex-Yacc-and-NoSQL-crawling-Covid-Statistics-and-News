import ply.lex as lex
import ply.yacc as yacc

### DEFINING TOKENS###
tokens = ('BEGINTABLE','BEGINTABLE2','BEGINTABLE3',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW', 'OPENLINK', 'IMAGE', 'OPENSMALL', 'CLOSESMALL', 'OPENBR', 'OPENBOLD', 'CLOSEBOLD',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF', 'OPENNOBR','CLOSENOBR',
          'CONTENT', 'OPENDATA', 'CLOSEDATA', 'OPENSPAN', 'OPENTABLEHEADER','CLOSETABLEHEADER',
          'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE', 'GARBAGE', 'OPENH4', 'CLOSEH4', 'OPENH3', 'CLOSEH3', 'OPENTABLE_TABLE', 'CLOSETABLE_TABLE')
t_ignore = ' \t\n'

############### Tokenizer Rules################


def t_BEGINTABLE(t):
    # r'International.grounds</span>'
    r'<div.class="tab-pane.".id="nav-yesterday2".role="tabpanel".aria-labelledby="nav-yesterday2-tab">'
    return t



def t_OPENNOBR(t):
    r'<nobr>'
    # return t

def t_CLOSENOBR(t):
    r'</nobr>'
    # return t

def t_OPENH4(t):
    r'<h4[^>]*>'
    return t


def t_CLOSEH4(t):
    r'</h4[^>]*>'
    return t


def t_OPENTABLE_TABLE(t):
    r'<table[^>]*>'
    return t


def t_CLOSETABLE_TABLE(t):
    r'</table[^>]*>'
    return t


def t_OPENH3(t):
    r'<h3[^>]*>'
    # return t


def t_CLOSEH3(t):
    r'</h3[^>]*>'
    # return t


def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t


def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t


def t_OPENROW(t):
    r'<tr[^>]*>'
    return t


def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENTABLEHEADER(t):
    r'<thead[^>]*>'
    return t


def t_CLOSETABLEHEADER(t):
    r'</thead[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t


def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t


def t_OPENHREF(t):
    r'<a[^>]*>'
    # return t


# def t_CLOSEHREF(t):
#     r'</a[^>]*>'
#     # return t


def t_OPENDATA(t):
    r'<td[^>]*>'
    return t


def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t


def t_CONTENT(t):
    # r'[A-Za-z0-9,./;& ]+'
    r'[A-Za-z0-9,./;& -]+'
    return t


def t_OPENDIV(t):
    r'<div[^>]*>'
    return t


def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t


def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t


def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    return t


def t_OPENSPAN(t):
    r'<span[^>]*>'
    # return t


def t_CLOSESPAN(t):
    r'</span[^>]*>'
    # return t


def t_OPENLINK(t):
    r'<link[^>]*>'
    # return t


def t_IMAGE(t):
    r'<img[^>]*>'
    # return t


def t_OPENBR(t):
    r'<br[^>] /*>'
    # return t


def t_OPENBOLD(t):
    r'<b[^>]*>'
    # return t


def t_CLOSEBOLD(t):
    r'</b[^>]*>'
    # return t


def t_GARBAGE(t):
    r'<[^>]*>'
    # return t


def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
    # GRAMMAR RULES


def p_start(p):
    '''start : table'''
    p[0] = p[1]


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | empty'''


def p_skiptable(p):
    '''skiptable : OPENTABLE skiptable
               | CLOSETABLE skiptable
               | OPENDATA skiptable
                | CLOSEDATA skiptable
                | OPENROW skiptable
                | CLOSEROW skiptable
                | OPENDIV skiptable
                | CLOSEDIV skiptable
                | CONTENT skiptable
               | empty'''

# .................................................................................

def p_headcontent(p):
    '''headcontent : CONTENT CONTENT
                    | CONTENT
                    | CONTENT CONTENT CONTENT CONTENT
                   | empty
    '''
    if len(p)==3:
        s=f'{p[1]} {p[2]}'
        env.append(s)
    if len(p)==2 and p[1] is not None:
        s=f'{p[1]}'
        env.append(s)
    if len(p)==2 and p[1] is  None:
        s=None
        env.append(s)
    if len(p)==5:
        s=f'{p[1]}{p[3]} {p[4]}'
        env.append(s)

def p_thead_data(p):
    '''thead_data : OPENHEADER headcontent CLOSEHEADER thead_data
                  | empty
    '''


def p_table_header(p):
    '''table_header : OPENROW thead_data CLOSEROW table_header
                    | empty
    '''


# .................................................................................

def p_rowcontent(p):
    '''rowcontent : CONTENT
                    | CONTENT CONTENT 
                    | empty
    '''
    if len(p)==3 :
        s=f'{p[1]} {p[2]}'
        env_2.append(s)
    if len(p)==2 and p[1] is not None:
        s=f'{p[1]}'
        env_2.append(s)
        # print(s)
    if len(p)==2 and p[1] is None:
        s=None
        env_2.append(s)
        # print(s)


def p_row_data(p):
    '''row_data : OPENDATA rowcontent CLOSEDATA row_data
                | empty
    '''


def p_row_handler(p):
    '''row_handler : OPENROW row_data CLOSEROW row_handler
                    | empty
    '''
    # if len(p)==5:
    #     s='######'
    #     env_2.append(s)
    
def p_fulltable(p):
    '''fulltable : OPENTABLEHEADER table_header CLOSETABLEHEADER fulltable
                | OPENTABLE row_handler CLOSETABLE fulltable

                | empty

    '''

def p_table(p):
    '''table : BEGINTABLE OPENDIV OPENTABLE_TABLE fulltable'''

def p_empty(p):
    '''empty :'''
    pass


def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]


def p_error(p):
    pass

######### DRIVER FUNCTION#######


env= []
env_2 = []

def main():
    file_obj = open('./webpage.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    print(env)
    print(env_2)

    with open("./output.txt", "w") as f:
        for item in env_2:
            f.write("%s\n" % item)


if __name__ == '__main__':
    main()
