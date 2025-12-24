from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home_page():
    print("hello home")
    return render_template("home.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)