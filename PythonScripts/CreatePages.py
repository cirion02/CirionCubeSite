import CreateComponents
import GetCubeData

def StitchFilesTogether(filenames:[str]) -> str:
    text = []
    for filename in filenames:
        with open("../BaseHtmlFiles/" + filename + ".html", 'r') as file:
            text.append(file.read())
    return "\n".join(text)

def CreateIndexPage():
    text = StitchFilesTogether(["head-start", "head-to-body", "navbar", "home-content", "body-end"])
    with open("../index.html", 'w') as file:
        file.write(text)

def CreateCubeCustomImageGallery(cubename:str):
    text1 = StitchFilesTogether(["head-start", "head-to-body", "navbar"])

    text2 = CreateComponents.CreateCardTable(sorted(GetCubeData.GetAllCustomImageNames(cubename), key=lambda x : x.lower()), cubename)

    text3 = StitchFilesTogether(["body-end"])

    with open("../trolley-images.html", 'w') as file:
        file.write("\n".join([text1, text2, text3]))
    
if __name__ == "__main__":
    CreateIndexPage()
    CreateCubeCustomImageGallery("TrolleyCube")