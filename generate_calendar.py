from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz
import os

# Define timezone
tz = pytz.timezone('America/New_York')

# Function to create a unique identifier for each event
def generate_uid(event_details):
    base_string = f"{event_details['summary']}-{event_details['start']}-{event_details['end']}"
    return str(abs(hash(base_string)))

# Set the path to the "calendar_application" directory
base_directory = os.path.dirname(os.path.abspath(__file__))

# Get the current version number
version = 1
while os.path.exists(f'{base_directory}/weekly_schedule_v{version}.ics'):
    version += 1

# Create the calendar
cal = Calendar()
cal.add('version', '2.0')
cal.add('calscale', 'GREGORIAN')

# Event details list
# events = [
#     {
#         'summary': 'Job Hunt Automation - Job Scraper Setup',
#         'start': datetime(2024, 11, 11, 7, 0, tzinfo=tz),
#         'end': datetime(2024, 11, 11, 8, 0, tzinfo=tz),
#         'description': 'Job Hunt Automation for LinkedIn job scraper setup.'
#     },
#     {
#         'summary': 'League of Legends Training - Esports Review, Solo Practice, Ranked Play',
#         'start': datetime(2024, 11, 11, 17, 0, tzinfo=tz),
#         'end': datetime(2024, 11, 11, 18, 30, tzinfo=tz),
#         'description': 'Training session including esports review, solo practice, and a ranked match.'
#     },
#     # Add more events here, following the same format for each day of the week.
# ]

