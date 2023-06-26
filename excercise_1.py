sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

test = {word:23 for word in sentence.split()}

print(result)

print(test)