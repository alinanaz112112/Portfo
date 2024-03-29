from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello(username=None, post_id=None):
#     return render_template('index1.html', name=username, id=post_id)

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on Alina Blog'

# @app.route('/contact')
# def contact():
#     return render_template('about.html')

# @app.route('/contact/email/2020')
# def email():
#     return 'alinanaz112@gmail.com'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Failed to store to database'
    else:
        return 'Something went worng'