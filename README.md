# ProjectDjango-Domo

ProjectDjango-Domo is a Django-based web application designed to manage and automate tasks in a home automation system. The project integrates different components like sensor management, device control, and monitoring features, offering a user-friendly interface for controlling smart devices in a connected environment.

## Features
- **Device Control**: Manage various smart home devices such as lights, thermostats, and security cameras.
- **Sensor Monitoring**: Real-time data display from sensors like temperature, humidity, and motion detectors.
- **User Authentication**: Secure login and user management system.
- **Mobile Responsive Design**: Optimized for both desktop and mobile devices.

## Requirements
The project dependencies are listed in the `requirements.txt` file, which can be installed with:
```bash
pip install -r requirements.txt
```
### Navigate to the project directory and set up a virtual environment:
```bash
cd ProjectDjango-Domo
python3 -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate  # For Windows
```

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run database migrations:
```bash
python manage.py migrate
```
### Start the development server:
```bash
python manage.py runserver
```
## Project Structure
- `domotica/`: Core Django app handling home automation functionalities.
- `.gitignore`: Ensures sensitive files and unnecessary directories are not tracked.
- `requirements.txt`: Lists the Python packages required to run the project.

## Contributing
Feel free to submit pull requests or open issues to suggest improvements or report bugs.



