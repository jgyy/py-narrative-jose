"""
Working with CSV Files
"""
from os.path import join, dirname
from csv import reader, writer

fil = lambda x: join(dirname(__file__), x)


def main():
    """
    main function
    """
    with open(fil("example.csv"), encoding="utf-8") as data:
        csv_data = reader(data)
        data_lines = list(csv_data)
    print(data_lines[:3])
    for line in data_lines[:5]:
        print(line)
    print(len(data_lines))
    all_emails = []
    for line in data_lines[1:15]:
        all_emails.append(line[3])
    print(all_emails)
    full_names = []
    for line in data_lines[1:15]:
        full_names.append(line[1] + " " + line[2])
    print(full_names)
    with open(
        fil("to_save_file.csv"), "w", newline="", encoding="utf-8"
    ) as file_to_output:
        csv_writer = writer(file_to_output, delimiter=",")
        csv_writer.writerow(["a", "b", "c"])
        csv_writer.writerows([["1", "2", "3"], ["4", "5", "6"]])
    with open(
        fil("to_save_file.csv"), "a", newline="", encoding="utf-8"
    ) as file:
        csv_writer = writer(file)
        csv_writer.writerow(['new','new','new'])


if __name__ == "__main__":
    main()
