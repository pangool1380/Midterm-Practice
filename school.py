

class School:
    """School class """
    def __init__(self, school_name, max_courses):
        School._validate_string(school_name)
        self._school_name = school_name
        School._validate_int(max_courses)
        self._max_courses = max_courses
        self._courses = []

    def add_course(self, course):
        """Add course to school"""
        if course in self._courses:
            raise ValueError("Course already exists")
        else:
            self._courses.append(course)

    def remove_course(self, course):
        """Remove course from school"""
        if course in self._courses:
            self._courses.remove(course)
        else:
            raise ValueError("Course does not exist")

    def set_max_courses(self, new_max):
        """Set max courses"""
        if new_max > 10:
            raise ValueError("Max courses cannot be greater than 10")
        else:
            self._max_courses = new_max

    def get_max_courses(self):
        """Return max courses"""
        return self._max_courses


    def get_school_summary(self):
        """Return school summary"""
        summary = "Summary for the {}:".format(self._school_name)
        for course in self._courses:
            summary += "\n{}".format(course.get_course_summary())
        return summary


    @staticmethod
    def _validate_string(label, value):
        """ Values a string value """
        if value is None:
            raise ValueError(label + " must be defined.")
        if value == "":
            raise ValueError(label + " cannot be empty.")

    @staticmethod
    def _validate_int(label, value):
        """ Values a string value """
        if value is None:
            raise ValueError(label + " must be defined.")
        if type(value) != int:
            raise ValueError(label + " must be an integer.")
        if value < 0:
            raise ValueError(label + " must be positive.")


    

        

