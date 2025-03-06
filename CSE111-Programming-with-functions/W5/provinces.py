
def main():
    text_list = read_list("provinces.txt")
    print(text_list)

    text_list.pop(0)
    text_list.pop()

    new_list = replace_ab(text_list)
    print(new_list)
    
    alberta_count = new_list.count("Alberta")
    print(f"Alberta occurs {alberta_count} times in the modified list")

def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list;

def replace_ab(list):
    new_list=[]
    for element in list:
        if element == "AB":
            new_list.append("Alberta")
        else:
            new_list.append(element)
    return new_list

main()