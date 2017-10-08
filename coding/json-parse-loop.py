
# Classification Data	
cars={"sportsCars":[{"Make":"Volkswagon","Model":"Porsche"},{"Make":"Dodge","Model":"Viper"},{"Make":"Chevy","Model":"Corvette"}]}

print("")
print("We're in the cars section of the code")
for car in cars["sportsCars"]:
    print("Make is: " + car["Make"])
    print("Model is: " + car["Model"])
    print("")

spark_rooms={
    "items": [
        {
            "title": "My Cool Room!"
        },
        {
            "title": "DevNet Fun!"
        },
        {
            "title": "Room with a View!"
        }        
    ]
}


print("We're in the Spark part of the code now")
for room in spark_rooms["items"]:
    print('The room name is ',room["title"])
    print("")


spark_rooms={
    "items": [
        {
            "lastActivity": "2017-02-02T23:04:47.612Z",
            "title": "LL Publishing"
        },
        {
            "lastActivity": "2017-02-06T23:14:22.409Z",
            "title": "My Cool Room!"
        },
        {
            "lastActivity": "2017-02-03T21:57:18.563Z",
            "title": "DNE Event Room"
        }
    ]
}

### Write loop here to parse and print data




spark_rooms={
    "items": [
        {
            "id": "Y2lzY29zcGFyazovLVzL1JPT00vNDQ2NTIxZTAtZTk5Yi0xMWU2LWFmNjktM2JjOGZhOWE1dr",
            "isLocked": "false",
            "title": "DevNet Fun Room!"
        },
        {
            "id": "Y2lzY29zcGFyazovLVzL1JPT00vNWQzOWQ1ZjAtZTk2Yy0xMWU2LTlmYjAtMDkzZjI4Yjc471",
            "isLocked": "false",
            "title": "Room With a View"
        },
        {
            "id": "Y2lzY29zcGFyazovLVzL1JPT00vZTY2Yzc3ZDAtZTRjNC0xMWU2LWJjNGItNjliMTc1N2J633",
            "isLocked": "false",
            "title": "Living Room"
        }        
    ]
}

### Write loop here to parse and print data
