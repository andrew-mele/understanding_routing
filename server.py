from flask import Flask
app = Flask(__name__)

@app.route('/')

def helloWorld():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def sayHi(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:hello>')
def repeatHello(hello,num):
    return f"Hello {hello * num}"

@app.route('/repeat/<int:num>/<string:bye>')
def repeatbye(bye,num):
    return f"bye {bye * num} "

@app.route('/repeat/<int:num>/<string:dogs>')
def repeatDogs(dogs,num):
    return f"Dogs {dogs * num}"

if __name__=="__main__":
    app.run(debug=True)
