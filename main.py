from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/")
def hello_flask():
    return "welcome"
@app.route("/index")
def index():
    pass
    

if __name__=='__main__':
    
    app.run (debug = True)

    
    
    
    
    