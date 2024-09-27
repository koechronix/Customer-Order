from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

# Create an instance of the Flask application
app = create_app()

# Create a Manager to handle commands
manager = Manager(app)

# Add Flask-Migrate command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
