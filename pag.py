if __name__ == '__main__':
    import sys, argparse, os, time
    from Function.FunctionPackage import CREAT_ACHTECTUR

    creatAchitecture = CREAT_ACHTECTUR()

    flutter_Achiterture = str("""
        .
        |___ src/
             |--- presentation/
             |    |--- widgets/
             |    |--- pages/
             |    |    |___ home.dart
             |    |___ bloc/
             |--- domain/
             |    |--- entiters/
             |    |--- repositories/
             |    |___ userCase/
             |___ data/
                  |--- dataResources/
                  |--- models/
                  |___ repositories/
    """)

    node_mvc_Achiterture = str("""
        .
        |--- app.js
        |--- .env
        |--- api/
        |    |__ Auth/
        |        |--- AuhtService.js
        |        |___ Router.js
        |--- config/
        |    |___ index.js
        |--- services/
        |    |___ index.js
        |--- models/
        |    |___ Users.js
        |--- scripts/
        |--- subscribers/
        |___ test/
    """)


    parser = argparse.ArgumentParser()
    parser.add_argument("--creat-node-mvc-api", type=str, help="created a mvc node Api")
    parser.add_argument("--creat-flutter-app", type=str, help="created a achitectur of project flutter")
    parser.add_argument("--delet", help="deleted achitectur")
    parser.add_argument("--log", default=sys.stdout, type=argparse.FileType('w'), help='the file where the sum should be written')
    args = parser.parse_args()
    if (args.creat_node_mvc_api != None) :
        args.log.write("creating node mvc api ... ")
        args.log.write(node_mvc_Achiterture)
    elif (args.creat_flutter_app != None) :
        args.log.write("creating flutter app ... ")
        time.sleep(2)
        creatAchitecture.CreatFlutterAApp(args.creat_flutter_app)
        time.sleep(2)
        args.log.write(flutter_Achiterture)
    elif (args.delet != None) :
        args.log.write("delet achitecture ... ")
        time.sleep(2)
        creatAchitecture.deletAchitecture(args.delet)
        time.sleep(2)
    else :
        args.log.write("ERROR : not argument is call")
    args.log.close()