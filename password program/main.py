from sqlalchemy import true
print("hello, $this is the program which store password which you all store")
inputpassword = input("enter your password:")
f = open(f"password.txt", 'a')
f.write(f"{inputpassword}\n")
f.close()
seepassword = input("do you want to see password you saved previous y/n:")
if seepassword == "y" or seepassword == "Y":
    seelinepassword = int(input("enter:"))
    file_path = "password.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_number = seelinepassword
        selected_line = lines[line_number - 1]
        print("The selected line is:", selected_line)
        file.close()
else: print("ok")
