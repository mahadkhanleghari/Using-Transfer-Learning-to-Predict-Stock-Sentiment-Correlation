import glob

read_files = glob.glob("*.txt")

with open("test_neg.txt", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write(infile.read())
            outfile.write("PARA:ID")

