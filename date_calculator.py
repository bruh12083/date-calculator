#######################################
# Mission 1: Date Calculator Template #
#######################################

#############################
# Task 1 - Helper Functions #
#############################


###########
# Task 1a #
###########
def is_leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


###########
# Task 1b #
###########
def days_in_month(month):
    days_in_month = [
        31,  # January
        28,  # February
        31,  # March
        30,  # April
        31,  # May
        30,  # June
        31,  # July
        31,  # August
        30,  # September
        31,  # October
        30,  # November
        31,  # December
    ]
    return days_in_month[month - 1]


###########
# Task 1c #
###########
def num_of_leap_years(start_year, end_year):
    leap_year_count = 0

    for year in range(start_year, end_year):
        if is_leap_year(year):
            leap_year_count += 1

    return leap_year_count


###########
# Task 1d #
###########
def is_valid_date(date):
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])

    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month(month):
        if month == 2 and day == 29 and is_leap_year(year):
            return True
        return False

    return True


###########################
# Task 2 - Main Functions #
###########################


###########
# Task 2a #
###########
def num_of_days_from_1900(date):
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
    total_days = 0

    total_days += (year - 1900) * 365  # Number of days from years
    total_days += num_of_leap_years(
        1900, year
    )  # Add leap year correction for entire years

    for m in range(1, month):
        total_days += days_in_month(m)
        if m == 2 and is_leap_year(year):
            total_days += 1  # Leap year correction for current year

    total_days += day - 1  # Add days of current month

    return total_days


###########
# Task 2b #
###########
def days_between_2_dates(date1, date2):
    days1 = num_of_days_from_1900(date1)
    days2 = num_of_days_from_1900(date2)

    return abs(days2 - days1)


###########
# Task 2c #
###########
def add_n_days_after_1900(days):
    year = 1900
    month = 1

    while days >= 365:
        if is_leap_year(year) and days > 365:
            days -= 366
            year += 1
        elif not is_leap_year(year) and days >= 365:
            days -= 365
            year += 1
        else:
            break

    while days >= 28:  # Reduced threshold to 28
        if month == 2 and is_leap_year(year):
            if days >= 29:
                days -= 29
                month += 1
            else:
                break  # Breaking the loop if days left are less than 29
        elif days >= days_in_month(month):
            days -= days_in_month(month)
            month += 1
        else:
            break

    day = days + 1

    return "{:02d}{:02d}{:04d}".format(day, month, year)


###########
# Task 2d #
###########
def add_n_days_from_a_date(date, days):
    total_days = num_of_days_from_1900(date) + days
    return add_n_days_after_1900(total_days)


###########
# Task 2e #
###########
def weekday_of_date(date):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    total_days = num_of_days_from_1900(date)
    return weekdays[total_days % 7]


############################
# Task 3 - Date Calculator #
############################
def date_calculator():
    done = False
    while not done:
        print("-----------------------------------------")
        print("Welcome to date calculator")
        print("  1. Calculate number of days between 2 dates.")
        print("  2. Add n days from a date.")
        print("  3. Find weekday of a date.")
        print("  4. Exit the programme.")
        print("  5. Test using provided testcases. \n")
        print(
            "**Please note the format of date should follow the format of 'DDMMYYYY'\n"
        )

        option = int(input("Select a function: "))

        if option == 1:
            date1 = input("Enter the first date (DDMMYYYY): ")
            date2 = input("Enter the second date (DDMMYYYY): ")
            print(
                "Number of days between {} and {}: {}".format(
                    date1, date2, days_between_2_dates(date1, date2)
                )
            )
        elif option == 2:
            date = input("Enter the date (DDMMYYYY): ")
            days = int(input("Enter the number of days to add: "))
            print("The new date is: {}".format(add_n_days_from_a_date(date, days)))
        elif option == 3:
            date = input("Enter the date (DDMMYYYY): ")
            print("The day of the week is: {}".format(weekday_of_date(date)))
        elif option == 4:
            done = True
        elif option == 5:
            print(is_leap_year(2000))  # True
            print(is_leap_year(1900))  # False
            print(is_leap_year(1984))  # True
            print(is_leap_year(2015))  # False
            for i in range(1, 13):
                print(i, days_in_month(i))
            print(num_of_leap_years(2010, 2016))  # 1
            print(num_of_leap_years(2008, 2013))  # 2
            print(num_of_leap_years(1900, 2016))  # 28
            print(is_valid_date("29022016"))  # True
            print(is_valid_date("31042015"))  # False
            print(is_valid_date("29022015"))  # False
            print(num_of_days_from_1900("30011900"))  # 29
            print(num_of_days_from_1900("28021900"))  # 58
            print(num_of_days_from_1900("01031904"))  # 1520
            print(num_of_days_from_1900("31012016"))  # 42398

            print(days_between_2_dates("15041984", "26102000"))  # 6038
            print(days_between_2_dates("26102000", "15041984"))  # 6038
            print(days_between_2_dates("26102000", "31012016"))  # 5575

            print(add_n_days_after_1900(30))  # "31011900"
            print(add_n_days_after_1900(31))  # "01021900"
            print(add_n_days_after_1900(59))  # "01031900"
            print(add_n_days_after_1900(1519))  # "29021904"
            print(add_n_days_after_1900(1520))  # "01031904"

            print(add_n_days_from_a_date("15041984", 6038))  # 26102000
            print(add_n_days_from_a_date("26102000", 6038))  # 08052017
            print(weekday_of_date("01011900"))  # "Monday"
            print(weekday_of_date("02011900"))  # "Tuesday"
            print(weekday_of_date("31012016"))  # "Sunday"
        else:
            print("Invalid option. Please choose a number between 1 and 5.")


date_calculator()
