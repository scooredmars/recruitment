# Django Text Processor & PESEL Validator

This project is a Django application that offers two main features:

- **Text Processor**: Upload a text file, scramble the letters in the middle of each word (keeping the first and last letters unchanged), and view the modified text.
- **PESEL Validator**: Enter a PESEL number, validate it using the official algorithm, and display details such as the date of birth and gender.

## Getting Started

### Prerequisites

- **Python 3.13 or later**
- **Django 5.x**
- A virtual environment (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/scooredmars/recruitment.git
   cd recruitment
2. **Create and activate a virtual environment:**

   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install Django:**

   ```bash
    pip install django
4. **Run migrations:**

   ```bash
    python manage.py migrate
5. **Start the development server:**

   ```bash
    python manage.py runserver

6. **Access the application:**

- Text Processor: <http://localhost:8000/text/>
- PESEL Validator: <http://localhost:8000/pesel/>

## Feature Details

### Text Processor

- **Upload a Text File:** Use the form to upload a text file.
- **Scramble Text:** The app scrambles the middle letters of each word (first and last letters remain unchanged) and displays the processed text.
- **Templates:**
  - **upload.html** for the file upload form.
  - **result.html** to display the scrambled text.

### PESEL Validator

- **Enter a PESEL Number:** The validator provides a form for entering an 11-digit PESEL number.
- **Validation:** The application checks if the number is valid by verifying its control digit and decodes the date of birth and gender.
- **Template:**
  - pesel.html displays the input form and validation result.

### .gitignore

The repository includes a **.gitignore** file to exclude files and directories such as:

- Python bytecode files
- The SQLite database file
- IDE-specific files
