from flask import Flask, render_template

app = Flask(__name__)
Jobs=[
  {
    'id':1,
    'title':'Data Anlayst',
    'location':'bengaluru,india',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location':'delhi,india',
    'salary':'Rs.15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'remote',
    'salary':'Rs.12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'san francisco,usa',
    'salary':'$120,000'
  }
]
@app.route("/")

def hello():
    return render_template("home.html",jobs=Jobs,company_name="something that you want")
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
