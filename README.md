# MongoDB Atlas Form Submission

## Objective

Create a frontend form that inserts user data into MongoDB Atlas using Flask.

## Features

* Frontend form for user input
* Flask backend
* MongoDB Atlas integration
* Redirects to a success page after successful submission
* Displays errors on the same page if submission fails

## Project Structure

```text
mongodb-atlas-form/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── form.html
    └── success.html
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd mongodb-atlas-form
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

<img width="959" height="599" alt="Screenshot 2026-06-13 152138" src="https://github.com/user-attachments/assets/962ca137-bc65-492c-99b0-f5e589855e65" />


## MongoDB Atlas Configuration

Before running the project, replace the following line in `app.py`:

```python
MONGO_URI = "YOUR_MONGODB_CONNECTION_STRING"
```

with your own MongoDB Atlas connection string:

```python
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
```

## Running the Application

```bash
python3 app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter Name and Email.
2. Click Submit.
3. Data is stored in MongoDB Atlas.
4. User is redirected to the success page displaying:

<img width="959" height="570" alt="Screenshot 2026-06-13 154352" src="https://github.com/user-attachments/assets/4162e837-878a-49f8-93a9-bc5328c5edd0" />


```text
Data submitted successfully
```
<img width="959" height="570" alt="Screenshot 2026-06-13 154358" src="https://github.com/user-attachments/assets/05902c48-e1d0-4972-93e2-712c2328b046" />


<img width="959" height="567" alt="Screenshot 2026-06-13 160414" src="https://github.com/user-attachments/assets/f8cb559c-bd89-4043-b4e7-5e60b5b41ff7" />



## Technologies Used

* Python
* Flask
* MongoDB Atlas
* PyMongo
* HTML

## Author

Pawan Kalyan

