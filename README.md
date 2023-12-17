# SportPerformanceTracker

A web app designed to explore the impact of menstrual cycles on athletic performance through daily surveys, enabling female athletes to log their physical and emotional state while providing users with a comprehensive data dashboard for in-depth analysis and performance correlation.
This is a small scale "proof of concept" -type version. Making the addition of new survey dimensions straightforward is key for enhanced future research and insights.

## For the final review 16.12.2023

[Try it out](https://sportperformancetracker.fly.dev)

In the last two weeks, the main goal was to enhance the user interface, making it functional yet straightforward, and to address various small tasks. This included refining error handling and cleaning up the code for better readability.

Users can create an account and participate in the daily poll to input their data. The app provides personalized tips based on user data. For now, these tips are mere placeholders and NOT sourced from credible references.

Looking forward, I'm considering expanding the scope of this project. By adding more depth to the daily poll, one could potentially collect valuable scientific data on the relationship between the menstrual cycle and athletic performance. This could pave the way for more nuanced advice and insights, backed by thorough data analysis.

### Known Issues

- When creating a new account, if the passwords don't match or the username is already in use, the app displays an error message. However, the form needs to be navigated back to and all fields are emptied, which is BAD UI design.
- The UI looks disgusting.

## For the peer reviewer 3.12.2023

Over the past two weeks, the primary focus has been on establishing the core functionalities of the app. In response to feedback from the previous peer review, I have made several improvements and have successfully integrated Chart.js. This has enhanced the app's capability to display user data, including an overlay of their menstrual cycle.

Currently, users can create an account and participate in a daily poll. The responses from this poll are then visualized in the chart(s).

The next and last phase of development involves implementing personalized tips based on user data. For example, if a user experiences a decline in sleep quality, the app will offer relevant advice for improving sleep. One long-term objective is to refine these tips, ensuring they are grounded in reliable data and credible sources. However, please note that the current tips are mom-level wisdom and serve as basic placeholders.

Additionally, I have not yet focused on the aesthetic aspects of the app. Enhancing the app's visual appeal will be a primary goal before the final review.

## For the peer reviewer 18.11.2023

I've been focusing primarily on setting up the initial configuration. As it stands, you can perform tasks like create a user, log in and out, input data, and view your personal data in a table format. However, this version is far from final.

In the upcoming iterations, the aim is to implement a dashboard and replace tables with graphical representations for better data visualization. The current survey questions are basic; the plan is to explore more sophisticated responses, possibly transitioning from the simple 1-5 radio buttons to incorporate text fields and checkboxes. As the latter brings complexity, there's a consideration to maintain simplicity by sticking mostly with radio buttons for now.

For password hashing, the project utilizes bcrypt instead of Werkzeug.security. The reason for this choice was due to compatibility issues encountered. I need to review the safety of the user-data query ASAP. As of now, it retrieves the user_id from the session, which might not be safe(?).

# Setup

Before getting started, make sure you have PostgreSQL installed and running on your system.

1. Run the following command to set up the database schema:

```bash
psql -U <your_username> -d <your_database_name> -f schema.sql
```

2. Create a `.env` file in the project directory and add the following environment variables:

```plaintext
DATABASE_URL=<your_database_url>
SECRET_KEY=<your_secret_key>
DEV = True
```

3. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Insert the schema into the database:

```bash
psql < schema.sql
```

5. Finally, run the app:

```bash
flask run
```
