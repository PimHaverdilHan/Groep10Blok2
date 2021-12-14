from tkinter import filedialog as fd
import pandas as pd
from openpyxl import load_workbook

def read_file():
    file = fd.askopenfilename()
    df = pd.read_excel(file)
    filtered_df = df[df["variation reads"]>5 & df["Gene component"]=="EXON_REGION"]
    book = load_workbook(file)
    writer = pd.ExcelWriter(file, engine="openpyxl")
    writer.book = book
    filtered_df.to_excel(writer, sheet_name="sheet2")
    writer.save()
    writer.close()

if "__main__" == __name__:
    print("start")
    read_file()