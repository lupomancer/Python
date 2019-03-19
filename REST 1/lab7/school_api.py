#!/usr/bin/env python3
#TODO: Fix all error codes
#! when creating get_school_details, use SET type for program list instead of LIST type

from flask import Flask, request
from course import Course
from school import School
import json

app = Flask(__name__)

school = School('BCIT')

@app.route('/school/courses', methods=['POST'])
def add_course():
    """adds a new course to school
    
    Returns:
        response -- status
    """

    content = request.json
    try:
        _validate_string_input('Course ID', content['course_id'])
        if len(content) == 4:
            if school.course_exists(content['course_id']):
                response = app.response_class(
                    response = 'Course exists',
                    status=400
                )
            else:
                course = Course(content['course_id'], content['crn'], content['program'])
                school.add_course(course)
                for student in content['students']:
                    course.add_student(student)

                response = app.response_class(
                    status=200
                )
        else:
            response = app.response_class(
                response='Course is invalid',
                status=400
            )
    except ValueError as e:
        response = app.response_class(
            response='Course is invalid',
            status=400
        )
    return response

@app.route('/school/courses/<course_id>', methods=['PUT'])
def update_course(course_id):
    """updates an existing course in the school
    
    Arguments:
        course_id {string} -- ID of course to be updated
    
    Returns:
        response -- status
    """

    content = request.json
    try:
        _validate_string_input('Course ID', content['course_id'])
        if len(content) == 4:
            if school.course_exists(course_id):
                course = Course(content['course_id'], content['crn'], content['program'])
                school.add_course(course)

                response = app.response_class(
                    status=200
                )
            else:
                response = app.response_class(
                    status=404
                )
        else:
            response = app.response_class(
                response='Course is invalid',
                status=400
            )
    except ValueError as e:
        response = app.response_class(
            response='Course is invalid',
            status=400
        )
    return response

@app.route('/school/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    """deletes a course in the school
    
    Arguments:
        course_id {string} -- ID of course to be deleted
    
    Returns:
        response -- status
    """

    try:
        _validate_string_input('Course ID', course_id)
        if school.course_exists(course_id):
            school.remove_course(course_id)

            response = app.response_class(
                status=200
            )
        else:
            response = app.response_class(
                response='Course does not exist',
                status=404
            )
    except ValueError as e:
        response = app.response_class(
            response='Course is invalid',
            status=400
        )
    return response

@app.route('/school/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    """gets a course in the school
    
    Arguments:
        course_id {string} -- ID of course to be retrieved
    
    Returns:
        response -- status
    """

    try:
        _validate_string_input('Course ID', course_id)
        if school.course_exists(course_id):
            school.get_course(course_id)
            course = school.get_course(course_id)
            response = app.response_class(
                status=200,
                response=json.dumps(course.to_dict()),
                mimetype='/application/json'
            )
        else:
            response = app.response_class(
                status=404
            )

    except ValueError as e:
        response = app.response_class(
            response='Course is invalid',
            status='400'
        )
    return response

@app.route('/school/courses/all', methods=['GET'])
def get_all_courses():
    """gets all courses in the school
    
    Returns:
        response -- status
    """

    courses = school.get_all_courses()

    course_list = []

    for course in courses:
        course_list.append(course.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(course_list),
        mimetype='/application/json'
    )
    return response

@app.route('/school/courses/program/<program_name>', methods=['GET'])
def get_courses_by_program(program_name):
    """gets all courses in a specific program in the school
    
    Arguments:
        program_name {string} -- program code
    
    Returns:
        response -- status
    """

    courses = school.get_all_courses()

    course_list = []

    for course in courses:
        if course.to_dict()['program'] == program_name:
            course_list.append(course.to_dict())
        else:
            pass

    if len(course_list) < 1: 
        response = app.response_class(
            status=404
        )
    else:
        response = app.response_class(
            status=200,
            response=json.dumps(course_list),
            mimetype='/application/json'
        )
    return response

@app.route('/school', methods=['GET'])
def get_school():
    """gets the school details
    
    Returns:
        response -- status
    """

    school_details = school.get_school_details()

    response = app.response_class(
        status=200,
        response=json.dumps(school_details),
        mimetype='application/json'
    )
    return response

def _validate_string_input(display_name, str_value):
    """ Private helper to validate string values """

    if str_value is None:
        raise ValueError(display_name + " cannot be undefined.")

    if str_value == "":
        raise ValueError(display_name + " cannot be empty.")

if __name__ == "__main__":
    app.run()
