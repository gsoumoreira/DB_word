import pycurl
from io import BytesIO
import re

b_obj = BytesIO()
crl = pycurl.Curl()

# URL list:
url_list = ['https://en.wikipedia.org/wiki/Brazil',
            'https://en.wikipedia.org/wiki/Brazil',
            'https://en.wikipedia.org/wiki/Brazil',
            'https://en.wikipedia.org/wiki/Brazil',
            'https://en.wikipedia.org/wiki/Brazil',
            'https://en.wikipedia.org/wiki/Brazil',]

# Set URL value
crl.setopt(crl.URL, 'https://en.wikipedia.org/wiki/Brazil')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer
crl.perform()

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters)
get_body = b_obj.getvalue()

# Cleaning the HTML
def cleanhtml(raw_html):
  # cleanr = re.compile('<.*?>')
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

word_list = str.split(cleanhtml(get_body))

# Exporting the html as a file
country = 'Brazil'

with open("html_data/"+country+".txt", "w") as output:
    for row in word_list:
        output.write(str(row) + '\n')
