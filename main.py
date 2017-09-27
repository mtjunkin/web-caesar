from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "POST" action = "/">
        <label>
            Rotate by:
        <input name="rot" type="text" value=0 />
        </label>                     
         <textarea name="message">{0}</textarea>      
        
        <input type = "submit"/>
        
       </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot1 = int(request.form['rot'])
    text1 = request.form['message']
    encrypted_message = rotate_string(text1, rot1)
    return form.format(encrypted_message)
@app.route("/")
def index():
    return form.format('')

app.run()