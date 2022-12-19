from lexer import Lexer

class Parser:
    def parse_build(self):
        lex = Lexer()
        build = lex.send_build()

        parsed = ""

        for i in range(len(build)):
            if build[i].get("keyword") == "num":
                parsed += f"int({build[i + 4].get('keyword')}) "

            elif build[i].get("keyword") == "str":
                parsed += f"str({build[i + 4].get('keyword')}) "

            elif build[i].get("keyword") == "prnt":
                parsed += f"print({build[i + 2].get('keyword')}) "


        print(parsed)





par = Parser()
par.parse_build()