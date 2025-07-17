

# Complete the solve function below.
def solve(s):
    sentence = s.split(" ") # not specifying delimeter removes all whitespcaes (tabs or strings)
    result = [ word.capitalize() for word in sentence ]

    return ' '.join(result)



