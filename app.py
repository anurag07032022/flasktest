import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return 'Web App with Python Flask using Jenkinks Trial Number:1'
    


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000) #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.


#app.run()
#76.251.77.235