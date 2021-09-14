from tkinter.filedialog import askopenfilename, asksaveasfilename

gb = "none"
fasta = "none"

def openGBfile():
    """functions use to open a file and read it"""
    
    global gb
    try:
        path = askopenfilename()
        with open(path, "r") as gbfile:
            gb = gbfile.read()
        print("\n file succesfuly loaded \n")
    
    except:
        pass

def gb2fasta(gb):
    """function use to convert the Genbank file to fasta

    the content of the genbank file is transform and 
    use to "construct" the fasta file with it head and
    it sequence with line of 80 nucleotides. it only compute
    nucleotidic sequence.
    """
    global fasta
    spliting = gb.split("        1 ")
    
    try:
        gb = spliting[1]
    except:
        raise Exception("error no file loaded or file format is not right")

    rawseq = ""
    
    for i in range(0,len(gb)):
        if gb[i] == "a" or gb[i] == "t" or gb[i] == "g" or gb[i] == "c":
            rawseq = rawseq + gb[i]

    rawseq = rawseq.upper()
    a = 0
    seq80 = ""
    
    for j in range(0,len(rawseq)):
        try:
            if a < 80:
                seq80 = seq80 + rawseq[j]
                a += 1
            else:
                seq80 = seq80 + "\n"
                a = 0
        except:
            break

    rawseq = seq80

    version = spliting[0].split("VERSION     ")
    version = version[1].split("DBLINK")
    version = version[0]
    version = version.rstrip()

    definition = spliting[0].split("DEFINITION  ")
    definition = definition[1].split("ACCESSION")
    definition = definition[0]
    definition = definition.rstrip()

    header = ">" + version + " " + definition

    fasta = header + "\n" + rawseq
    print("\n done converting to full genome sequence \n")

def savefile():
    """function use to save the converted fasta file"""

    global fasta
    if fasta != "none":
        save = asksaveasfilename()
        save = open(save, "a")
        save.write(fasta)
        save.close()
        fasta = ""
    
    else:
        print("\n there is no converted file to save \n")