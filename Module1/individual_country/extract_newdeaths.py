import ply.lex as lex
import ply.yacc as yacc

### DEFINING TOKENS###
tokens = ('BEGINTABLE', 'OPENSCRIPT', 'CLOSESCRIPT', 'CATEGORY', 'SPECIFICYAXIS', 'SPECIFICDATA',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW', 'OPENLINK', 'IMAGE', 'OPENSMALL', 'CLOSESMALL', 'OPENBR', 'OPENBOLD', 'CLOSEBOLD',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF', 'OPENNOBR', 'CLOSENOBR',
          'CONTENT', 'OPENDATA', 'CLOSEDATA', 'OPENSPAN', 'OPENTABLEHEADER', 'CLOSETABLEHEADER',
          'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE', 'GARBAGE', 'OPENH4', 'CLOSEH4', 'OPENH3', 'CLOSEH3', 'OPENTABLE_TABLE', 'CLOSETABLE_TABLE')
t_ignore = ' \t\n'

############### Tokenizer Rules################


def t_BEGINTABLE(t):
    r'Daily.New.Deaths.in.'
    return t


def t_SPECIFICYAXIS(t):
    r'yAxis'
    return t

def t_SPECIFICDATA(t):
    r'data'
    return t

def t_CATEGORY(t):
    r'categories'
    return t


def t_OPENSCRIPT(t):
    r'<script[^>]*>'
    return t


def t_CLOSESCRIPT(t):
    r'</script[^>]*>'
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
    return t


def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t


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
               | OPENDIV skiptag
                | CLOSEDIV skiptag
                | OPENH3 skiptag
                | CLOSEH3 skiptag
               | empty'''


# .................................................................................


def p_dates(p):
    ''' dates : CONTENT CONTENT dates
              | CONTENT SPECIFICYAXIS
              | SPECIFICYAXIS
    '''
    if len(p)==4:
        s=f'{p[1]} {p[2]}'
        env_date.append(s)

def p_spec_data(p):
    '''spec_data : SPECIFICDATA CONTENT
                    | empty'''
    if len(p)==3:
        # print("..")
        # print(p[2])
        s=p[2]
        env_value.append(s)


def p_script_handle(p):
    '''script_handle : CONTENT script_handle
                     | OPENSCRIPT script_handle
                     | CLOSESCRIPT script_handle
                     | CATEGORY dates script_handle
                     | spec_data script_handle
                     | empty'''



def p_handlescript(p):
    '''handlescript : OPENSCRIPT script_handle CLOSESCRIPT
                    | empty'''


def p_table(p):
    '''table : BEGINTABLE skiptag handlescript'''


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


env_value = []
env_date = []


def main():
    file_obj = open('./webpage.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    # lexer.input(data)
    # for tok in lexer:
    #     print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()


    x_1=env_value[0].split(',')
    x_2=env_value[1].split(',')
    x_3=env_value[2].split(',')
    sss=["new deaths"]
    data=[]
    env_date.reverse()
    for i in range(len(env_date)):
        env_date[i]=env_date[i][0:(env_date[i].rindex(',')-1)]
        # data.append([env_date[i],x_1[i],x_2[i],x_3[i]])
        data.append([env_date[i],sss[0],x_1[i]])

    # print(data)

    # # print((env_value[0]))
    with open("./output_newdeaths.txt", "w") as f:
        for i in data:
            f.write(str(i))
            f.write("\n")
    


if __name__ == '__main__':
    main()
