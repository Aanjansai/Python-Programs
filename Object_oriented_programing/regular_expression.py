import re
import datetime


class RegularExpression:

    def regex_method(self):
        sentence = "hello <<username>>, We have your full name as <<full name>> in our system."
        first_name = input("enter your first name\n")
        sentence_one = re.sub("<<username>>", first_name, sentence)
        full_name = input("enter your full name\n")
        sentence_two = re.sub("<<full name>>", full_name, sentence_one)
        print(sentence_two, "\n")

        try:
            contact_sentence = "your contact number is 91-xxxxxxxxxx."
            contact_number = int(input("enter your mobile number\n"))
            new_contact_number = str(contact_number)
            new_sentence = re.sub("xxxxxxxxxx", new_contact_number, contact_sentence)
            print(new_sentence, "\n")
        except ValueError:
            print("enter the data in numbers\n")

        date_sentence = "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
        date = datetime.date.today()
        replaced_date = str(date)
        bridge_labs = re.sub("01/01/2016", replaced_date, date_sentence)
        print(bridge_labs)


object1 = RegularExpression()

if __name__ == '__main__':
    object1.regex_method()


