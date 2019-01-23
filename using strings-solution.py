#Create a function that concatenates strings.

n = ["Michael", "Lieberman"]


def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)
