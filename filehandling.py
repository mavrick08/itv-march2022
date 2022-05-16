"""
1) opening the file 
2) do any kind of desired operation
3) close the open file
"""

# data = open('sample.txt','r')
# # print(data.read())
# # print(data.readline())
# # print(data.readline())
# print(data.readlines())
# data.close()


# with open('sample.txt','r') as data:
#     print(data.read())


"""
Append Mode : appends the data in the existing file without 
losing the original content of the file
"""
# with open('sample.txt','a') as inp_data:
#     inp_data.write('\n')
#     inp_data.write('This is a new line')
#     inp_data.write('HELLO')


# with open('demo.txt','w') as inp:
#     inp.write("Trying for some modification")


# with open('demo.txt','w') as data:
#     data.writelines(['Line1\n','Line2\n','Line3\n'])

# with open('sample.txt','r') as inp:
#     inp.seek(27)
#     print(inp.readline())



"""
copying data from one file to another program
"""

# with open('sample.txt','r') as data:
#     with open('copied.txt','w') as inp:
#         inp.write(data.read())


# with open('Python.png','rb') as img_data:
#     print(img_data.read())

import pickle

# test_dict = {'Name':'Punit','Age':29,'Loc':'Santacruz'}

# with open('secret.pickle','wb') as output:
#     pickle.dump(test_dict,output)



"""
De-Serialization
"""

# with open('secret.pickle','rb') as inp_file:
#     output_data = pickle.load(inp_file)
#     print(output_data)


import os
print(os.getcwd())

# os.mkdir('TEST')
# os.rmdir('TEST')
source_path = '/home/punit/Downloads/IT-V/march2022/copied.txt'

dest_path = '/home/punit/Downloads/IT-V/march2022/Copy.txt'


# os.rename(source_path,dest_path)

os.remove('/home/punit/Downloads/IT-V/march2022/Python.png')
