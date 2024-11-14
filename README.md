# README.md

## Calendar Scheduler Application

This application is a Python script that creates a weekly schedule as an `.ics` calendar file. It allows users to define a set of events, which are then automatically generated and saved to an `.ics` file. Below is a description of each part of the code and what it does.

### Import Statements
- **`from icalendar import Calendar, Event`**: This library provides the tools to create and manipulate iCalendar files, which can be imported into calendar applications like Google Calendar or Outlook.
- **`from datetime import datetime, timedelta`**: The `datetime` module is used for working with dates and times, to define start and end times for events.
- **`import pytz`**: `pytz` is used to manage timezones effectively, ensuring that all times are accurately localized.
- **`import os`**: The `os` module is used to interact with the operating system, primarily to manage file paths.

### Timezone Setup
- **`tz = pytz.timezone('America/New_York')`**: Defines the timezone that the application will use (Eastern Time).

### UID Generation Function
- **`generate_uid(event_details)`**: This function creates a unique identifier for each event by hashing a combination of the event's summary, start time, and end time. This ensures that each event in the calendar has a unique UID.

### Set Base Directory
- **`base_directory = os.path.dirname(os.path.abspath(__file__))`**: Defines the directory where the calendar file will be saved. It uses the directory of the script itself.

### Version Management
- **`version = 1`**: Starts with version 1 and increments if an existing file with that version number is already present. This ensures that each calendar version has a unique filename.
- **`while os.path.exists(...)`**: Checks if the file already exists and increments the version number accordingly.

### Create the Calendar Object
- **`cal = Calendar()`**: Initializes the `Calendar` object.
- **`cal.add('version', '2.0')`**: Sets the version of the calendar.
- **`cal.add('calscale', 'GREGORIAN')`**: Specifies the calendar scale, which is Gregorian.

### Event Details
- **`events = [...]`**: Defines a list of events with details like `summary`, `start`, `end`, and `description`. This list serves as the input data for the calendar.
  - **Summary**: A short description of the event.
  - **Start and End**: The start and end time of the event, using `datetime` objects to specify the precise timing.
  - **Description**: Additional details about the event.

### Create Events and Add to Calendar
- **`for event_details in events:`**: Iterates over each event in the `events` list.
- **`event = Event()`**: Creates a new `Event` object.
- **`event.add(...)`**: Adds properties to the event, including `summary`, `dtstart` (start time), `dtend` (end time), `description`, and `uid` (unique identifier).
- **`cal.add_component(event)`**: Adds the created event to the calendar.

### Save the Calendar File
- **`filename = f'weekly_schedule_v{version}.ics'`**: Defines the filename based on the current version.
- **`calendar_path = os.path.join(...)`**: Constructs the full path for the calendar file.
- **`with open(calendar_path, 'wb') as f:`**: Opens the file for writing in binary mode.
- **`f.write(cal.to_ical())`**: Writes the calendar data to the `.ics` file.

### Update Changelog
- **`changelog_path = os.path.join(...)`**: Defines the path for a changelog file.
- **`with open(changelog_path, 'a') as changelog:`**: Opens the changelog file in append mode.
- **`changelog.write(...)`**: Logs the version of the calendar generated, along with the events included. This keeps track of what each version of the calendar contains.

## How to Run the Application
1. Make sure you have Python installed (preferably version 3.6+).
2. Install the required packages using `pip`:
   ```sh
   pip install icalendar pytz
   ```
3. Run the script:
   ```sh
   python calendar_scheduler.py
   ```
4. The script will create a calendar file (`weekly_schedule_vX.ics`) in the same directory as the script. It will also update `changelog.txt` to keep track of generated calendar versions.

## How to Modify Events
- To add or modify events, simply edit the `events` list in the script. Each event needs a `summary`, `start`, `end`, and `description`.

## Features
- **Unique Calendar Versions**: Each generated calendar is saved with a unique version number to prevent overwriting previous files.
- **Automatic Event UID Generation**: Ensures each event is uniquely identifiable.
- **Changelog Maintenance**: Logs details of each generated calendar version for tracking purposes.

## License
This application is open-source and can be freely modified and distributed.

