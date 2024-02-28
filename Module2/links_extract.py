import os
import re
from ply import lex, yacc
from urllib.request import Request, urlopen

main_list = []
WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"

### DEFINING TOKENS ###
tokens = ('OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDIV', 'CLOSEDIV', 'OPENUL', 'CLOSEUL', 'OPENLI', 'CLOSELI', 'GARBAGE')
t_ignore = '\t'

# Create folders for timelines and responses if they don't exist
TIMELINE_FOLDER = 'timeline'
RESPONSE_FOLDER = 'response'
if not os.path.exists(TIMELINE_FOLDER):
    os.makedirs(TIMELINE_FOLDER)
if not os.path.exists(RESPONSE_FOLDER):
    os.makedirs(RESPONSE_FOLDER)

# Function to save links to a text file
def save_links(links):
    existing_links = set()
    # Check if the file exists
    if os.path.exists('links.txt'):
        # Read existing links from the file
        with open('links.txt', 'r') as file:
            existing_links.update(file.read().splitlines())

    # Add new links to the existing set
    existing_links.update(links)
    
    # Write the links back to the text file
    with open('links.txt', 'w') as file:
        for link in existing_links:
            file.write(link + '\n')



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


def t_OPENHEADER(t):
    r'<h2[^>]*>'
    return t


def t_CLOSEHEADER(t):
    r'</h2[^>]*>'
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


def t_CLOSELI(t):
    r'</li[^>]*>'
    return t


def t_GARBAGE(t):
    r'<[^>]*>'


def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
# GRAMMAR RULES


def p_start(p):
    '''start : orderedlist'''
    p[0] = p[1]


def p_orderedlist(p):
    '''orderedlist : OPENLI OPENHREF CONTENT CLOSEHREF'''
    if len(p) == 5:
        if (re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b', p[3]) \
                and ('timeline' in p[2].lower() or 'response' in p[2].lower())) \
                and re.search(r'\b\d{4}\b', p[2]):
            main_list.append(p[2])
        elif re.search(r'_of_the_COVID-19_pandemic_in_(\d{4})', p[2]):
            main_list.append(p[2])

def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    pass


def save_html(file_name, folder_name, html_content):
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML saved: {file_path}")


def download_html(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
        else:
            print(f"Failed to download HTML from URL: {url}")
            return None
    except Exception as e:
        print(f"Failed to download HTML from URL: {url}. Error: {e}")
        return None


def main():
    file_obj = open('jan2020.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

    extracted_links = []
    for link in main_list:
        # Extract the URL from the anchor tag
        match = re.search(r'href="([^"]+)"', link)
        if match:
            extracted_links.append(match.group(1))

    # Save links to a text file
    save_links(extracted_links)

    # Download HTML files into respective folders
    for link in extracted_links:
        full_url = WIKIPEDIA_BASE_URL + link
        folder_name = TIMELINE_FOLDER if 'timeline' in link.lower() else RESPONSE_FOLDER
        print(f"Downloading HTML from URL: {full_url}")
        
        # Combine regular expressions to extract both response and timeline links
        match_response = re.search(r'_to_the_COVID-19_pandemic_in_(\w+)_([0-9]{4})', link)
        match_timeline = re.search(r'_of_the_COVID-19_pandemic_in_(\w+)?_?(\d{4})', link)
        
        if match_response:
            month, year = match_response.groups()
            # This is a response link
            folder_name = RESPONSE_FOLDER
            prefix = 'R'
        elif match_timeline:
            month, year = match_timeline.groups()
            if not month:
                month = ""
            # This is a timeline link
            folder_name = TIMELINE_FOLDER
            prefix = 'T'
        else:
            print(f"Neither response nor timeline link: {link}")
            continue
        
        # Adjust file_name based on the presence of month
        if month:
            file_name = f"{prefix}_{month}_{year}.html"
        else:
            file_name = f"{prefix}_{year}.html"

        print(f"Saving HTML file: {file_name} to folder: {folder_name}")
        
        html_content = download_html(full_url)
        if html_content:
            save_html(file_name, folder_name, html_content)
        else:
            print(f"Failed to download HTML content from URL: {full_url}")

if __name__ == '__main__':
    main()