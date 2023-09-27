str = input()
start_index = int(input())
end_index = int(input())
substr = str[start_index:end_index+1]
min_replication = (len(str) // len(substr)) + 1
new_string = substr * min_replication
print(new_string)