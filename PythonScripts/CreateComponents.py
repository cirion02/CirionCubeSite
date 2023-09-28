import CardnameToImage

def CreateImageInTable(cardname:str, component:str, cubename:str):
    return component.replace("[CARD_IMAGE]", CardnameToImage.CardnameToLink(cardname, cubename))

def CreateCardTable(cardnames:[str], cubename:str) -> str:
    with open("../BaseHtmlFiles/Components/card-in-table.html", 'r') as file:
        imageComponent = file.read()
    
    contents = "\n".join(map(lambda x: CreateImageInTable(x, imageComponent, cubename), cardnames))

    with open("../BaseHtmlFiles/Components/card-holder.html", 'r') as file:
        return file.read().replace("[CARD_HERE]", contents)