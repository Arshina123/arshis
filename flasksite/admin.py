from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=False)

@app.route('/books')
def books():
    books=[{'name':'book1','author':'author1','cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoswOIOhQPzdfofzYIJ0xGD2tsluOonPY861x1CftQ&s'},{'name':'book2','author':'author2','cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoswOIOhQPzdfofzYIJ0xGD2tsluOonPY861x1CftQ&s'},{'name':'book1','author':'author1','cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoswOIOhQPzdfofzYIJ0xGD2tsluOonPY861x1CftQ&s'}]
    return render_template('books.html',books=books)
app.run(debug=True)
