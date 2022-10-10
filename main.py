import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
   print(dt.datetime.now().date())



if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()