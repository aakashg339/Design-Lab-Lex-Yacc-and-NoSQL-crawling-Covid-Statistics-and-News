import sys
import datetime

# Used to count the number of nodes with degree >= 20
class Combiner:
    def __init__(self):
        pass

    def combiner(self):

        currentStartDate = None
        currentEndDate = None
        for line in sys.stdin:

            startDate, endDate = line.strip().split("|")

            # Convert the date to date object
            try:
                startDate = datetime.datetime.strptime(startDate, '%d-%b-%Y')
                endDate = datetime.datetime.strptime(endDate, '%d-%b-%Y')
            except:
                continue
            
            # If current iteration is first iteration
            if currentStartDate is None:
                currentStartDate = startDate
                currentEndDate = endDate
                continue

            # If current iteration is not first iteration
            # Store the earliest start date and latest end date
            if currentStartDate > startDate:
                currentStartDate = startDate
            if currentEndDate < endDate:
                currentEndDate = endDate

        print("{}|{}".format(currentStartDate.strftime('%d-%b-%Y'), currentEndDate.strftime('%d-%b-%Y')))
    
if __name__ == "__main__":
    combinerObj = Combiner()
    combinerObj.combiner()