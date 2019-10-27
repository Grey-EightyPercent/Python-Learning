str = "this is string example...wow!!!"
str = str.encode('utf-16', 'strict')

print(f"Encoded String: {str}")
print(f"Decoded String: {str.decode('utf-16', 'strict')}")

test_b = open("test.txt", encoding = "utf-8")
test_b_read = test_b.read ()

print(f"This is 1: {test_b}.\nThis is 2: {test_b_read}")
