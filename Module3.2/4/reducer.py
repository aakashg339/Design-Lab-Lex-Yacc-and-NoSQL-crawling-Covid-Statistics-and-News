import sys
import datetime

# Used to get the nodes which are having an edge to any one of the top 10 nodes with maximum frequency
class Reducer:
    def __init__(self):
        pass

    def reducer(self):
        for line in sys.stdin:

            datas = line.strip().split("|")

            # Check if the first column is date in format 'dd-Month-YYYY'
            try:
                date_object = datetime.datetime.strptime(datas[0], '%d-%b-%Y')
            except:
                continue

            # If the date is within the range, print the date
            print("{}|{}".format(datas[0], datas[1]))


if __name__ == "__main__":
    reducerObj = Reducer()
    reducerObj.reducer()