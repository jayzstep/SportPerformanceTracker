# SportPerformanceTracker

A web app designed to explore the impact of menstrual cycles on athletic performance through daily surveys, enabling female athletes to log their physical and emotional state while providing users and the administrators with a comprehensive data dashboard for in-depth analysis and performance correlation.
This is a small scale "proof of concept" -type version. Making the addition of new survey dimensions straightforward is key for enhanced future research and insights.

# For the peer reviewer 18.11.2023

I've been focusing primarily on setting up the initial configuration. As it stands, you can perform tasks like create a user, log in and out, input data, and view your personal data in a table format. However, this version is far from final.

In the upcoming iterations, the aim is to implement a dashboard and replace tables with graphical representations for better data visualization. The current survey questions are basic; the plan is to explore more sophisticated responses, possibly transitioning from the simple 1-5 radio buttons to incorporate text fields and checkboxes. As the latter brings complexity, there's a consideration to maintain simplicity by sticking mostly with radio buttons for now.

For password hashing, the project utilizes bcrypt instead of Werkzeug.security. The reason for this choice was due to compatibility issues encountered. I need to review the safety of the user-data query ASAP. As of now, it retrieves the user_id from the session, which might not be safe(?).

# Setup (under construction)

## Database Setup

Ensure that you have PostgreSQL installed and running on your system.

Run the following command:

```bash
psql -U <your_username> -d <your_database_name> -f schema.sql
```

etc...
