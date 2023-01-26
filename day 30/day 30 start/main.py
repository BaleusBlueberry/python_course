
try:
  file = open("a_file.txt")
  # text = {"key": "value"}
  # print(text["sasas"])
except FileNotFoundError:
  file = open("a_file.txt", "w")
  file.write("something")
except  KeyError as error_massage:
  print(f"the key {error_massage} dose not exsist")
else:
  content = file.read()
  print(content)
finally:
  raise TypeError("this is an error that i made up")