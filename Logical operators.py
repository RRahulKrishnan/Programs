x, y, z = 2, 10, 7

print(x < y and y < z)  # Should print False since y is not less than z
print(x < y or y < z)  # Should print True since x is less than y
print(not x < y)  # Should print False since x < y is True and opposite of it is False.
print (x < y and not y < z)  # Should print true since x < y and y >= z
# These operators play a complementary role
print(x+y < z*2 and x*z <= y**5)
