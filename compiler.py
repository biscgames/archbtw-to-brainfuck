from sys import argv

def replace_extension_with_bf(string):
    return string.split(".")[0]+".bf"
def compile(archbtw:str,writeto:str|None):
    replace = {
        "i": ">",
        "use": "<",
        "arch": "+",
        "linux": "-",
        "btw": ".",
        "by": ",",
        "the": "[",
        "way": "]",
        "gentoo": "\nINSERT MEMORY DUMP HERE\n"
    }
    result = ""
    with open("compilersource/gentoo.bf","r") as f:
        result = "\n".join(f.readlines())
        f.close()
    result += "\n"
    for command in archbtw.split(" "):
        result += replace.get(command,"")

    f = open(writeto,"w")
    f.write(result)
    f.close()

def main():
    if len(argv) < 2:
        print("usage: python compiler.py [FILE:archbtw] -o [FILE:bf]")
        print("[FILE:archbtw]: the archbtw that will be compiled")
        print("[FILE:bf]: the output, by default it'll have the same filename as the archbtw file, but with .bf instead")
    else:
        with open(argv[1],"r") as f:
            writeto = ""
            if len(argv) > 3:
                writeto = argv[3]
            else:
                writeto = replace_extension_with_bf(argv[1])
            compile(" ".join(f.readlines()),writeto)
            f.close()

if __name__ == "__main__":
    main()
