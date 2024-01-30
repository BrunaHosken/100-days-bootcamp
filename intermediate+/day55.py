inputs = eval(input())

def logging_decorator(function):
  def wrapper(*args):
    function_called = f"You called {function.__name__}{args}"
    print(function_called)
    result = function(args[0], args[1], args[2])
    print(f"It returned: {result}")
    
  return wrapper


@logging_decorator
def a_function(a, b, c):
  return a * b * c