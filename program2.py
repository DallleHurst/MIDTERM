# this function collects user input and converts it into Month/Day/Year format
def translate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%B %d, %Y")
        formatted_date = date_obj.strftime("%m/%d/%Y")
        print("Converted Date:", formatted_date)
    except ValueError:
        print("Invalid date format. Use 'Month Day, Year' (e.g., January 24, 2054).")

user_date = input("Enter a date (ex. January 24, 2054): ")
translate_date(user_date)