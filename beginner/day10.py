#Day 10
# Functions with Ouputs


def format_name(f_name, l_name):
  """Formats a name so that it returns the title case version of the name separated by a space."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs"
  return f_name.title() + " " + l_name.title()


result = format_name(input("What is your first name? "),
                     input("What is your last name? "))
print(result)
