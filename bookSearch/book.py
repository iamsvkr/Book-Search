from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import folium 
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="myMap")

app.config['MONGO_DBNAME'] = 'mydb_shivam'
app.config['MONGO_URI'] = 'mongodb://shivam:shivam1998@ds119853.mlab.com:19853/mydb_shivam'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        tasks = mongo.db.tasks
        login_user = tasks.find_one({'username' : request.form['username'], 'password' : request.form['password']})
        
        if login_user:
            return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        
        tasks = mongo.db.tasks
        existing_user = tasks.find_one({'name' : request.form['username']})
        
        if existing_user ==  None:
            location = geolocator.geocode(request.form['address'])
            tasks.insert({'username' : request.form['username'], 'email' : request.form['email'], 'book' : request.form['booksEnter'], 'password' : request.form['password'], 'address' : request.form['address'], 'latitude': location.latitude, 'longitude': location.longitude})
            session['username'] = request.form['username']
            return redirect(url_for('phone'))
        return 'username already exists'
    return render_template('register.html')


@app.route('/search', methods = ['POST', 'GET'])
def search():
    data = ""
    if request.method == 'POST':
        tasks = mongo.db.tasks
        book = tasks.find({'book' : request.form['book']})
        
        if book == None:
            return 'this book is not available'
        for bk in book:
            data = data +bk['username'] + bk['address'] + "," + " "
            my_map4 = folium.Map(location = [bk['latitude'], bk['longitude']],zoom_start = 15) 
            folium.Marker([bk['latitude'], bk['longitude']],popup = ' Geeksforgeeks.org ').add_to(my_map4) 
        my_map4.save(" my_map4.html ") 
        return data
    
    return render_template('search.html')

@app.route('/phone', methods = ['POST', 'GET'])
def phone():
    if request.method == 'POST':
        phone = mongo.db.phone
        phone.insert({'username' : request.form['username'],'mobile' : request.form['phone']})
        return redirect(url_for('index'))
    return render_template('phone.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)