
def remove_blank_lines(path):
    formatted_contents = []
    file = open(path)
    file_contents = file.read().splitlines()

    for line in file_contents:
        if line != "":
            formatted_contents.append(line)

    return formatted_contents

def copy_string_to_file(string, path):
    file = open(path, "w")
    file.write(string)


def write_array_to_file(array, path):
    file = open(path, "w")
    for element in array:
        file.write(element)
        file.write("\n")

def clean_file(path):
    cleaned_contents = remove_blank_lines(path)
    write_array_to_file(cleaned_contents, path)

def copy_file_to_array(path):
    file = open(path)
    file_contents = file.read().splitlines()
    return file_contents

def wipe_file(path):
    file = open(path, "w")
    file.write("")



if __name__ == "__main__":
    formatted_contents = remove_blank_lines("TextFiles/codes.txt")
    write_array_to_file(formatted_contents, "TextFiles/io_test.txt")
