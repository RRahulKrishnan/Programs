x, y, z = 2, 10, 7

print(x < y and y < z)  # Should print False since y is not less than z
print(x < y or y < z)  # Should print True since x is less than y
# These operators play a complementary role
print(x+y < z*2 and x*z <= y**5)
