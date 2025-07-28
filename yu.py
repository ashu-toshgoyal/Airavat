import json

dictionary = {
    "name": "sathiyajith",
    "rollno": 23,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("data.json", "w") as outfile:
    outfile.write(json_object)