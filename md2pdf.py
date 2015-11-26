from markdown import markdown
import pdfkit
import codecs

input_filename = 'README.md'
html_template_filename = 'html_template.html'
output_filename = 'README.pdf'
css = ['6aika.css', ]

with codecs.open(html_template_filename, 'r', encoding='utf8') as f:
    html_template = f.read()

with codecs.open(input_filename, 'r', encoding='utf8') as f:
    html_text = markdown(f.read(), output_format='html4')

#print html_text 
#print html_template 

html = html_template.replace('###CONTENT###', html_text)

print html

options = {
    'page-size': 'A4',
    'margin-top': '3cm',
    'margin-right': '3cm',
    'margin-bottom': '3cm',
    'margin-left': '3cm',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_string(html, output_filename, options=options, css=css)
