

records = {}

with open('PeopleTrainngDate.csv', 'r') as data_file:
    headers = data_file.readline()
    headers = headers.split(",")
    print(headers)
    # Skip the header line: Title,Name,ID,Email,Company,Updated
    for ind, line in enumerate(data_file, 1):
        data = line.split(",")
        # Add line data to records dict for easier access of elements
        # Use unique ID as key
        records[data[3]] = {
            "Title": data[0],
            "Name": data[2],
            "Email": data[4],
            "Company": data[5],
            "Updated": data[6]
        }

fill = ''
align = '<'
spaces = 30

print(f'{headers[2]:{fill}{align}{spaces}}  {headers[0]:{fill}{align}{spaces}}  {headers[1]:{fill}{align}{spaces}}  {headers[3]:{fill}{align}{spaces}}  {headers[4]:{fill}{align}{spaces}}  {headers[5]:{fill}{align}{spaces}}')
for key, val in records.items():
    print(f'{key:{fill}{align}{spaces}}  {val["Title"]:{fill}{align}{spaces}}  {val["Name"]:{fill}{align}{spaces}}  {val["Email"]:{fill}{align}{spaces}}  {val["Company"]:{fill}{align}{spaces}}  {val["Updated"]:{fill}{align}{spaces}}')









    
