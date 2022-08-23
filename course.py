from school import School

class Course:
    """Course class """
   
    def __init__(self, course_id, name, credits, instructor_name):
        Course._validate_int(course_id)
        self._course_id = course_id
        Course._validate_string("Course Name", name)
        self._name = name
        Course._validate_int(credits)
        self._credits = credits
        Course._validate_string("Instructor Name", instructor_name)
        self._instructor_name = instructor_name

   
    def get_course_id(self):
        """Return course id"""
        return self._course_id

  
    def get_name(self):
        """Return course name"""
        return self._name

 
    def get_credits(self):
        """Return course credits"""
        return self._credits


    def get_instructor_name(self):
        """Return instructor name"""
        return self._instructor_name

    #get_course_summary(): string
    def get_course_summary(self):
        """Return course summary"""
        return "Summary for the School of Computing and Academic Studies: Course {} ({}) is a {} credit course taught by {}.".format(self._name, self._course_id, self._credits, self._instructor_name)


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
