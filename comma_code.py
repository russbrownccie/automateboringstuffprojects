# This code takes a list of items, passes it into a function and makes it a string,
# with commas and the word and at the end
# in proper english style - the following list (spam) should produce the string
# "apples, bananas, tofu, and cats"

def comma_code(mylist):
    try:  # some error correction for an empty list
        new_list = mylist.copy()  # allows me to run the command more than once - creates a new list
        last_item = len(mylist)  # this and next line give me the right index number for the list
        last_item -= 1
        last_string = mylist[last_item]  # gives me the last string item
        new_list.pop(last_item)  # begins altering list - this is the new list we alter
        new_list.append(f'and {last_string}.')  # adds it back with extra string comments
        alpha = ', '.join(new_list)  # creates the string from the list
        print(alpha)
    except IndexError:
        print('You must use a list with contents')


spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = []

comma_code(spam2)
comma_code(spam)
comma_code(spam)
