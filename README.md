# ChitChat: Real-time Chat Rooms with Django Channels

ChitChat is a Django-based web application that allows users to create and join real-time chat rooms. It leverages the power of Django Channels to provide instant communication using WebSockets.

## Features

* **Create Rooms:** Users can easily create new chat rooms.
* **Join Rooms:** Users can join existing public chat rooms.
* **Real-time Messaging:** Messages are sent and received instantly within the joined room using WebSockets.
* **User Presence:** (Optional, depending on implementation) See who else is online in the room.
* **Simple and Intuitive Interface:** A clean and user-friendly design for seamless chatting.

## Technologies Used

* **Django:** The high-level Python web framework.
* **Django Channels:** Extends Django to handle WebSockets and other asynchronous protocols.
* **Asgi:** The Asynchronous Server Gateway Interface.
* **HTML, CSS, JavaScript:** For the frontend interface.

## Prerequisites

* **Python:** (Specify minimum version, e.g., 3.8+)
* **pip:** Python package installer.
* **Database:** (e.g., PostgreSQL, SQLite - Django's default)
* **Redis or other Channel Layer Backend:** (Required for Django Channels)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AbrarZaved/ChitChat
    cd chitchat
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your database:**
    * Edit the `DATABASES` settings in `chitchat/settings.py`.

5.  **Configure the Channel Layer:**
    * Edit the `CHANNEL_LAYERS` settings in `chitchat/settings.py`. Ensure you have a Redis server running or configure another supported backend.

6.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```


9. **Access the application:** Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  Navigate to the application in your browser.
2.  You should see an interface to either create a new chat room or view existing ones.
3.  Click on a room name to join it.
4.  Start typing messages in the input field and press Enter to send. Messages will appear in real-time for all users in the same room.

## Further Development (Optional)

* **Private Rooms:** Implement the ability to create private rooms with invited users.
* **User Authentication:** Add user registration and login for personalized experiences.
* **Message History:** Store and display previous messages in a room.
* **User Avatars:** Display user profile pictures.
* **Notifications:** Implement notifications for new messages or room invitations.
* **Moderation Tools:** Add features for room administrators to manage messages and users.

## Contributing

Contributions are welcome! Please feel free to submit pull requests with bug fixes, new features, or improvements. Please follow standard coding practices and include clear descriptions of your changes.


## Author

**Abrar Javed**
