from flask import Flask, render_template, url_for, flash, redirect, request, session
import svo2
from forms import RegistrationForm, LoginForm, PostForm
app = Flask(__name__)
global_text = None
x: ...
app.config['SECRET_KEY'] = '854a9d6cf0b9bc8c3ce9934d3f1439de'


posts = [
    {
        'author': 'Rohan Rao',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'February 9, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'February 10, 2021'
    }
]
#
# @app.route("/")
# def home():
#     return render_template("login.html")


@app.route("/", methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def home():
    global global_text
    # return render_template('home.html', posts=posts)
    # return render_template('home.html')
    if request.method != "POST":
        # return redirect(url_for("user"))

        return render_template("login.html")

    text = request.form["nm"]
    global_text = text
    return redirect(url_for("user", usr=text))    

@app.route("/user")
def user():
        text = svo2.main(global_text)
        # print(global_text)
        bias = round(abs(text['compound']*100), 2)
        neg_intent = text['neg']*100
        pos_intent = text['pos']*100
        polarity = (bias, neg_intent, pos_intent)
        # return f"""
        #     <h1>Overall Bias: {bias}% </h1>
        #         <body>Negative Intent: {neg_intent}%</body>
        #             <br>
        #         <body>Positive Intent: {pos_intent}%</body>
        # """
        return render_template("user.html", bias=bias, neg=neg_intent, pos=pos_intent, text=global_text)
# return f"""
# {% extends "layout.html" %}
# {% block content%}
#     <h1>About Page</h1>
#     <body>
#     </body>
# {% endblock content %}
# """

@app.route("/about")
def about():
    return render_template('about.html', title='About')





#
# @app.route("/login", methods=['GET', 'POST'])
# def new_post():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("login.html")

# @app.route("/register", methods=['GET', 'POST'])
# def register():-----------
#     global x
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         x = redirect(url_for('home'))
#         print(x, "This is x")
#         print(x, "This is x")
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)
#
#
# @app.route("/login")
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
for _ in range(1, 10):
    print(10)

