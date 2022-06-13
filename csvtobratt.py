# https://old.reddit.com/r/learnpython/comments/v8lio5/how_to_read_data_from_csv_and_use_it_to_convert/

import os.path

import pandas as pd
import requests
import sys
import tkinter.filedialog
import math

root = tkinter.Tk()
csv_filename = tkinter.filedialog.askopenfilename(filetypes=[('csv files', '*.csv')])
root.destroy()
ann_file_url = input("\nName you output ann file: ") + ".ann"
if os.path.exists(ann_file_url):
    os.remove(ann_file_url)

keyterm_dict = {
    "ALAS": "varietal alias",
    "CROP": "crop",
    "CVAR": "crop_variety",
    "JRNL": "journal reference",
    "PATH": "pathogen",
    "PED": "pedigree",
    "PLAN": "plant anatomy",
    "PPTD": "plant predisposition to disease",
    "TRAT": "trait",
    # not complete for given CSV!
}

csv = None
try:
    with open(csv_filename, "r") as f:
        csv = f.readlines()
    print(f"Loaded CSV from disk {csv_filename}")
except:
    raise ValueError("File does not exist")

if not csv:
    print(f"Couldn't load CSV")
    sys.exit(0)

df = pd.read_csv(csv_filename)

for row in df.itertuples(name='Row'):
    #print(f"\nRow #{row.Index}")
    # print("\t", row.Sentences)
    # print("\t", "\t".join([str(e) for e in row[2:]]))

    for t_idx, entity in enumerate(row[2:]): # I assume t_idx resets for each row in CSV

        if pd.isna(entity):
            break
        start, end, keyterm = entity.split(" ")
        keyterm = keyterm.replace("'", "")
        # print(f"{entity} \t->\t start={start} end={end} keyterm={keyterm}")

        keyterm_long = keyterm_dict.get(keyterm, None)
        if keyterm_long:
            actual_word = row.sentences[int(start):int(end)]
            t_entry = f"T{t_idx}\t{keyterm_long} {start} {end} {actual_word}"
            #print(t_entry)
            with open(ann_file_url, "a") as f:
                f.write(t_entry)
                f.write("\n")

        else:
            #print(f"Unknown keyterm {keyterm}")
            with open(ann_file_url, "a") as f:
                f.write(f"Unknown keyterm {keyterm}")
                f.write("\n")