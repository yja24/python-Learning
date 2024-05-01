#exception with raise 
#try:
 #   age=int(input("enter your age-"))
  #  if age<18:
   #     raise ValueError
    #else:
     #   print("valid")

#except ValueError:
 #   print("not valid")


#user defined exceptions
class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass
number=11
while True:
    try:
        num=int(input("enter your desired number-"))
        
        if num<number:
            raise ValueTooSmallError
        elif num>number:
            raise ValueTooLargeError
        break
    
    except ValueTooSmallError:
        print("this value is too small")
    except ValueTooLargeError:
        print('this value is too large')

print("congo!!!")