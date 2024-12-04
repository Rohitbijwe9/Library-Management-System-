📚 Library Management System
An advanced backend solution built with Django and Django REST Framework to streamline library operations. This system empowers librarians to efficiently manage users, books, and borrow requests while allowing library users to browse books, make borrow requests, and track their borrowing history.

🌟 Features
Librarian Functionality
User Management: Create, update, and delete library users.
Book Management: Add, update, and remove books in the library.
Request Management: Approve or deny book borrow requests.
Borrow History: View detailed borrowing history for all users.
Library User Functionality
Book Catalog: Browse and search for available books.
Borrow Requests: Submit requests to borrow books for specific periods.
Borrow History: View personal borrowing history in real-time.

🚀 Getting Started

Installation
Clone the Repository

bash
Copy code
git clone https://github.com/Rohitbijwe9/Library-Management-System-.git  
cd Library-Management-System-  
Set Up Virtual Environment

bash
Copy code
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  
Install Dependencies

bash
Copy code
pip install -r requirements.txt  
Apply Migrations

bash
Copy code
python manage.py makemigrations  
python manage.py migrate  
Create Superuser

bash
Copy code
python manage.py createsuperuser  
Run the Server

bash
Copy code
python manage.py runserver  
