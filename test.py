enrolled_courses = ["Math", "Computer science", "Calculus", "Statistics", "Matematics", "Matatu", "Mali"]

# def display_courses(courses):
#     print("Available courses:")
#     for index, course in enumerate(courses, start = 1):
#         print (f"{index}.{course}")

# display_courses(enrolled_courses)

# def add_course(enrolled_courses, new_course):
#     enrolled_courses.append(new_course)
#     print(f"{new_course} has been added to the course list.")
#     print(enrolled_courses)

# add_course(enrolled_courses, "Physics 102")

# def drop_course(enrolled_courses, course_name):
#     if course_name in enrolled_courses:
#         enrolled_courses.remove(course_name)
#         print(f"{course_name} has been removed from your list of courses")
#     else:
#         print(f"{course_name} is not in your list of courses.")

# drop_course(enrolled_courses, "Math")
# print(enrolled_courses)

# def filter_courses(enrolled_courses, keyword):
#     filtered_courses = [course for course in enrolled_courses if keyword.lower() in course.lower()]
#     return filtered_courses
    
# filtered_courses = filter_courses(enrolled_courses, "ma")
# print(f"Here is a list of courses matching your keyward: {filtered_courses}")

# def course_generator(courses, keyword):
#     return(course for course in courses if keyword.lower() in course.lower())

# science_courses = course_generator(enrolled_courses, "Science")
# print(next(science_courses))