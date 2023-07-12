# Use an official Python runtime as the base image
FROM python:<3.10>

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project code to the container
COPY . /app/

# Expose the port on which your Django app runs
EXPOSE 8080

# Set the command to run your Django app
CMD python manage.py runserver 0.0.0.0:8080
