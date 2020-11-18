#import własnego modułu
def myMessage(string = "Hi this is a default massage"):
    print(string)
myvar = 10
if __name__ == '__main__':
    print("Script run as main script")
else:
    print("Script import module")