import sys
import datetime

# Used to count the number of nodes with degree >= 20
class Mapper:
    def __init__(self):
        pass

    def mapper(self):

        # Take date range from command line
        startDate = sys.argv[1]
        endDate = sys.argv[2]

        # Convert the date to date object
        try:
            startDate = datetime.datetime.strptime(startDate, '%d-%B-%Y')
            endDate = datetime.datetime.strptime(endDate, '%d-%B-%Y')
        except:
            print("Invalid date")
            return

        for line in sys.stdin:
            datas = line.strip().split("|")

            # Check if the first column is date in format 'dd-Month-YYYY'
            try:
                date_object = datetime.datetime.strptime(datas[0], '%d-%B-%Y')
            except:
                continue

            # If the date is within the range, print the date
            if date_object >= startDate and date_object <= endDate:
                formatted_date = date_object.strftime('%d-%b-%Y')
                print("{}|{}".format(formatted_date, datas[1]))
    
if __name__ == "__main__":
    mapperObj = Mapper()
    mapperObj.mapper()