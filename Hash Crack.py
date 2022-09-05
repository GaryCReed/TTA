# Task 6
from cyber_tools import get_hashed_password, hashes_match, get_popular_passwords_from_file

popular_passwords_list = []
count = 0
get_popular_passwords_from_file("passwords-top-1000.txt", popular_passwords_list)


with open("leaked-data-100.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        username, pw = line.split(" ")
        for popular_password in popular_passwords_list:
            result = get_hashed_password(popular_password, "md5")
            if hashes_match(result, pw):
                print(username + " is using a popular password! --> " + popular_password)
                count = count + 1

print("Finished processing file.")
print(str(count) + " passwords cracked!")
