#For calculationg the tuple size, we can use len() function with syntax as follows
#Having User input for tuple 
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(len(integer_list));
