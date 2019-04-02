# def html_tags(tag_name):
#     print( 'begin outer function.')
#     def wrapper_(func):
#         print ("begin of inner wrapper function.")
#         def wrapper(*args, **kwargs):
#             content = func(*args, **kwargs)
#             print("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
#         print( 'end of inner wrapper function.')
#         return wrapper
#     print('end of outer function')
#     return wrapper_
#
# @html_tags('b')
# def hello(name='Toby'):
#     return 'Hello {}!'.format(name)
#
# hello()
# hello()


flist = []
for i in range(3):
    def foo(x):
        print(x+i)
    flist.append(foo)
for f in flist:
    f(2)