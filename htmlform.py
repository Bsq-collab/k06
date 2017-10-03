from flask import Flask, render_template, request
app = Flask(__name__)

#Bayan Berri
# SoftDev1 pd7
#k06 -- Echo echo echo
#2017-10-03

#assign following fxn to run when root route requested
@app.route("/")

def formfunct():
    print app;
'''    print request.headers;
    print request.method;
    print request.args;
    print request.form;'''
    return render_template("form.html");
"""
EXPERIMENT PRINT STATEMENTS

@app.route("/auth")
def authenticate():
    print "\n\n\n"
    print "***DIAG: this Flask obj***"
   ## print app
    print "***DIAG: request obj"
    #print request
    print "***DIAG: request.args***"
    #print request.args
   # print "***DIAG: request form"
    print "form"
   # print request.form
"""
@app.route("/hi")#this line redirects user after submitting the form
def sayHi():
    return render_template("hello.html", name= request.args["nombre"])
#sets name blank in the html hello file to the user input.

if __name__ == "__main__":
    app.debug = True
    app.run()
    
