import os, shutil, sys
class CREAT_ACHTECTUR(object):
    """
    docstring
    """

    def CreatFlutterAApp(self, foldeName) :
        projectWorkingDirectory = os.getcwd()
        if not (os.path.exists(f"{foldeName}")) :
            os.mkdir(f"{foldeName}")
        os.chdir(f"./{foldeName}")
        listFolde = list([
            "presentation",
            [
                "widget",
                "pages",
                "bloc",
            ],
            "domain",
            [
                "entiters",
                "repositories",
                "userCase",
            ],
            "data",
            [
                "dataResources",
                "models",
                "repositorie",
            ],
        ])
        for i in range(0, len(listFolde), 2) :
            current = os.getcwd()
            if not (os.path.exists(f"./{listFolde[i]}")) :
                os.mkdir(f"./{listFolde[i]}")
            os.chdir(f"./{listFolde[i]}")
            for fold in listFolde[i+1] :
                if not (os.path.exists(f"./{fold}")) :
                    os.mkdir(f"./{fold}")
            os.chdir(current)
        os.chdir(f"./{listFolde[0]}/{listFolde[1][1]}")
        with open("home.dart", "a") : pass
        os.chdir(str(projectWorkingDirectory))

    
    def CreatNodeMVCAPI(self, name) :
        pass
    
    def deletAchitecture(self, foldeName) :
        listDir = list(os.listdir(foldeName))
        if len(listDir) > 0 :
            for dirElement in listDir :
                if not os.path.isdir(f"./{foldeName}/{dirElement}") :
                    os.remove(f"./{foldeName}/{dirElement}")
                elif len(list(os.listdir(f"./{foldeName}/{dirElement}"))) > 0 :
                    self.deletAchitecture(f"./{foldeName}/{dirElement}")
                else :
                    shutil.rmtree(f"./{foldeName}/{dirElement}")
        shutil.rmtree(f"./{foldeName}")