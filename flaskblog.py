from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm,LoginForm

app =   Flask(__name__)
app.config['SECRET_KEY'] = '56e41a823eaabdd45381d52fbdf65b9b'

posts = [
    {
        'author':'Omkar Kadam',
        'title':'Blog-post-1',
        'content':'first-post-content',
        'date-published':'10 november,2020'
    },
    {
        'author':'bhalchandra kolekar',
        'title':'Blog-post-2',
        'content':'second-post-content',
        'date-published':'11 november,2020'
    }

]


@app.route('/')
@app.route('/home')
def Home():
    return render_template("home.html",posts = posts)

@app.route('/about')
def hello():
    return render_template("about.html")

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('Home'))
    return render_template('register.html',title='Register',form = form)

@app.route('/login')
def Login():
    form = LoginForm()
    return render_template('login.html',title='Login',form = form)

if __name__ == '__main__':
    app.run(debug=True)