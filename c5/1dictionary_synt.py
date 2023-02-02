firstDictionary = {
    "Name": "Nur Hasan Masum",
    "Email": "masumhasan92@gmail.com",
    "Marks": [5.0, 4.44, 3.8],
    "newDick": {"address": "Thakurgaon"}
}
print(firstDictionary["Name"])  # access a dictionary element by key
print(firstDictionary["Email"])
print(firstDictionary["Marks"])
# access element of a dictionary inside another dictionary
print(firstDictionary['newDick']['address'])
