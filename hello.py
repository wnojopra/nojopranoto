import random
import os
from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    background-color:#E6B85C;
    text-align:center;
}
img {
    margin: 20px;
    width: 100px;
    height: 100px;
    -webkit-animation-name: spin;
    -webkit-animation-duration: 4000ms;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
    -moz-animation-name: spin;
    -moz-animation-duration: 4000ms;
    -moz-animation-iteration-count: infinite;
    -moz-animation-timing-function: linear;
    -ms-animation-name: spin;
    -ms-animation-duration: 4000ms;
    -ms-animation-iteration-count: infinite;
    -ms-animation-timing-function: linear;
    
    animation-name: spin;
    animation-duration: 4000ms;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}
@-ms-keyframes spin {
    from { -ms-transform: rotate(0deg); }
    to { -ms-transform: rotate(360deg); }
}
@-moz-keyframes spin {
    from { -moz-transform: rotate(0deg); }
    to { -moz-transform: rotate(360deg); }
}
@-webkit-keyframes spin {
    from { -webkit-transform: rotate(0deg); }
    to { -webkit-transform: rotate(360deg); }
}
@keyframes spin {
    from {
        transform:rotate(0deg);
    }
    to {
        transform:rotate(360deg);
    }
}
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