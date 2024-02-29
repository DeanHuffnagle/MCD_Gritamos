import file_io as io

CODE_PATH="TextFiles/codes.txt"
NEW_CODE_PATH="TextFiles/newCodes.txt"

def expand_codes(path):
    io.clean_file(path)
    array = io.copy_file_to_array(path)
    expanded_array = []
    for i in array:
        print(i)
        num = 0
        while num <= 9:
            code = f"{i[:-1]}{num}"
            num+=1
            expanded_array.append(code)
    return expanded_array


def add_new_codes():
    io.clean_file(NEW_CODE_PATH)
    expanded_new_codes = expand_codes(NEW_CODE_PATH)
    current_codes = io.copy_file_to_array(CODE_PATH)
    for i in expanded_new_codes:
        current_codes.append(i)
    io.write_array_to_file(current_codes, CODE_PATH)
    io.wipe_file(NEW_CODE_PATH)

def zipper_codes():
    zipped_array = []
    array = io.copy_file_to_array(CODE_PATH)
    array.sort()

    index = 0
    while len(array) > 0:
        leftValue = array.pop(0)
        zipped_array.append(leftValue)
        try:
            rightValue = array.pop(len(array)-1)
            zipped_array.append(rightValue)
        except:
            continue
    return zipped_array



if __name__ == "__main__":
    add_new_codes()
    io.write_array_to_file(zipper_codes(), CODE_PATH)