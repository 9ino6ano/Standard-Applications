from zipfile import ZipFile

file=input("Enter path of zip file: ")#ensure you include a zip file path

with ZipFile(file,"r") as zip:
    zip.printdir()
    zip.extractall()
    print("Unzipped file complete.")

