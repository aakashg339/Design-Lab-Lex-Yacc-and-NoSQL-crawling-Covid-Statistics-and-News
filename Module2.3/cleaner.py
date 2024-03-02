import re

# Open file dataUrls.txt and read the file names
filenames = []
filenameAndYearMap = {}

with open("dataUrls.txt", "r") as file:
    fileNames = file.readlines()
    for i in range(len(fileNames)):
        # file name is present before '|'. So, split the string and take the first part. ALso add .txt at end of file name. Also files are in folder 'extractedData'
        fileNames[i] = "extractedData/"+fileNames[i].split("|")[0].strip()+".txt"
        filenames.append(fileNames[i])
        # Also create a map of filename and year
        # extract year from file name
        year = re.findall(r'\d+', fileNames[i])
        filenameAndYearMap[fileNames[i]] = year[0]

    file.close()

# Open each file and read data
for filename in filenames:
    # if filename contains 'India', 'Australia', 'Malaysia' then only open the file
    if "India" in filename or "Australia" in filename or "Malaysia" in filename:
        try:
            # Open the file
            with open(filename, "r") as file:
                # read each data line by line
                data = file.readlines()
                file.close()

                newData = []
                for i in data:
                    # Split data as per first ',' and check if it contains month names such as Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
                    # If it contains then keep the data else remove the data
                    dataSplited = i.split(",")[0]
                    if "Jan" in dataSplited or "Feb" in dataSplited or "Mar" in dataSplited or "Apr" in dataSplited or "May" in dataSplited or "Jun" in dataSplited or "Jul" in dataSplited or "Aug" in dataSplited or "Sep" in dataSplited or "Oct" in dataSplited or "Nov" in dataSplited or "Dec" in dataSplited:
                        if len(dataSplited) < 20:
                            # combine the data by placing '|' in place of first ',' and remove 'On', 'As of'and 'By' from i.split(",")[0]. Also keep till Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec before i.split(",")[0]
                            key = i.split(",")[0].replace("On", "").replace("As of", "").replace("By", "").strip()
                            # Only keeping till Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec and seperate number and Jan with '-'
                            key = key.split(" ")[0]+"-"+key.split(" ")[1]
                            # add year to key
                            key = key+"-"+filenameAndYearMap[filename]
                            value = i.split(",")[1:]
                            value = ",".join(value)
                            newData.append(key+"|"+value)

                    # else:
                    #     print("Removed: "+i)
                data = newData

                # Save the data to same file erasing the previous data
                with open(filename, "w") as file:
                    for i in data:
                        file.write(i)
                    file.close()
        except IOError:
            print("Error opening file "+filename)
            continue
    elif 'England' in filename:
        try:
            # Open the file
            with open(filename, "r") as file:
                # read each data line by line
                data = file.readlines()
                file.close()

                newData = []
                for i in data:
                    # Split data as per first ',' and check if it contains month names such as Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
                    # If it contains then keep the data else remove the data
                    try:
                        if "–" in i:
                            dataSplited = i.split(" – ")[0]
                            if "Jan" in dataSplited or "Feb" in dataSplited or "Mar" in dataSplited or "Apr" in dataSplited or "May" in dataSplited or "Jun" in dataSplited or "Jul" in dataSplited or "Aug" in dataSplited or "Sep" in dataSplited or "Oct" in dataSplited or "Nov" in dataSplited or "Dec" in dataSplited:
                                if len(dataSplited) < 20:
                                    # combine the data by placing '|' in place of first ',' and remove 'On', 'As of'and 'By' from i.split(",")[0]. Also keep till Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec before i.split(",")[0]
                                    key = dataSplited.replace("On", "").replace("As of", "").replace("By", "").strip()
                                    # Only keeping till Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec and seperate number and Jan with '-'
                                    key = key.split(" ")[0]+"-"+key.split(" ")[1]
                                    # add year to key
                                    key = key+"-"+filenameAndYearMap[filename]
                                    value = i.split(" – ")[1:]
                                    value = " – ".join(value)
                                    newData.append(key+"|"+value)

                        else:
                            continue
                    except:
                        continue
                data = newData

                # Save the data to same file erasing the previous data
                with open(filename, "w") as file:
                    for i in data:
                        file.write(i)
                    file.close()
        except IOError:
            print("Error opening file "+filename)
            continue

# Check for more errors and removing those from the file
# From each file, spliting as per '|' to get key and value. There is possibility of multiple entries for the key. IN that case just keep the first entry and remove the rest
# Also remove the key which has no value
for filename in filenames:
    try:
        # Open the file
        with open(filename, "r") as file:
            # read each data line by line
            data = file.readlines()
            file.close()

            newData = []
            keyList = []
            for i in data:
                # Split data as per first '|'
                key = i.split("|")[0]
                value = i.split("|")[1]
                # if key is not present in keyList then add it to keyList and also add the value to newData
                if key not in keyList:
                    keyList.append(key)
                    newData.append(key+"|"+value)

            data = newData

            # Save the data to same file erasing the previous data
            with open(filename, "w") as file:
                for i in data:
                    file.write(i)
                file.close()
    except IOError:
        print("Error opening file "+filename)
        continue
