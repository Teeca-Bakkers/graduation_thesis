#url_check.py

import re
import webbrowser

def url_check(url):
	pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
	if re.match(pattern, url):
		webbrowser.open(url)
	
	pass

