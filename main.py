from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/")
def hello_flask():
    return "changed for merging"
@app.route("/index")
def index():
    pass
    

if __name__=='__main__':
    
    app.run (debug = True)

    
    
    
    
    