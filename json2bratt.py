import json
import tkinter.filedialog

class json2bratt:
    root = tkinter.Tk()
    infile = tkinter.filedialog.askopenfilename(initialdir=["../Data"], filetypes=[("json files", "*.json *.jsonl")])
    root.destroy()

    with open(infile) as f:
        data = json.load(f)

    outfile = input("Name your ann file: ") + ".ann"
    data2 = data['sentences'].keys()
    counter = 0
    tindx = 0
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
    for x in data2:
        i = 1
        while i <= len(data['sentences'][x]):
            entity = data['sentences'][x]['entity ' + str(i)]

            irr = str(entity).split(" ")
            startnum = int(irr[1].replace(",", "")) + counter
            endnum = int(irr[3].replace(",", "")) + counter
            keyterm = irr[5].replace("'", "").replace("}", "")
            keyterm_long = keyterm_dict.get(keyterm, None)
            substring = x[int(irr[1].replace(",", "")): int(irr[3].replace(",", ""))]
            #print(str(startnum) + " " + str(endnum) + " " + " " + sentence)
            t_entry = f"t{tindx}\t{keyterm_long} {startnum} {endnum}\t{substring}"
            with open(outfile, "a") as f:
                f.write(t_entry)
                f.write("\n")

            tindx += 1
            counter += len(x)
            i += 1
