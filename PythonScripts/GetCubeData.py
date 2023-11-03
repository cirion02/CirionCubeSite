import csv
from os import listdir

def CubenameToRelativePath(cubename:str) -> str:
      return f"../CubeArtisanDownloads/{cubename}/{cubename}"

def CubenameToCsvPath(cubename:str) -> str:
      return CubenameToRelativePath(cubename) + ".csv"

def CubenameToNamesPath(cubename:str) -> str:
      return CubenameToRelativePath(cubename) + ".txt"

def GetAllCustomImageNames(cubename:str, useCsv=False) -> [str]:
    if useCsv:
        result = []
        with open(CubenameToCsvPath(cubename), encoding="utf8") as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            with open(CubenameToNamesPath(cubename)) as names:
                for card, name in zip(reader, [""] + names.readlines()):
                    if card[0] == "Name":
                        continue
                    if "Paper Only" in card[13].split(";"):
                        continue

                    name = name.strip()

                    if card[11] != "": #Custom Image
                        result.append(name)
        return result
    
    files = [f[:-4] for f in listdir(f"../ImageFiles/{cubename}")]

    return files

if __name__ == "__main__":
     print(GetAllCustomImageNames("TrolleyCube"))