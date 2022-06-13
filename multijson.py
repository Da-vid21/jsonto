import pandas as pd
import os
import json


def final(location):
    path_to_json = location
    infiles = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    infiles.sort()
    print("\nThese are your json data inputs", infiles)
    if __name__ == "__main__":
        outfile = input("\nName your output file: ") + '.csv'
    else:
        outfile = "multijson.csv"
    if os.path.exists(outfile):
        os.remove(outfile)

    def output():
        return outfile
    conversion(infiles, location, outfile)
    output()

def conversion(files, location, output):
    for i in files:
        def js_r(data):
            with open(location + "/" + data) as f_in:
                return json.load(f_in)
        try:
            my_dic_data = js_r(i)
            #print("\nThis is my dictionary", my_dic_data)
            keys = my_dic_data.keys()
            # print("\nThe original dict keys", keys)
            # You assign a new dictionary key- SO_users, and make dictionary comprehension = { your_key: old_dict[your_key] for your_key in your_keys }
            dict_you_want = {'sentences': my_dic_data['sentences'] for key in keys}

            # print("\nThese are the keys to ", dict_you_want.keys())

            df = pd.DataFrame(dict_you_want)

            # When .apply(pd.Series) method on items column is applied, the dictionaries in items column will be used as column headings
            df2 = df['sentences'].apply(pd.Series)
            df2.to_csv(output, mode='a', header=not os.path.exists(output))

        except:
            print("\n" + i + "file is not formatted correctly so it is skipped")

    removewords(output)

def removewords(output):
    #Deleting start, end and label
    text = open(output, "r")
    text = ''.join([i for i in text]) \
        .replace("{'start': ", "") \
        .replace(", 'end': ", " ") \
        .replace(", 'label': ", " ") \
        .replace("}", "") \
        .replace(",entity 1", "sentences,entity 1", 1)


    x = open(output, "w")
    x.writelines(text)
    x.close()
    print("\nFile has been successfully converted to csv")

