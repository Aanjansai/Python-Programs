# author: Sai Anjan
# task  : Object Oriented programming
# date  : 24/01/19

""" Desc -> Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system.
    your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification
    Thank you BridgeLabz 01/01/2016. Use Regex to replace name, full name, Mobile#, and Date with proper value.
    I/P -> read in the Message
    Logic -> Use Regex to do the following
    Replace <<name>> by first name of the user ( assume you are the user)
    replace <<full name>> by user full name.
    replace any occurance of mobile number that should be in format 91-xxxxxxxxxx by your contact number.
    replace any date in the format XX/XX/XXXX by current date.
    O/P -> Print the Modified Message.
"""

import re
import datetime


class RegularExpression:                    # This method is created to display the details of the user

    def regex_method(self):
        sentence = "hello <<username>>, We have your full name as <<full name>> in our system."
        first_name = input("enter your first name\n")
        sentence_one = re.sub("<<username>>", first_name, sentence)     # re.sub is used to replace the string
        full_name = input("enter your full name\n")
        sentence_two = re.sub("<<full name>>", full_name, sentence_one)
        print(sentence_two, "\n")

        try:
            contact_sentence = "your contact number is 91-xxxxxxxxxx."
            contact_number = int(input("enter your mobile number\n"))
            new_contact_number = str(contact_number)                    # converting number to string
            new_sentence = re.sub("xxxxxxxxxx", new_contact_number, contact_sentence)  # replacing the number
            print(new_sentence, "\n")
        except ValueError:
            print("enter the data in numbers\n")

        date_sentence = "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
        date = datetime.date.today()                                    # datetime is used to display the date
        replaced_date = str(date)
        bridge_labs = re.sub("01/01/2016", replaced_date, date_sentence)
        print(bridge_labs, "\n")
        print("complete statement:")
        print(sentence_two, new_sentence)
        print(bridge_labs)


object1 = RegularExpression()

if __name__ == '__main__':
    try:
        object1.regex_method()                                      # calling regex method
    except UnboundLocalError:
        print("try again by entering the valid data")

