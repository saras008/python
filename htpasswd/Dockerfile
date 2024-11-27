# Specify the Python version
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the port that the app will run on
EXPOSE 5000

# Set the Flask environment variables (Optional if using gunicorn)
ENV FLASK_APP=htpasswd.py     
ENV FLASK_ENV=development

# Run the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "htpasswd:app"]

