import glob
import sys
import pandas as pd
import json
import os
import tkinter.filedialog
import json
import multijson

print()
fileoption = input("Do you want to select a file or a folder? *file or *dir(folder): ")



def jsontocsvfile(data, outfile):
    def js_r(data):
        with open(data) as f_in:
            return json.load(f_in)

    my_dic_data = js_r(data)
    ### print("\nThis is my dictionary", my_dic_data)
    keys = my_dic_data.keys()
    #print("\nThe original dict keys", keys)
    # You assign a new dictionary key- SO_users, and make dictionary comprehension = { your_key: old_dict[your_key] for your_key in your_keys }
    dict_you_want = {'sentences': my_dic_data['sentences'] for key in keys}

    #print("\nThese are the keys to ", dict_you_want.keys())

    df = pd.DataFrame(dict_you_want)

    # When .apply(pd.Series) method on items column is applied, the dictionaries in items column will be used as column headings
    df2 = df['sentences'].apply(pd.Series)

    df2.to_csv(outfile, sep=',', encoding='utf-8')
    return outfile


if fileoption.lower() == 'dir' or fileoption.lower() == 'folder':

    root = tkinter.Tk()
    infile = tkinter.filedialog.askdirectory(initialdir=[("../Data")])
    root.destroy()

    data = multijson.final(infile)

elif fileoption.lower() == 'file' or 'f':
    root = tkinter.Tk()
    infile = tkinter.filedialog.askopenfilename(initialdir=["../Data"], filetypes=[('json file', '*.json *.jsonl')])
    root.destroy()
    data = infile

    print("\nThis is json data input", data)
    outfile = input("\nName your output file: ") + '.csv'
    jsontocsvfile(data, outfile)
    multijson.removewords(outfile)

# JsontoCSV for a single file ends here




else:
    raise ValueError("Invalid Argument")


