from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # creating instance and naming it as app


@app.route('/')  # @ shows how it should execute the function hello_world() when the user visits the root URL
def hello_world():
    # returning a string that will be displayed in the browser
    return "<center>Hello, World!<br><a href='/register'>Register</a></center>"


@app.route('/success/<name>/<roll_no>/<year>')
def success(name, roll_no, year):
    # rendering the template and passing the values to it
    return render_template('success.html', name=name, roll_no=roll_no, year=year)


@app.route('/register', methods=['GET'])
def register_get():
    return render_template('register.html')


@app.route('/register', methods=['POST'])  # specifying that this route will only accept POST requests
def register():
    # getting the values from the form
    name = request.form['name']
    roll_no = request.form['roll_no']
    year = request.form['year']

    # redirecting to the success page and passing the values
    return redirect(url_for('success', name=name, roll_no=roll_no, year=year))


if __name__ == '__main__':
    # debug=True allows the server to reload itself on code changes and show an interactive debugger in the browser if an error occurs
    app.run(debug=True)

