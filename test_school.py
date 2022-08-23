from course import Course
from school import School

#this script should create 1 instance of a School object with a maximum of 3 courses, and add 4 courses to the School. 
#Print the school summary. Remove 1 Course from the School and print the school summary again.
#Remove all remaining courses and prit the school summary a final time. It should ignore the fourth course and print the same summary as before.

def main():

    #If it is more than 3 courses, it should raise an error.
    if len(school.get_courses()) > 3:
        raise ValueError("Max courses cannot be greater than 3")
    school = School("School of Computing and Academic Studies", 3)
    course1 = Course(101, "ACIT 2515", 4, "Mike Mulder")
    course2 = Course(210, "COMP 1510", 6, "Julie Chen")
    course3 = Course(512, "MATH 1100", 4, "Sam Jones")
    course4 = Course(104, "COMP 2629", 3, "Lei Zhang")
    school.add_course(course1)
    school.add_course(course2)
    school.add_course(course3)
    school.add_course(course4)
    print(school.get_school_summary())
    school.remove_course(course2)
    print(school.get_school_summary())
    school.remove_course(course3)
    school.remove_course(course4)
    print(school.get_school_summary())


if __name__ == "__main__":
    main()
    