from flask import Flask, request, render_template
 
#initialize flask function
app = Flask(__name__)
 
#database for accounts
database = 'acc_info.csv'


#index page
@app.route('/')
def hello_world():
    return render_template("index.html")
 
#registration

@app.route("/register")
def register():
    return render_template("registration.html")

#login
@app.route("/")
def index():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():

#Open the file
    infile = open(database, 'r') 

    lines = infile.readlines() 

    for line in lines:
        sline = line.split(',')  
        print(sline) 

    infile.close()
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', 
                               info='User does not exist')
    else:
        if database[name1] != pwd:
            return render_template('login.html', 
                                   info='Wrong password')
        else:
            return render_template('home.html',
                                   name=name1)
 
 
#Run flask in debug mode
if __name__ == '__main__':
    app.run()