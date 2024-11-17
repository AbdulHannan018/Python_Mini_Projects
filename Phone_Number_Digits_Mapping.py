user_input_phone_number = input("Enter a Phone Number: ")
digits = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}

mapped_digits = ""
for each_digit in user_input_phone_number:
    mapped_digits += digits.get(each_digit, "!") + " "   #! for any digit which is not present in the digits such as space or -
print(mapped_digits)