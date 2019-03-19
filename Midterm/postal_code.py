#! /usr/bin/env python3

def main():
    password = input("Please enter your password: ")
    accepted = False
    if password == "please":
        accepted = True
        print("Password accepted.")
    else:
        print("Ah ah ah, you didn't say the magic word.")

    if accepted == True:
        post_code = input("Please enter your postal code for validation.")
        post_code = post_code.replace(" ", "")
        validate(post_code)
    return

def validate(postal_code):
    valid = False
    if len(postal_code) != 6:
        print("A Postal Code must be 6 characters long")

    if postal_code[0].isalpha() == False:
        print("Postal Code character 1 must be a letter not", postal_code[0])
    if postal_code[1].isdigit() == False:
        print("Postal Code character 2 must be a letter not", postal_code[1])
    if postal_code[2].isalpha() == False:
        print("Postal Code character 3 must be a letter not", postal_code[2])
    if postal_code[3].isdigit() == False:
        print("Postal Code character 4 must be a letter not", postal_code[3])
    if postal_code[4].isalpha() == False:
        print("Postal Code character 5 must be a letter not", postal_code[4])
    if postal_code[5].isdigit() == False:
        print("Postal Code character 6 must be a letter not", postal_code[5])

    if postal_code[0].isalpha() == True and postal_code[2].isalpha() == True and  postal_code[4].isalpha() == True and postal_code[1].isdigit() == True and postal_code[3].isdigit() == True and postal_code[5].isdigit() == True:
        print("Valid")
        valid = True

    return valid

if __name__ == "__main__":
    main()