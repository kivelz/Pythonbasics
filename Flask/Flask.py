from flask import Flask, request

app= Flask(__name__)

@app.route('/')
def helloworld():
    return '<h1>hello world</h1>'
@app.route('/greet/', defaults = {'name': 'nobody'})
@app.route('/greet/<name>')
def greet(name):
        return 'Good Morning, ' + name

@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return 'Total is  ' + str(x+y)

@app.route('/sayhello', methods = ['GET', 'POST'])
def say_hello():
    name = request.args.get('name') or request.args.form.get('name')
    return 'Hello' + name;
    

if __name__ == '__main__':
    app.run(debug=True)
    
