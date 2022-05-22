from enum import Enum, auto
class TypeToken(Enum):
    # Identifiers
    TK_IDENTIFIER = auto(),
    TK_INTEGER = auto(),
    TK_FLOATINGPOINT = auto(),
    TK_CHARLITERAL = auto(),
    TK_STRINGLITERAL = auto(),
    # -------------------Operators-------------------
    # Arithmetic
    TK_OPSUM = auto()
    TK_OPSUB = auto()
    TK_OPMULT = auto()
    TK_OPDIV = auto()
    TK_OPMOD = auto()
    TK_OPINC = auto()
    TK_OPDEC = auto()
    # Relational
    TK_OPEQ = auto()
    TK_OPNEQ = auto()
    TK_OPLT = auto()
    TK_OPGT = auto()
    TK_OPGTEQ = auto()
    TK_OPLTEQ = auto()
    # Logical
    TK_OPAND = auto()
    TK_OPOR = auto()
    TK_OPNEGATION = auto()
    # Assignment
    TK_OPASSIGNMENT = auto()
    TK_OPASUM = auto()
    TK_OPASUB = auto()
    TK_OPAMULT = auto()
    TK_OPADIV = auto()
    TK_OPAMOD = auto()
    TK_OPALEFTSHIFT = auto()
    TK_OPARIGHTSHIFT = auto()
    TK_OPABITAND = auto()
    TK_OPABITOR = auto()
    TK_OPABITXOR = auto()
    # BITWISE
    TK_OPBITAND = auto()
    TK_OPBITOR = auto()
    TK_OPBITXOR = auto()
    TK_OPBITCOMP = auto()
    TK_OPBITLEFTSHIFT = auto()
    TK_OPBITRIGHTSHIFT = auto()
    # MISC 
    TK_OPTERNARYIF = auto()
    TK_OPTERNARYELSE = auto()
    TK_OPEOL = auto()
    TK_OPHEAD = auto()
    TK_OPDOT = auto()
    TK_OPARROW = auto()
    TK_OPCOMMENT = auto()
    TK_OPCOMMENTBLOCK = auto()
    # Delimiters
    TK_PARENTHESESOPEN = auto()
    TK_PARENTHESESCLOSE = auto()
    TK_BRACKETSOPEN = auto()
    TK_BRACKETSCLOSE = auto()
    TK_BRACESOPEN = auto()
    TK_BRACESCLOSE = auto()
    # keywords
    TK_KWAUTO = auto()
    TK_KWELSE = auto()
    TK_KWLONG = auto()
    TK_KWSWITCH = auto()
    TK_KWBREAK = auto()
    TK_KWENUM = auto()
    TK_KWREGISTER = auto()
    TK_KWTYPEDEF = auto()
    TK_KWCASE = auto()
    TK_KWEXTERN = auto()
    TK_KWRETURN = auto()
    TK_KWUNION = auto()
    TK_KWCHAR = auto()
    TK_KWFLOAT = auto()
    TK_KWSHORT = auto()
    TK_KWUNSIGNED = auto()
    TK_KWCONST = auto()
    TK_KWFOR = auto()
    TK_KWSIGNED = auto()
    TK_KWVOID = auto()
    TK_KWCONTINUE = auto()
    TK_KWGOTO = auto()
    TK_KWSIZEOF = auto()
    TK_KWVOLATILE = auto()
    TK_KWDEFAULT = auto()
    TK_KWIF = auto()
    TK_KWSTATIC = auto()
    TK_KWWHILE = auto()
    TK_KWDO = auto()
    TK_KWINT = auto()
    TK_KWSTRUCT = auto()
    TK_KW_PACKED = auto()
    TK_KWDOUBLE = auto()

    
_listAlphabet="(\w|\d|-|+|*|\/|\\|\||&|\.|)"



