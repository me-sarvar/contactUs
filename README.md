# ContactUs Django App

**ContactUs** is a Django application designed to provide administrators with control over user contact permissions. Admins can manage which users are allowed to reach out, and can block users based on their IP address or email address.

## Features

* **Admin Control:** Allows administrators to manage user contact permissions.
* **IP Address Blocking:** Admins can block users based on their IP addresses.
* **Email Blocking:** Admins can block users based on their email addresses.
* Easy integration into existing Django projects.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/me-sarvar/contactUs
    cd contactUs
    ```

2.  **Install the app:**

    ```bash
    pip install -r requirements.txt # if you have requirements.txt file, if not skip this step
    ```

3.  **Add `contactus` to your `INSTALLED_APPS` in `settings.py`:**

    ```python
    INSTALLED_APPS = [
        # ... other apps
        'contactus',
    ]
    ```

4.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (if you haven't already):**

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Access the Django admin panel:**

    Navigate to `/admin/` in your browser and log in with your superuser credentials.

2.  **Manage contact permissions:**

    In the admin panel, you'll find the "ContactUs" section. Here you can:

    * Add or remove users from the allowed contact list.
    * Add IP addresses to the blocked list.
    * Add email addresses to the blocked list.

## Models

* **AllowedUser:** Stores users who are allowed to contact.
* **BlockedIP:** Stores IP addresses that are blocked.
* **BlockedEmail:** Stores email addresses that are blocked.

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
