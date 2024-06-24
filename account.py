from flask import Flask, request, render_template
 
#initialize flask function
app = Flask(__name__)
 
#database for accounts
database = 'C:\\Users\\DELL\\OneDrive\\Documents\\Soilstuff\\Plantville.github.io\\acc_info.csv'

#registration

#login
@app.route("/" )
def index():
    return render_template("login_page.html")

@app.route("/home_page", methods=['POST', 'GET'])
def home_page():
    return render_template("home_page.html")

@app.route('/register_page.html', methods=['POST', 'GET'])
def register_page():
    return render_template("register_page.html")

def login():

#Open the file
    infile = open(database, 'r') 

    lines = infile.readlines() 

    for line in lines:
        sline = line.split(',')  
        print(sline) 

    infile.close()
    username = request.form['username']
    password = request.form['password']
    if username not in database:
        return render_template('login_page.html', 
                               info='User does not exist')
    else:
        if database[username] != password:
            return render_template('login_page.html', 
                                   info='Wrong password')
        else:
            return render_template('home_page.html',
                                   name=username)
 
 
#Run flask in debug mode
if __name__ == '__main__':
    app.debug = True
    app.run()
