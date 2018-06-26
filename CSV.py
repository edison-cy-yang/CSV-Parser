class CSV:

    # def parser(self, file):
    #     result = []
    #     lines = file.split('\n')
    #     for i in range(len(lines)):
    #         result.append([])
    #         fields = lines[i].split(',')
    #         for j in range(len(fields)):
    #             result[i].append(fields[j])
    #
    #     return result

    def parser(self, file):
        quote = '"'
        separator = ','
        result = []
        result.append([])
        curLine = 0
        curField = ""
        inQuotes = False

        for i in range(len(file)):
            if inQuotes:
                "if currently inside a quote (quoted field)"
                if file[i] == quote:
                    inQuotes = False
                else:
                    curField+=file[i]
            else:
                "if not in a quote (quoted field)"
                if file[i] == quote:

                    inQuotes = True
                    if curField != "":
                        curField+='"'

                elif file[i] == separator:
                    "end of field"
                    result[curLine].append(curField)
                    curField = ""

                elif file[i] == '\n':
                    "end of row"
                    result[curLine].append(curField)
                    result.append([])
                    curField = ''
                    curLine += 1

                else:
                    curField += file[i]

        result[curLine].append(curField)
        return result

csv = CSV()

print(csv.parser("a,b,c\nd,e,f"))
# # [['a', 'b', 'c'], ['d', 'e', 'f']]

print(csv.parser("one,\"two wraps,\nonto \"\"two\"\" lines\",three\n4,,6"))
# [["one", "two wraps,\nonto \"two\" lines", "three"], ["4", "", "6"]]

# print(csv.parser("|alternate|\t|\"quote\"|\n\n|character|\t|hint: |||", "\t", "|"))
# # [["alternate", "\"quote\""], [""], ["character", "hint: |"]]

# print(csv.parser("\"dog\",\"cat\",\"uhoh"))

