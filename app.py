from  flask import  Flask

app= Flask(__name__)
@app.route('/<int:name>')
def new( name):
    return f"{ name} My name  is  Pranit"


if __name__ == '__main__':
    app.run(debug=True)