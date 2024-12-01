# Sample list containing mixed types
my_list = [20, "hi", 3, "guvi", 5.5, "python"]

# Lambda function to check if an element is an integer or a string
check_type = lambda x: 'integer' if isinstance(x, int) else 'string' if isinstance(x, str) else 'other'

# Apply the lambda function to each element in the list
result = list(map(check_type, my_list))

# Output the result
print(result)
