from datetime import datetime

def date(date_input):
    date_object = datetime.strptime(date_input, '%m/%d/%Y')
    print(date_object.strftime('%B %d, %Y'))

def main():
    date_input = input('Enter a date(mm/dd/yyyy): ')
    date(date_input)

main()
