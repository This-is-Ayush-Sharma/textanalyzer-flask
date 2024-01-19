from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def indexPage():
    return render_template('index.html', result = "Your result will be displayed here")

@app.post("/form")
def task():
    
    text = request.form['text']
    action = request.form['action']
    answer = ""

    if(action == "countchr"):
        # logic for character count 
        answer = f"the number of characters are {len(text)}"
    if(action == "countws"):
        # logic for count white spaces
        answer = f"the number of white space are {text.count(' ')}"

    return render_template('index.html', result = answer)
    
app.run(debug=True)