events = [
    # Week 1: Foundation and Setup
    {
        'summary': 'CMS Application - Initial Project Setup',
        'start': datetime(2024, 11, 18, 9, 0),
        'end': datetime(2024, 11, 18, 12, 0),
        'description': 'Project structure setup, virtual environment configuration, git initialization, dependency installation'
    },
    {
        'summary': 'CMS Application - Backend Foundation',
        'start': datetime(2024, 11, 18, 13, 0),
        'end': datetime(2024, 11, 18, 15, 0),
        'description': 'FastAPI setup, basic routing configuration, test framework initialization'
    },
    {
        'summary': 'CMS Application - File Processing Module',
        'start': datetime(2024, 11, 19, 9, 0),
        'end': datetime(2024, 11, 19, 12, 0),
        'description': 'CSV validation implementation, file upload utilities, error handling'
    },
    {
        'summary': 'CMS Application - Testing Framework',
        'start': datetime(2024, 11, 19, 13, 0),
        'end': datetime(2024, 11, 19, 15, 0),
        'description': 'Test fixtures creation, validation tests, error handling tests'
    },
    {
        'summary': 'CMS Application - ML Service Foundation',
        'start': datetime(2024, 11, 20, 9, 0),
        'end': datetime(2024, 11, 20, 12, 0),
        'description': 'ML service architecture, feature preparation utilities, data transformer implementation'
    },
    {
        'summary': 'CMS Application - ML Model Core',
        'start': datetime(2024, 11, 20, 13, 0),
        'end': datetime(2024, 11, 20, 15, 0),
        'description': 'Scoring mechanism, model loading utilities, feature scaling setup'
    },
    {
        'summary': 'CMS Application - Database Architecture',
        'start': datetime(2024, 11, 21, 9, 0),
        'end': datetime(2024, 11, 21, 12, 0),
        'description': 'Database setup, repository pattern implementation, schema design'
    },
    {
        'summary': 'CMS Application - Database Implementation',
        'start': datetime(2024, 11, 21, 13, 0),
        'end': datetime(2024, 11, 21, 15, 0),
        'description': 'CRUD operations, data models, repository tests'
    },
    {
        'summary': 'CMS Application - Integration Phase 1',
        'start': datetime(2024, 11, 22, 9, 0),
        'end': datetime(2024, 11, 22, 12, 0),
        'description': 'Backend service integration, testing connectivity, error handling'
    },
    {
        'summary': 'CMS Application - Week 1 Review',
        'start': datetime(2024, 11, 22, 13, 0),
        'end': datetime(2024, 11, 22, 15, 0),
        'description': 'Code review, documentation update, next week planning'
    },

    # Week 2: Frontend Development
    {
        'summary': 'CMS Application - Frontend Setup',
        'start': datetime(2024, 11, 25, 9, 0),
        'end': datetime(2024, 11, 25, 12, 0),
        'description': 'Next.js setup, Material-UI integration, component structure'
    },
    {
        'summary': 'CMS Application - Upload Component',
        'start': datetime(2024, 11, 25, 13, 0),
        'end': datetime(2024, 11, 25, 15, 0),
        'description': 'File upload component, progress indicator, error handling'
    },
    {
        'summary': 'CMS Application - DataGrid Component',
        'start': datetime(2024, 11, 26, 9, 0),
        'end': datetime(2024, 11, 26, 12, 0),
        'description': 'Data display grid, sorting functionality, filtering implementation'
    },
    {
        'summary': 'CMS Application - Frontend Testing',
        'start': datetime(2024, 11, 26, 13, 0),
        'end': datetime(2024, 11, 26, 15, 0),
        'description': 'Component tests, integration tests, UI testing'
    },
    {
        'summary': 'CMS Application - API Integration',
        'start': datetime(2024, 11, 27, 9, 0),
        'end': datetime(2024, 11, 27, 12, 0),
        'description': 'API service implementation, error handling, loading states'
    },
    {
        'summary': 'CMS Application - Frontend Polish',
        'start': datetime(2024, 11, 27, 13, 0),
        'end': datetime(2024, 11, 27, 15, 0),
        'description': 'UI refinements, responsive design, accessibility'
    },
    {
        'summary': 'CMS Application - User Feedback',
        'start': datetime(2024, 11, 28, 9, 0),
        'end': datetime(2024, 11, 28, 12, 0),
        'description': 'Error messages, loading indicators, success notifications'
    },
    {
        'summary': 'CMS Application - Frontend Integration',
        'start': datetime(2024, 11, 28, 13, 0),
        'end': datetime(2024, 11, 28, 15, 0),
        'description': 'Full frontend-backend integration testing'
    },
    {
        'summary': 'CMS Application - Week 2 Review',
        'start': datetime(2024, 11, 29, 9, 0),
        'end': datetime(2024, 11, 29, 12, 0),
        'description': 'Frontend review, documentation, next week planning'
    },

    # Week 3: ML Integration and Enhancement
    {
        'summary': 'CMS Application - ML Pipeline Integration',
        'start': datetime(2024, 12, 2, 9, 0),
        'end': datetime(2024, 12, 2, 12, 0),
        'description': 'ML service integration, data processing pipeline'
    },
    {
        'summary': 'CMS Application - Feature Engineering',
        'start': datetime(2024, 12, 2, 13, 0),
        'end': datetime(2024, 12, 2, 15, 0),
        'description': 'Feature extraction, transformation implementation'
    },
    
    # Week 3 (continued): ML Integration and Enhancement
    {
        'summary': 'CMS Application - Model Optimization',
        'start': datetime(2024, 12, 3, 9, 0),
        'end': datetime(2024, 12, 3, 12, 0),
        'description': 'Performance optimization, model tuning, validation metrics'
    },
    {
        'summary': 'CMS Application - Batch Processing',
        'start': datetime(2024, 12, 3, 13, 0),
        'end': datetime(2024, 12, 3, 15, 0),
        'description': 'Implement batch processing for large datasets, progress tracking'
    },
    {
        'summary': 'CMS Application - ML Testing',
        'start': datetime(2024, 12, 4, 9, 0),
        'end': datetime(2024, 12, 4, 12, 0),
        'description': 'ML pipeline testing, accuracy validation, error analysis'
    },
    {
        'summary': 'CMS Application - Error Handling',
        'start': datetime(2024, 12, 4, 13, 0),
        'end': datetime(2024, 12, 4, 15, 0),
        'description': 'ML service error handling, fallback strategies'
    },
    {
        'summary': 'CMS Application - Performance Testing',
        'start': datetime(2024, 12, 5, 9, 0),
        'end': datetime(2024, 12, 5, 12, 0),
        'description': 'Load testing, performance optimization, bottleneck identification'
    },
    {
        'summary': 'CMS Application - Week 3 Review',
        'start': datetime(2024, 12, 6, 9, 0),
        'end': datetime(2024, 12, 6, 12, 0),
        'description': 'ML integration review, documentation update, next week planning'
    },

    # Week 4: Testing and Quality Assurance
    {
        'summary': 'CMS Application - Integration Testing',
        'start': datetime(2024, 12, 9, 9, 0),
        'end': datetime(2024, 12, 9, 12, 0),
        'description': 'End-to-end testing, integration test suite development'
    },
    {
        'summary': 'CMS Application - Unit Testing',
        'start': datetime(2024, 12, 9, 13, 0),
        'end': datetime(2024, 12, 9, 15, 0),
        'description': 'Comprehensive unit test coverage, edge case testing'
    },
    {
        'summary': 'CMS Application - Security Implementation',
        'start': datetime(2024, 12, 10, 9, 0),
        'end': datetime(2024, 12, 10, 12, 0),
        'description': 'Security testing, vulnerability assessment, authentication implementation'
    },
    {
        'summary': 'CMS Application - Performance Optimization',
        'start': datetime(2024, 12, 10, 13, 0),
        'end': datetime(2024, 12, 10, 15, 0),
        'description': 'Performance tuning, caching implementation, query optimization'
    },
    {
        'summary': 'CMS Application - User Acceptance Testing',
        'start': datetime(2024, 12, 11, 9, 0),
        'end': datetime(2024, 12, 11, 12, 0),
        'description': 'UAT preparation, test case documentation, feedback collection'
    },
    {
        'summary': 'CMS Application - Bug Fixing',
        'start': datetime(2024, 12, 11, 13, 0),
        'end': datetime(2024, 12, 11, 15, 0),
        'description': 'Address UAT feedback, bug fixes, regression testing'
    },
    {
        'summary': 'CMS Application - Documentation',
        'start': datetime(2024, 12, 12, 9, 0),
        'end': datetime(2024, 12, 12, 12, 0),
        'description': 'API documentation, user guides, deployment documentation'
    },
    {
        'summary': 'CMS Application - Week 4 Review',
        'start': datetime(2024, 12, 13, 9, 0),
        'end': datetime(2024, 12, 13, 12, 0),
        'description': 'Quality assurance review, documentation finalization, deployment planning'
    },

    # Week 5: Deployment and Monitoring
    {
        'summary': 'CMS Application - Deployment Setup',
        'start': datetime(2024, 12, 16, 9, 0),
        'end': datetime(2024, 12, 16, 12, 0),
        'description': 'Production environment setup, deployment pipeline configuration'
    },
    {
        'summary': 'CMS Application - Monitoring Setup',
        'start': datetime(2024, 12, 16, 13, 0),
        'end': datetime(2024, 12, 16, 15, 0),
        'description': 'Monitoring tools integration, alert setup, logging configuration'
    },
    {
        'summary': 'CMS Application - CI/CD Pipeline',
        'start': datetime(2024, 12, 17, 9, 0),
        'end': datetime(2024, 12, 17, 12, 0),
        'description': 'CI/CD pipeline setup, automated testing integration'
    },
    {
        'summary': 'CMS Application - Staging Deployment',
        'start': datetime(2024, 12, 17, 13, 0),
        'end': datetime(2024, 12, 17, 15, 0),
        'description': 'Staging environment deployment, testing verification'
    },
    {
        'summary': 'CMS Application - Production Deployment',
        'start': datetime(2024, 12, 18, 9, 0),
        'end': datetime(2024, 12, 18, 12, 0),
        'description': 'Production deployment, smoke testing, monitoring verification'
    },
    {
        'summary': 'CMS Application - Post-Deployment Testing',
        'start': datetime(2024, 12, 18, 13, 0),
        'end': datetime(2024, 12, 18, 15, 0),
        'description': 'Production testing, performance verification, monitoring check'
    },
    {
        'summary': 'CMS Application - Final Review',
        'start': datetime(2024, 12, 19, 9, 0),
        'end': datetime(2024, 12, 19, 12, 0),
        'description': 'Final system review, documentation review, handover preparation'
    },
    {
        'summary': 'CMS Application - Project Handover',
        'start': datetime(2024, 12, 19, 13, 0),
        'end': datetime(2024, 12, 19, 15, 0),
        'description': 'Knowledge transfer, documentation handover, support setup'
    }
]

# Create events and add to calendar
for event_details in events:
    event = Event()
    event.add('summary', event_details['summary'])
    event.add('dtstart', event_details['start'])
    event.add('dtend', event_details['end'])
    event.add('description', event_details['description'])
    event.add('uid', generate_uid(event_details))  # Add unique identifier to event
    cal.add_component(event)

# Save the calendar to a file in the "calendar_application" directory
filename = f'weekly_schedule_v{version}.ics'
calendar_path = os.path.join(base_directory, filename)
with open(calendar_path, 'wb') as f:
    f.write(cal.to_ical())

# Update changelog.txt in the "calendar_application" directory
changelog_path = os.path.join(base_directory, 'changelog.txt')
with open(changelog_path, 'a') as changelog:
    changelog.write(f"Version {version} generated on {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}\n")
    for event in events:
        changelog.write(f"- {event['summary']} from {event['start']} to {event['end']}\n")
    changelog.write("\n")