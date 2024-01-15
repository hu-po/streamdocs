import os

def rename_files():
    directory = os.listdir("./")
    for file in directory:
        if file.endswith(".md") and file.count(".") == 3:
            names = file.split(".")
            new_name = names[2] + "." + names[1] + "." + names[0] + "." + names[3]
            os.rename(file, new_name)
            print(new_name)

if __name__ == "__main__":
    rename_files()
