# Mini Student Profile App
# A small console program styled after a Flask web app, using OOP concepts:
# classes, objects, attributes, methods, self, constructors, and inheritance.


# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # Store the three values in instance attributes.
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        # Return the student's information using HTML-like tags.
        return (
            f"<h2>{self.name}</h2>\n"
            f"<p>Course: {self.course}</p>\n"
            f"<p>Year Level: {self.year_level}</p>"
        )


# Child class for an IT student. Inherits name/course/year_level and
# get_profile() from Student, and adds a programming skill.
class ITStudent(Student):
    # Class attribute shared by IT students (can be overridden per instance).
    skill = "Python"

    def get_skill(self):
        # Return the programming skill using a <p> tag.
        return f"<p>Programming Skill: {self.skill}</p>"


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # Store the app title and the student object to display.
        self.title = title
        self.student = student

    def route(self, path):
        # Process the route path and return the matching HTML-like content.
        if path == "/":
            return f"<h1>{self.title}</h1>"
        elif path == "/profile":
            # Combine the inherited profile with the IT-specific skill.
            return f"{self.student.get_profile()}\n{self.student.get_skill()}"
        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        # Print the app name, then simulate GET requests to each route.
        print(f"Running: {self.title}\n")

        routes_to_test = ["/", "/profile", "/unknown"]
        for path in routes_to_test:
            print(f"GET {path}")
            print(self.route(path))
            print()


# Create the student and application objects.
student = ITStudent("Mary Ann O. Elijan", "BSIT - Web and Mobile Technologies", 4)
app = StudentApp("Student Profile App", student)

# Start the application.
app.run()