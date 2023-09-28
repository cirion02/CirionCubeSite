import GetCubeData
import CardnameToImage


import os.path

CUBE_NAME = "TrolleyCube"


def TestIfAllImagesExist(cubename:str) -> bool:
    result = True

    names = GetCubeData.GetAllCustomImageNames(cubename)

    for name in names:
        path = CardnameToImage.CardnameToPathInternal(name, cubename)

        if not os.path.isfile(path):
            print(f"Card not found: {name} as file {CardnameToImage.CardnameToImage(name)}")
            result = False

    return result


if __name__ == "__main__":
    TestIfAllImagesExist(CUBE_NAME)