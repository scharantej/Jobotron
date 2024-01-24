## Flask Application Design

### Objective:
Create a Flask web application that monitors the number of jobs available on LinkedIn, stores the data, and presents it as a graph. It should allow users to filter jobs by region and substring.

### Application Structure:

#### HTML Files:

- `index.html`:
  - This is the home page of the application.
  - Contains a form to specify filtering options (region and substring) and a submit button.
  - Displays a graph of the number of jobs over time, initially showing all jobs.

- `results.html`:
  - Displays the graph of the number of jobs over time, filtered based on the user's input.
  - Includes a table with the details of the jobs that match the filtering criteria.

#### Routes:

- `/`:
  - Serves the `index.html` page.

- `/results`:
  - Handles the form submission from the home page.
  - Queries LinkedIn for jobs matching the specified criteria.
  - Stores the results in a database.
  - Generates a graph of the number of jobs over time.
  - Renders the `results.html` page with the graph and job details.

### Technical Implementation Considerations:

- Utilize Flask's `request` object to access the form data submitted by the user.
- Use a Python library like `LinkedInJobs` to query LinkedIn for job postings.
- Store the results in a database using an ORM like SQLAlchemy.
- Use a Python library like `Plotly` to create the graph of the number of jobs over time.
- Host the application on a web server like Apache or Nginx.

### Testing:

- Create unit tests to verify the functionality of the Flask routes and the data storage and retrieval operations.
- Perform integration tests to ensure that the application works as expected when all components are integrated.

### Deployment:

- Package the application as a standalone executable using tools like PyInstaller or cx_Freeze.
- Deploy the application to a web hosting platform or a cloud environment.

### Additional Features (Optional):

- Allow users to create an account and save their filtering preferences.
- Send email notifications to users when new jobs matching their criteria are posted.
- Provide an API for external applications to access the job data.