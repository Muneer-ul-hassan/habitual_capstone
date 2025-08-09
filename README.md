# Habitual: Build Lasting Habits — CS50W Capstone Project

Habitual is a privacy-first web application designed to help users create, track, and maintain lasting habits through a dynamic and interactive platform. Unlike simple habit trackers, Habitual integrates mood tracking, streak-based gamification, and data-driven insights to motivate users toward positive lifestyle changes. It uses Django as the backend framework to store user data, habits, mood logs, and reminders in models, while JavaScript on the frontend powers dynamic charts, interactive UI elements, notifications, and responsive design.

## Distinctiveness and Complexity

Habitual is distinct from the other projects in the CS50W curriculum. It is not a social network, an e-commerce platform, or a simple content-delivery site. Instead, it is a personal productivity tool that focuses on user engagement and data visualization. The complexity of the project lies in the following features:

*   **Mood Tracking and Correlation:** Users can log their daily mood, and the application will visualize the correlation between their mood and habit completion. This provides users with valuable insights into their well-being.
*   **Gamification:** The application includes a streak calculation system and a badge system to gamify the habit-tracking process and keep users motivated.
*   **Time-Zone-Aware Reminders:** Users can set reminders for their habits, and the application will send them notifications at the correct time in their local timezone.
*   **Data Export:** Users can export their habit and mood data as a CSV file for their own personal use.
*   **Interactive Charts:** The application uses Chart.js to create interactive charts that visualize habit completion trends and mood correlations.
*   **Dynamic UI:** The application uses AJAX to update the UI without requiring a page reload, creating a smooth and responsive user experience.

## File Structure

*   `habitual/`: The main Django project directory.
    *   `settings.py`: The project's settings file.
    *   `urls.py`: The project's main URL configuration.
*   `habits/`: The core application for managing habits, mood logs, and reminders.
    *   `models.py`: Defines the database models for `Habit`, `HabitLog`, `MoodLog`, and `Reminder`.
    *   `views.py`: Contains the views for handling user requests and rendering templates.
    *   `urls.py`: Defines the URL patterns for the `habits` app.
    *   `forms.py`: Defines the forms for user registration, habit creation, and mood logging.
    *   `badges.py`: Contains the logic for awarding badges to users.
    *   `management/commands/send_reminders.py`: A management command for sending habit reminders.
    *   `templates/`: Contains the HTML templates for the application.
    *   `static/`: Contains the static files (CSS, JavaScript) for the application.
*   `users/`: A dedicated app for managing user-related functionality.
    *   `models.py`: Defines the `CustomUser` model.
    *   `forms.py`: Defines the form for updating the user profile.
    *   `views.py`: Contains the view for the user profile page.
    *   `urls.py`: Defines the URL patterns for the `users` app.
*   `manage.py`: A command-line utility for interacting with the Django project.
*   `requirements.txt`: A list of the project's dependencies.

## How to Run the Application

1.  Clone the repository:
    ```
    git clone <repository-url>
    cd habitual_capstone
    ```

2.  Create a virtual environment:
    ```
    python -m venv venv
    ```

3.  Activate the virtual environment:
    *   **On Windows:**
        ```
        venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```
        source venv/bin/activate
        ```

4.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

5.  Run the database migrations:
    ```
    python manage.py migrate
    ```

6.  Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```

7.  Start the development server:
    ```
    python manage.py runserver
    ```

8.  Access the application at `http://localhost:8000` in your web browser.

## Additional Packages Used

*   **Django:** The backend framework for the application.
*   **pytz:** A library for working with timezones.
*   **Bootstrap:** A CSS framework for creating a responsive design.
*   **Chart.js:** A JavaScript library for creating interactive charts.