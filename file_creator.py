import os
def file_creator(company_name, date):
    folder_name = str(company_name + "-" + date)
    read_files = os.listdir(folder_name + "/")
    output_file_name = company_name + "_out.txt"
    with open(output_file_name, "w") as outfile:
        for f in read_files:
            if f.endswith(".txt"):
                with open(folder_name + "/" + f, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("PARA:ID")
    return output_file_name



