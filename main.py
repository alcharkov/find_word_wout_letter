import random

def main():
    table = []
    lines = open("lithuanian-words-list-without-names.txt", "r").readlines()
    while True:
        random.shuffle(lines)
        char = input("Press letter:")
        for line in lines:
            if line in table:
                break
            elif char not in line:
                table.append(line)
                print("Word: ", line)
                break
if __name__ == "__main__":
    main()