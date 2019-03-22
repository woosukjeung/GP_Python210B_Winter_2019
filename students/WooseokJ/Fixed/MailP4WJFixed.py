import sys
import datetime



def menu():
    return(''''Menu
    Please choose from below options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Exit the program
    4 - Print thank you letter to all current donors''')


# first it will ask to choose a name whoom you would want to send the mail
# along side that when typing list it will give you all the names on the current list
# second if the name is not in the list then it will prompt to add the name into the data base
# lastly it will print the message of the email
#added excepts to close off any errors that has to do with input errors
def send_a_thankyou():
    '''send a thankyou note to donor'''
    while True:
        # prompt for a full name
        fullname = input("Enter full name of a donor (type 'list' to show all info of current donors) or type"
                         " 'quit' to leave: ")
        if fullname.lower() == 'list':
            print(donor_db)
        elif fullname.lower() == 'quit':
            break
        else:
            while True:
                try:
                    donation_amount = float(input("Enter the donation amount: "))
                    break
                except ValueError:
                    print("Donation amount has to be a number, try again.")
            add_donor(fullname, donation_amount, donor_db)
            print(f"${donation_amount} has been added to {fullname}'s donation history.")
            break
    print()

def add_donor(fullname, donation_amount, donor_dict):
    donor_list = [donor.lower() for donor in donor_dict]
    if fullname.lower() not in donor_list:
        print(f'{fullname} does not exist in current donor data, '
              f'adding {fullname} to the donor data.')
        donor_dict[fullname] = [1,donation_amount]
    elif fullname.lower() in donor_list:
        donor_dict[fullname][1] = donor_dict[fullname][1] + 1
        donor_dict[fullname][0] = donor_dict[fullname][0] + donation_amount
    return fullname, donor_dict[fullname]

# this prints out the database of the donors with their total amaounts and average amount donated
def create_a_report():
    summary = []
    headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']
    print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
    .format(headers[0], headers[1], headers[2], headers[3]))

    donor_totals = {donor: sum(donations) for donor, donations in donor_db.items()}
    sorted_donor_totals = sorted((value, key)
                                 for (key, value) in donor_totals.items())
    for total_donor in sorted_donor_totals[::-1]:
        print('{:25} | ${:<11,} | {:^19} | ${:<16,}'.format(
            total_donor[1], total_donor[0], len(donor_db[total_donor[1]]), (total_donor[0] / len(donor_db[total_donor[1]]))))
    print('\n\n')


def create_a_report_test(key, val):
    '''create a report in tabular and return to original prompt'''
    return "{:<25} ${:>13.2f} {:>13}  ${:>12.2f}".format(key, val[0], val[1], val[0]/val[1])


def sort_total_donation(number):
    return number[1][0]


# this makes a text that has the thankyou message to all the current doners on the list
# the title of the file has the date and the name of the person on the list
def send_letters_to_all_donors():
    '''generate thank you letter to all donors'''
    for key in donor_db:
        with open(key + "_" + str(datetime.date.today()) + ".txt", 'w') as f:
            f.write("Dear {name},\n"
                    "\n"
                    "        Thank you for your very kind donation of ${amount:10.2f}.\n"
                    "\n"
                    "        It will be put to very good use.\n"
                    "\n"
                    "                       Sincerely\n"
                    "                          -The Team".format(name=key, amount=donor_db[key][0]))


def send_letters_to_all_donors_test(key, donor_dict):
    '''generate thankyou letter to all donors'''
    return ("Dear {name},\n"
            "\n"
            "        Thank you for your very kind donation of ${amount:10.2f}.\n"
            "\n"
            "                       Sincerely\n"
            "                          -The Team".format(name=key, amount=donor_dict[key][0]))

def exit_program():
    print("Terminating program")
    sys.exit(0)


def main():
    while True:
        try:
            choice = ''
            choice = int(input(menu()))
            if choice in main_menu:
                main_menu[choice]()
            else:
                print("Not a valid option, try again.")
        except ValueError:
            print("Selection has to be a number, try again.\n")

# the main frame of the console
main_menu = {1: send_a_thankyou,
             2: create_a_report,
             3: exit_program,
             4: send_letters_to_all_donors
             }

if __name__ == "__main__":
    donor_db = {"William Gates, III": [653784.49, 2],
                "Mark Zuckerberg": [16396.10, 3],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [708.42, 3],
                }

    main()