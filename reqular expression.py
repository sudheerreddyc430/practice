#import sys
# #
# # # it's easy to print this list of course:
# # print(sys.argv)
# #
# # # or it can be iterated via a for loop:
# #
# # for i in range(len(sys.argv)):
# #     if i == 0:
# #         print("Function name: %s" % sys.argv[0])
# #     else:
# #         print("%d. argument: %s" % (i,sys.argv[i]))
# #

# print(sys.path)

# def f1():
#     print("hello")
# f1()
# print(f1())

#from os import listdir
# from os.path import isfile,join,isdir
# path='C:/Users/chevsudh/Downloads/'
# for f in listdir(path):
#     if isdir(join(path,f)):
#         print(f)

import os
# import glob
#
# os.chdir('C:/Users/chevsudh/Downloads/')
# for file in glob.glob('*.xlsx'):
#     print(file)


print(os.getcwd())

#os.mkdir("newdir")
#os.rename('newdir','newdir52')
#os.rmdir('newdir52')