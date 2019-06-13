from flask import Flask, request
import Flask.handler1

app= Flask(__name__)

app.add_url_rule('/', view_func=Flask.handler1.helloworld)
app.add_url_rule('/greet/', defaults={'name': 'nobody'}, view_func=Flask.handler1.greet)


if __name__ == '__main__':
    app.run(debug=True)
    
