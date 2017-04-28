def main():

    course_num = input('What is the course number?: ')

    room = room_number()
    room_num = room[course_num]

    instructor = instructor_name()
    name_instructor = instructor[course_num]

    time = meeting_time()
    class_time = time[course_num]

    print('For', course_num, 'the room number is', room_num, 'and the instructor name is', name_instructor, 'and the meeting time is', class_time)

def room_number():
    room = {'CIS101' : '3004', 'CIS102' : '4501', 'CIS103' : '6755', 'NT110' : '1244', 'CM241' : '1411'}
    return room

def instructor_name():
    instructor = {'CIS101' : 'Haynes', 'CIS102' : 'Alvarado', 'CIS103' : 'Rich', 'NT110' : 'Burke', 'CM241' : 'Lee'}
    return instructor

def meeting_time():
    time = {'CIS101' : '8:00 a.m.', 'CIS102' : '9:00 a.m.', 'CIS103' : '10:00 a.m.', 'NT110' : '11:00 a.m.', 'CM241' : '1:00 p.m.'}
    return time

main()