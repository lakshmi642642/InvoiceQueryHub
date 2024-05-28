# # InvoiceQueryHub # #

InvoiceQueryHub is a web application built with Flask, a Python web framework, that allows users to upload invoice images and extract information from them by asking questions.

# Features

* Upload Invoice Images: Users can upload images of invoices directly through the web interface.
* Ask Questions: Users can ask questions about the uploaded invoice images, such as the invoice number, total amount, or date of the invoice.
* Information Extraction: The application uses the Hugging Face LayoutLM model to extract relevant information from the uploaded invoice images based on the user's questions.
* User-Friendly Interface: The web interface is designed to be intuitive and easy to use, with clear instructions and feedback provided to the user.

# Technologies Used

* Flask: Flask is a lightweight WSGI web application framework in Python.
* Hugging Face Transformers: The Hugging Face Transformers library is used to interface with pre-trained transformer models for natural language processing tasks.
* Bootstrap: Bootstrap is a popular CSS framework for building responsive and visually appealing web interfaces.
* HTML/CSS/JavaScript: Standard web development technologies are used for creating the frontend interface and interactivity.
* Docker: Docker is used for containerization, making it easy to deploy the application in different environments.

# Steps To Run
* docker build -t flask-invoice-app .
* docker run -p 5000:5000 flask-invoice-app

# Sample Images Of the Application
![image](https://github.com/lakshmi642642/InvoiceQueryHub/assets/73113554/4b213ee9-275d-4850-a784-e1950f0d7d14)
![image](https://github.com/lakshmi642642/InvoiceQueryHub/assets/73113554/16d55827-4382-40a8-bfc7-139cd3f1e3d4)
![image](https://github.com/lakshmi642642/InvoiceQueryHub/assets/73113554/b61850e2-314d-4279-9358-a05af03f570d)


