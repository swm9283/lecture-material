# decorator
#decorator
def document_info(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args,**kwargs)
        print("Result:", result)
        return result
    return new_function

def sub_int(x,y):
    return  x - y

print(sub_int(7,3))

#수동방식
info_sub_int = document_info(sub_int)
r = info_sub_int(7,3)
print(r)
