import random
import os
from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<style>
body{background-color:#E6B85C; text-align:center;}
</style>
<title>
Willy Nojopranoto
</title>
</head>
<body>

<h2>Just hanging out.</h2>
<img src="https://scontent.fsnc1-1.fna.fbcdn.net/hphotos-xfa1/t31.0-8/1026053_10151567907326843_1432800181_o.jpg" alt="Pointer Hangin" style="width:418px;height:558px;">

</body>
</html>
"""

@app.route('/')
def hello():
	try:
	    return HTML_TEMPLATE
	except Exception as e:
		print e
		raise