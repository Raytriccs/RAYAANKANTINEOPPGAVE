from flask import Flask 

app = Flask(__name__) 

#Ruten ti lhjemsiden
@app.route('/')
def index():
	return "Hello, Kantina!"

#Kjør appen hvis name = main
if __name__ == "__main__":
    app.run() 