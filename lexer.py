import re

class Lexer:
    def reader(self):
        f = open("main.hy", "r")
        return f.read()

    def lexical_analyzer(self):
        keyword = ["num", "str", "bool", "prnt"]
        operator = ["(", ")", "{", "}", ",", "'", "=", ".", "<", ">"]
        identifier = []

        build = []

        var_read = False
        variable = ""

        lex = Lexer()
        content = lex.reader().replace(" ", "")

        for keyw in range(len(keyword)):
            for item in re.finditer(keyword[keyw], content):

                insert = {
                    "token": "keyword",
                    "keyword": keyword[keyw],
                    "start_pos": item.start(),
                    "end_pos": item.end()
                }

                build.append(insert)

        for opr in range(len(operator)):
            for item in range(len(content)):
                if content[item] == operator[opr]:

                    insert = {
                        "token": "operator",
                        "keyword": operator[opr],
                        "start_pos": item,
                        "end_pos": item
                    }

                    build.append(insert)

        for i in range(len(build) - 1):
            for j in range(0, len(build) - i - 1):
                if build[j].get("start_pos") > build[j + 1].get("start_pos"):
                    build[j], build[j + 1] = build[j + 1], build[j]

        for i in range(len(build)):
            print(build[i].get("start_pos"), build[i].get("end_pos"))

        return build

    def send_build(self):
        lex = Lexer()
        build = lex.lexical_analyzer()
        return build


lex = Lexer()
build = lex.lexical_analyzer()