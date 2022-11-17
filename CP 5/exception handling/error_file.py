import io
file_name = "files.txt"
mode = "w"

try:
    with open(file_name,mode) as fp:
        content = fp.read()
        print(content)

except FileNotFoundError:
    print(f" '{file_name}' not found")

except io.UnsupportedOperation:
    print("Are you sure",file_name,"is readable?")