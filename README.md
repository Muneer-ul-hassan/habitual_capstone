
# Habitual: Build Lasting Habits — CS50W Capstone Project

Habitual is a privacy-first web application designed to help users create, track, and maintain lasting habits through a dynamic and interactive platform. Unlike simple habit trackers, Habitual integrates mood tracking, streak-based gamification, and data-driven insights to motivate users toward positive lifestyle changes. It uses Django as the backend framework to store user data, habits, mood logs, and reminders in models, while JavaScript on the frontend powers dynamic charts, interactive UI elements, notifications, and responsive design.

## Features

- **Habit Tracking with Emojis**: Create and track habits with customizable emojis for visual appeal
- **Mood Tracking and Correlation**: Log daily mood and visualize correlations with habit completion
- **Streak-based Gamification**: Track consecutive days of habit completion with visual streak counters
- **Badge System**: Earn badges for achieving milestones and maintaining streaks
- **Interactive Dashboard**: Beautiful, responsive UI with gradient designs and smooth animations
- **Data Visualization**: Interactive charts showing habit trends and mood correlations using Chart.js
- **Time-Zone-Aware Reminders**: Set personalized reminders that respect your local timezone
- **Data Export**: Export habit and mood data as CSV files for personal analysis
- **Progress Tracking**: Visual progress bars and completion rates
- **Responsive Design**: Optimized for desktop and mobile devices

## Distinctiveness and Complexity

Habitual is distinct from the other projects in the CS50W curriculum. It is not a social network, an e-commerce platform, or a simple content-delivery site. Instead, it is a personal productivity tool that focuses on user engagement and data visualization. The complexity of the project lies in the following features:

*   **Mood Tracking and Correlation:** Users can log their daily mood, and the application will visualize the correlation between their mood and habit completion. This provides users with valuable insights into their well-being.
*   **Gamification:** The application includes a streak calculation system and a badge system to gamify the habit-tracking process and keep users motivated.
*   **Time-Zone-Aware Reminders:** Users can set reminders for their habits, and the application will send them notifications at the correct time in their local timezone.
*   **Data Export:** Users can export their habit and mood data as a CSV file for their own personal use.
*   **Interactive Charts:** The application uses Chart.js to create interactive charts that visualize habit completion trends and mood correlations.
*   **Dynamic UI:** The application uses AJAX to update the UI without requiring a page reload, creating a smooth and responsive user experience.
*   **Enhanced UX:** Modern design with gradient backgrounds, smooth animations, and intuitive user interface elements.

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
        *   `base.html`: Base template with navigation and common elements
        *   `index.html`: Main dashboard with habit overview and statistics
        *   `add_habit.html`: Form for creating new habits with emoji selection
        *   `log_mood.html`: Interactive mood logging interface
        *   `login.html` & `register.html`: Authentication pages
    *   `static/`: Contains the static files (CSS, JavaScript) for the application.
        *   `style.css`: Comprehensive styling with gradients, animations, and responsive design
        *   `js/charts.js`: Chart.js implementation for data visualization
        *   `js/main.js`: Interactive JavaScript functionality
*   `users/`: A dedicated app for managing user-related functionality.
    *   `models.py`: Defines the `CustomUser` model with timezone support.
    *   `forms.py`: Defines the form for updating the user profile.
    *   `views.py`: Contains the view for the user profile page.
    *   `urls.py`: Defines the URL patterns for the `users` app.
    *   `templates/users/profile.html`: Enhanced user profile page with statistics
*   `manage.py`: A command-line utility for interacting with the Django project.
*   `requirements.txt`: A list of the project's dependencies.

## How to Run the Application

1.  Clone the repository:
    ```
    git clone <repository-url>
    cd habitual_capstone
    ```

2.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

3.  Run the database migrations:
    ```
    python manage.py migrate
    ```

4.  Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```

5.  Start the development server:
    ```
    python manage.py runserver 0.0.0.0:5000
    ```

6.  Access the application at the provided URL in your web browser.

## Usage

1. **Register/Login**: Create an account or login to access your personal dashboard
2. **Add Habits**: Create new habits with custom names, descriptions, and emojis
3. **Track Progress**: Mark habits as complete and watch your streaks grow
4. **Log Mood**: Record your daily mood to see correlations with habit completion
5. **View Analytics**: Check your progress charts and statistics on the dashboard
6. **Earn Badges**: Complete milestones to unlock achievement badges
7. **Export Data**: Download your habit and mood data for external analysis

## Technologies Used

*   **Backend**: Django (Python web framework)
*   **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
*   **Database**: SQLite (development), PostgreSQL compatible
*   **Charts**: Chart.js for data visualization
*   **Styling**: Custom CSS with gradients and animations
*   **Icons**: Font Awesome for UI icons
*   **Timezone**: pytz for timezone-aware functionality

## Additional Packages Used

*   **Django:** The backend framework for the application.
*   **pytz:** A library for working with timezones.
*   **Bootstrap:** A CSS framework for creating a responsive design.
*   **Chart.js:** A JavaScript library for creating interactive charts.

## License

This project is created for educational purposes as part of the CS50W Web Programming course.
