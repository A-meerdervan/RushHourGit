
import time
from datetime import date

def convertfile():
    import csv
    # open de file en schrijf de juiste waarde over naar een csv bestand
    with open( 'KNMI_19970101.csv','rb' ) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        with open('converted.csv','wb') as writefile:
            i = 0
            for row in spamreader:
                if i < 13:
                    i += 1
                    continue

                date = row[1]
                row = date +','+ row[2].strip()
                writefile.write(row+'\n')

if __name__ == '__main__':
    convertfile()
