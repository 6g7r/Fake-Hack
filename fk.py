from flask import Flask
print("""
────────▄█▀▄
──────▄██▀▀▀▀▄
────▄███▀▀▀▀▀▀▀▄
──▄████▀▀▀▀▀▀▀▀▀▀▄
▄█████▀▀▀▀▀▀▀▀▀▀▀▀▀▄
insta = @6g7r_here

""")
name = input('your name : ')
app = Flask(__name__)
yehia = f'''                                                                                             
<html dir="rtl">

<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>Hacked By 6G7R</title>
</head>

<body text="#FF0000" bgcolor="#000000">

<p align="center"><font size="6">Hacked By {name} </font></p>
&nbsp;




‏<p align="center">
‏<img border="" src="https://i0.wp.com/myotakuworld.com/wp-content/uploads/2020/01/Surprisingly-Scary-Anime.gif?resize=500%2C324&ssl=1"
‏width="389" height="400"></p></body>

</html>                                                                                        
'''


@app.route('/')
def hack():
    return (yehia)

app.run(port=5000)
