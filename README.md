
# social_media
RESTful API for a social media platform. The API should allow users to create accounts, post updates, follow other users, like and comment on posts, and retrieve a user's feed. Additionally, implement user authentication and authorization to protect sensitive operations.


## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your local system:

- Python (3.10.4 or higher): [Download Python](https://www.python.org/downloads/)
- pip (Python package manager): [Install pip](https://pip.pypa.io/en/stable/installation/)
- Git: [Install Git](https://git-scm.com/downloads/)

## Getting Started

Follow these steps to set up the project on your local system.

### Clone the Repository

1. Open your command-line terminal.

2. Navigate to the directory where you want to store the project.

3. Clone the project repository using the following command:

   ```bash
   git clone https://github.com/karanwadhawan1/social_media.git

4. Create the Environment File
Create a .env file in the project root directory and add the necessary environment variables. You can copy the example.env file and modify it as needed.

   ```bash
   python -m venv venv
   source venv/bin/activate

6. Navigate to the Project Directory

  Change your directory to the project folder:

   ```bash
   cd social_media

7. Switch to the main Branch
Make sure you are on the main branch:

    ```bash
    git checkout master

8. Install Dependencies
Install the project dependencies using pip:

    ```bash
    pip install -r requirements.txt

9. Apply Migrations
Run the following commands to apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

10. Create a Superuser
Create a superuser account to access the admin panel:

    ```bash
    python manage.py createsuperuser

9. Run the Development Server
Start the development server:

    ```bash
    python manage.py runserver

10. import the `Social  Media.postman_collection.json` in Postman . 






