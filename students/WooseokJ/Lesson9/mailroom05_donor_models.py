import operator

class Donor():
    def __init__(self, fullname='', *args):
        self.fullname = fullname
        self.donations = list(args)
    @staticmethod
    def send_a_thankyou(fullname, donation_amount):
        return f'Thank you {fullname} for your generous donation of ${donation_amount:^10.2f}!'


class DonorCollection():
    donor_db = {}

    @staticmethod
    def add_donor(fullname, donation_data):
        DonorCollection.donor_db[fullname] = donation_data

    @staticmethod
    def add_donation(fullname, donation_amount):
        DonorCollection.donor_db[fullname][0] += donation_amount
        DonorCollection.donor_db[fullname][1] += 1
        return f"${donation_amount} has been added to {fullname}'s donation history."

    @staticmethod
    def list_all_names():
        return str(DonorCollection.donor_db.keys())

    @staticmethod
    def create_a_report():
        sorted_donor_db = sorted(DonorCollection.donor_db.items(), key=operator.itemgetter(1),
                                   reverse=True)
        report_string = ''
        for key, val in sorted_donor_db:
            report_string += DonorCollection.create_a_report_text(key, val)
        return report_string

    @staticmethod
    def create_a_report_text(key, val):
        '''create a report in tabular and return to original prompt'''
        return "{:<25} ${:>13.2f} {:>13}  ${:>12.2f}\n".format(key, val[0], val[1], val[0] / val[1])

    @staticmethod
    def create_a_report_header():
        '''create header of the report'''
        headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']
        print(f"\n{'-' * 80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-' * 80}"\
              .format(headers[0], headers[1], headers[2], headers[3]))