_tableOfTypes={
    "^[a-zA-Z\_][a-zA-Z0-9\_]*[^a-zA-Z0-9]":TypeToken.TK_IDENTIFIER,
    "^\d+\D":TypeToken.TK_INTEGER,
    "^\d+\.\d+\D":TypeToken.TK_FLOATINGPOINT,
    "^\'.*\'(.|\n)":TypeToken.TK_CHARLITERAL,
    "^\".*\"(.|\n)":TypeToken.TK_STRINGLITERAL,
    "^\+[^\+=]":TypeToken.TK_OPSUM,
    "^-[^-=>]":TypeToken.TK_OPSUB,
    "^\*[^\*=]":TypeToken.TK_OPMULT,
    "^\/[^\/=]":TypeToken.TK_OPDIV,
    "^%[^%=]":TypeToken.TK_OPMOD,
    "^\+\+(.|\n)":TypeToken.TK_OPINC,
    "^--(.|\n)":TypeToken.TK_OPDEC,
    "^==(.|\n)":TypeToken.TK_OPEQ,
    "^!=(.|\n)":TypeToken.TK_OPNEQ,
    "^<[^=]":TypeToken.TK_OPLT,
    "^>[^=]":TypeToken.TK_OPGT,
    "^>=(.|\n)":TypeToken.TK_OPGTEQ,
    "^<=(.|\n)":TypeToken.TK_OPLTEQ,
    "^&&(.|\n)":TypeToken.TK_OPAND,
    "^\|\|(.|\n)":TypeToken.TK_OPOR,
    "^![^=]":TypeToken.TK_OPNEGATION,
    "^=[^=]":TypeToken.TK_OPASSIGNMENT,
    "^\+=(.|\n)":TypeToken.TK_OPASUM,
    "^-=(.|\n)":TypeToken.TK_OPASUB,
    "^\*=(.|\n)":TypeToken.TK_OPAMULT,
    "^\/=(.|\n)":TypeToken.TK_OPADIV,
    "^%=(.|\n)":TypeToken.TK_OPAMOD,
    "^<<=(.|\n)":TypeToken.TK_OPALEFTSHIFT,
    "^>>=(.|\n)":TypeToken.TK_OPARIGHTSHIFT,
    "^&=(.|\n)":TypeToken.TK_OPABITAND,
    "^\|=(.|\n)":TypeToken.TK_OPABITOR,
    "^\^=(.|\n)":TypeToken.TK_OPABITXOR,
    "^&[^&=]":TypeToken.TK_OPBITAND,
    "^\^[^=]":TypeToken.TK_OPBITOR,
    "^\^[^=]":TypeToken.TK_OPBITXOR,
    "^~(.|\n)":TypeToken.TK_OPBITCOMP,
    "^<<[^=]":TypeToken.TK_OPBITLEFTSHIFT,
    "^>>[^=]":TypeToken.TK_OPBITRIGHTSHIFT,
    "^\?(.|\n)":TypeToken.TK_OPTERNARYIF,
    "^:(.|\n)":TypeToken.TK_OPTERNARYELSE,
    "^\((.|\n)":TypeToken.TK_PARENTHESESOPEN,
    "^\)(.|\n)":TypeToken.TK_PARENTHESESCLOSE,
    "^\[(.|\n)":TypeToken.TK_BRACKETSOPEN,
    "^\](.|\n)":TypeToken.TK_BRACKETSCLOSE,
    "^{(.|\n)":TypeToken.TK_BRACESOPEN,
    "^}(.|\n)":TypeToken.TK_BRACESCLOSE,
    "^;(.|\n)":TypeToken.TK_OPEOL,
    "^#.":TypeToken.TK_OPHEAD,
    "^\..":TypeToken.TK_OPDOT,
    "^\/\/.*\n":TypeToken.TK_OPCOMMENT,
    # "^\/\*(.|\s)*(\*\/|[^\w])":TypeToken.TK_OPCOMMENTBLOCK,
    "^->.":TypeToken.TK_OPARROW
}
    
_keyWordsTable={
    "auto":TypeToken.TK_KWAUTO,
    "else":TypeToken.TK_KWELSE,
    "long":TypeToken.TK_KWLONG,
    "switch":TypeToken.TK_KWSWITCH,
    "break":TypeToken.TK_KWBREAK,
    "enum":TypeToken.TK_KWENUM,
    "register":TypeToken.TK_KWREGISTER,
    "typedef":TypeToken.TK_KWTYPEDEF,
    "case":TypeToken.TK_KWCASE,
    "extern":TypeToken.TK_KWEXTERN,
    "return":TypeToken.TK_KWRETURN,
    "union":TypeToken.TK_KWUNION,
    "char":TypeToken.TK_KWCHAR,
    "float":TypeToken.TK_KWFLOAT,
    "short":TypeToken.TK_KWSHORT,
    "unsigned":TypeToken.TK_KWUNSIGNED,
    "const":TypeToken.TK_KWCONST,
    "for":TypeToken.TK_KWFOR,
    "signed":TypeToken.TK_KWSIGNED,
    "void":TypeToken.TK_KWVOID,
    "continue":TypeToken.TK_KWCONTINUE,
    "goto":TypeToken.TK_KWGOTO,
    "sizeof":TypeToken.TK_KWSIZEOF,
    "volatile":TypeToken.TK_KWVOLATILE,
    "default":TypeToken.TK_KWDEFAULT,
    "if":TypeToken.TK_KWIF,
    "static":TypeToken.TK_KWSTATIC,
    "while":TypeToken.TK_KWWHILE,
    "do":TypeToken.TK_KWDO,
    "int":TypeToken.TK_KWINT,
    "struct":TypeToken.TK_KWSTRUCT,
    "_Packed":TypeToken.TK_KW_PACKED,
    "double":TypeToken.TK_KWDOUBLE,
}

_sintaxGraph={
    TK_OPHEAD:[TK_IDENTIFIER],
    TK_KWUNION:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWCHAR:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWFLOAT:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWSHORT:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWINT:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWDOUBLE:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWENUM:[TK_IDENTIFIER,TK_OPMULT],
    TK_KWLONG:[TK_IDENTIFIER,TK_OPMULT],

    TK_KWSIGNED:[TK_KWSHORT,TK_KWINT,TK_KWCHAR],
    TK_KWUNSIGNED:[TK_KWSHORT,TK_KWINT,TK_KWCHAR],
    K_KWCONST:[TK_KWCHAR,TK_KWFLOAT,TK_KWSHORT,TK_KWINT,TK_KWDOUBLE,TK_KWENUM,TK_KWLONG,TK_KWSIGNED,TK_KWUNSIGNED],
    
    TK_IDENTIFIER:[TK_PARENTHESESOPEN,TK_BRACKETSOPEN,TK_OPARROW,TK_OPDOT,TK_OPEOL,TK_OPTERNARYIF,TK_OPTERNARYELSE,TK_OPASSIGNMENT,TK_OPASUM,TK_OPASUB,TK_OPAMULT,TK_OPADIV,TK_OPAMOD,TK_OPALEFTSHIFT,TK_OPARIGHTSHIFT,TK_OPABITAND,TK_OPABITOR,TK_OPABITXOR,TK_OPAND,TK_OPOR,TK_OPNEGATION,TK_OPSUM,TK_OPSUB,TK_OPMULT,TK_OPDIV,TK_OPMOD,TK_OPINC,TK_OPDEC,TK_OPBITAND,TK_OPBITOR,TK_OPBITXOR,TK_OPBITCOMP,TK_OPBITLEFTSHIFT],

    }