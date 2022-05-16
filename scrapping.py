from bs4 import BeautifulSoup
# with open('test.html','r') as data:
#     string_data = data.read()
#     soup = BeautifulSoup(string_data,'lxml')
#     course_name = soup.find('h5',class_='card-title').text
#     course_description = soup.find('p',class_='card-text').text
#     course_price = soup.find('a',class_='btn btn-primary').text.split(' ')[-1]
#     print(course_price)

my_course_list = []
with open('test.html','r') as data:
    string_data = data.read()
    soup = BeautifulSoup(string_data,'lxml')
    all_div = soup.find_all('div',class_='card-body')
    for item in all_div:
        course_name = item.find('h5',class_='card-title').text
        course_description = item.find('p',class_='card-text').text
        course_price = item.find('a',class_='btn btn-primary').text.split(' ')[-1]

        my_course_info = {
            'Course Name':course_name,
            'Course Description':course_description,
            'Course Price':course_price
        }

        my_course_list.append(my_course_info)


import pandas as pd
df = pd.DataFrame(my_course_list)
df.to_csv('Course_Info.csv')