from functions import *

def main():
    content = get_json()

    dat = find_last_five(content)
    last_five = show_last_five(dat)
    for i in last_five:
        print(i + '\n')

if __name__ == "__main__":
    main()