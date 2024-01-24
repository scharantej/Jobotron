
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objects as go
from linkedin_jobs import LinkedInJobs

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db = SQLAlchemy(app)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.Text)

# Create the database tables
db.create_all()

# Initialize the LinkedInJobs client
linkedin_jobs = LinkedInJobs()

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Results page route
@app.route('/results', methods=['POST'])
def results():
    # Get the form data
    region = request.form['region']
    substring = request.form['substring']

    # Query LinkedIn for jobs
    jobs = linkedin_jobs.search(keywords=substring, location=region)

    # Store the results in the database
    for job in jobs:
        new_job = Job(title=job['title'], location=job['location'], description=job['description'])
        db.session.add(new_job)

    db.session.commit()

    # Create the graph of the number of jobs over time
    dates = [job.timestamp for job in Job.query.all()]
    counts = [len(Job.query.filter(Job.timestamp == date).all()) for date in dates]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=counts, mode='lines'))
    fig.update_layout(title='Number of Jobs Over Time', xaxis_title='Date', yaxis_title='Number of Jobs')

    # Render the results page
    return render_template('results.html', graph=fig, jobs=jobs)

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
