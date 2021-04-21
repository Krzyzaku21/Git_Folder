def calc(arguments):
    if arguments == 1:
        return 1
    else:
        return arguments + calc(arguments - 1)


nums = 5
print(calc(nums))
