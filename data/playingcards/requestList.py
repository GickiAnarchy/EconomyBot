import io
import os
import urllib.request

pathHere = os.path.abspath(os.path.dirname(__file__))
txtOne = f"{pathHere}\curlList.txt"
listOne = []

def stepOne():
    with open(txtOne) as f:
        for line in f.readlines():
            listOne.append(line)
            print(f"\n{line} is done.")


def stepTwo():
    amount = len(listOne)

    while True:
        newfilename = f"/html/ile{str(amount)}.html"
        webUrl = urllib.request.urlopen(listOne.pop())
        with open(newfilename, "wb") as nf:
            data = webUrl.read()
            nf.write(data)
            nf.close()
        print(f"File #{str(amount)} done.")
        amount -= 1
        if amount <= 0:
            break
    print("\nI\nAm\nDone\nWith\nThe\nList\n##################################")


stepOne()

stepTwo()