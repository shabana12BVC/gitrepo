from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/")
def hello_flask():
    return "merge conflict created "
@app.route("/index")
def index():
    return render_template("index.html")
    

if __name__=='__main__':
    
    app.run (debug = True)

    
    
    
    
    