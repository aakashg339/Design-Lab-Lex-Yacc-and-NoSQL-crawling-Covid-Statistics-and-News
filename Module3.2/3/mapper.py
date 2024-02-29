import sys
import datetime

# Used to count the number of nodes with degree >= 20
class Mapper:
    def __init__(self):
        pass

    def mapper(self):

        for line in sys.stdin:
            datas = line.strip().split("|")

            # Check if the first column is date in format 'dd-Month-YYYY'
            try:
                date_object = datetime.datetime.strptime(datas[0], '%d-%B-%Y')
            except:
                continue
            
            # check if date object is null
            # if date_object is None:
            #     continue

            # print(date_object)

            formatted_date = date_object.strftime('%d-%b-%Y')

            print("{}|{}".format(formatted_date, formatted_date))
    
if __name__ == "__main__":
    mapperObj = Mapper()
    mapperObj.mapper()