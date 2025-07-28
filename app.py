from flask import Flask,render_template,request,redirect,session
from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db=client['Rock']
collection=db['std']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def loginPage():
   return render_template('login.html') 

@app.route('/dash')
def main():
   return render_template('dash.html') 

@app.route('/',methods=['POST'])
def data():
    name=request.form['name']
    rollno=request.form['rollno']
    phone=request.form['phone']
    gender=request.form['gender']
    dob=request.form['dob']
    email=request.form['email']
    password=request.form['password']
    course=request.form['course']
    about=request.form['about']
    print(name,rollno,phone,gender,dob,email,password,course,about)
    
    
    for i in collection.find():
        if i['rollno']==rollno:
            return render_template('home.html', error='you have already registered')
    k={}
    k['name']=name
    k['rollno']=rollno
    k['phone']=phone
    k['gender']=gender
    k['dob']=dob
    k['email']=email
    k['password']=password.replace(" ", "")
    k['course']=course
    k['about']=about
    collection.insert_one(k)
    print("Inserted Sucessfully")
    return render_template('home.html',result='you have registered successfully')
    # return "hello"
    
@app.route('/login', methods=['POST'])
def logindata():
    rollno=request.form['rollno']
    password=request.form['password']
    print(rollno,password)
    for i in collection.find():
        if (i['rollno']==rollno) and (i['password']==password):
            # session['username']=rollno
            return render_template('dash.html')
        
    return render_template('login.html',er='you have entered incorrect password')

@app.route('/logout')
def logout():
    # session['username']=None
    return redirect('/login')

@app.route('/homepage')
def homepage():
    return redirect('/dash')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feed():
    return render_template('feedback.html')
            

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)
