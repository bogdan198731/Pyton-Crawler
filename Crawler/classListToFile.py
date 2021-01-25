from produs import *
from general import *


def str_class_list_to_file(prod, nume_obiect, file_path):
    delete_file_content('test1.py')
    create_data_files(file_path, 0)
    create_data_files('test1.py', 'from Crawler import *')
    append_to_file('test1.py', "from general import *")
    append_to_file('test1.py', "def write(prod):")
    append_to_file('test1.py', "    string1 = ''")
    string1 = ""
    for item in prod.__dict__.keys():
        string = str("    string = str('<" + nume_obiect + "." + item + ">  {' " + " + str(" + nume_obiect + "." + item + ") + '}')")

#        string = str("    print('" + nume_obiect + "." + item+"'" + " + str(" + nume_obiect + "." + item + "))")
#        print(string)
        append_to_file('test1.py', string)
        string = str("    print(string)")
        string = str("    append_to_file("'"' + file_path + '"'", string)")
#        print(string)
        append_to_file('test1.py', string)
        string = str("    string1 = string1 + string ")
        append_to_file('test1.py', string)
    os.system("test2.py 1")
    print("s-a lansat test2")
    delete_file_content("test1.py")
    create_data_files('test1.py', 'from general import *')
    append_to_file('test1.py', "def write(prod):")
    append_to_file('test1.py', "    string1 = ''")


print("classListToFile3")



string = """
def patrat(nr):
    return nr*nr


numar=int(input('numar : '))

num = patrat(numar)
print(num)

"""