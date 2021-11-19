from enum import Enum


def from_short_name(short_name: str):
    for typeofword in TypeOfWord:
        value = typeofword.value().get('short_name')
        if value == short_name:
            return typeofword


class TypeOfWord(Enum):
    CC = {'full_name': "coordinating conjunction", 'short_name': "CC", 'example': "and"}
    CD = {'full_name': "cardinal number", 'short_name': "CD", 'example': "1,  third"}
    DT = {'full_name': "determiner", 'short_name': "DT", 'example': "the"}
    EX = {'full_name': "existential there", 'short_name': "EX", 'example': "there is"}
    FW = {'full_name': "foreign word", 'short_name': "FW", 'example': "les"}
    IN = {'full_name': "preposition,  subordinating conjunction", 'short_name': "IN", 'example': "in,  of,  like"}
    IN_THAT = {'full_name': "that as subordinate", 'short_name': "IN/THAT", 'example': "that"}
    JJ = {'full_name': "adjective", 'short_name': "JJ", 'example': "green"}
    JJR = {'full_name': "adjective,  comparative", 'short_name': "JJR", 'example': "greener"}
    JJS = {'full_name': "adjective,  superlative", 'short_name': "JJS", 'example': "greenest"}
    LS = {'full_name': "list marker", 'short_name': "LS", 'example': "1}"}
    MD = {'full_name': "modal", 'short_name': "MD", 'example': "could,  will"}
    NN = {'full_name': "noun,  singular or mass", 'short_name': "NN", 'example': "table"}
    NNS = {'full_name': "noun plural", 'short_name': "NNS", 'example': "tables"}
    NP = {'full_name': "proper noun,  singular", 'short_name': "NP", 'example': "John"}
    NPS = {'full_name': "proper noun,  plural", 'short_name': "NPS", 'example': "Vikings"}
    PDT = {'full_name': "predeterminer", 'short_name': "PDT", 'example': "both the boys"}
    POS = {'full_name': "possessive ending", 'short_name': "POS", 'example': "friend’s"}
    PP = {'full_name': "personal pronoun", 'short_name': "PP", 'example': "I,  he,  it"}
    PPZ = {'full_name': "possessive pronoun", 'short_name': "PPZ", 'example': "my,  his"}
    RB = {'full_name': "adverb", 'short_name': "RB", 'example': "however,  usually,  naturally,  here,  good"}
    RBR = {'full_name': "adverb,  comparative", 'short_name': "RBR", 'example': "better"}
    RBS = {'full_name': "adverb,  superlative", 'short_name': "RBS", 'example': "best"}
    RP = {'full_name': "particle", 'short_name': "RP", 'example': "give up"}
    SENT = {'full_name': "Sentence-break punctuation", 'short_name': "SENT", 'example': ". ! ?"}
    SYM = {'full_name': "Symbol", 'short_name': "SYM", 'example': "/ [ = *"}
    TO = {'full_name': "infinitive ‘to’", 'short_name': "TO", 'example': "togo"}
    UH = {'full_name': "interjection", 'short_name': "UH", 'example': "uhhuhhuhh"}
    VB = {'full_name': "verb be,  base form", 'short_name': "VB", 'example': "be"}
    VBD = {'full_name': "verb be,  past tense", 'short_name': "VBD", 'example': "was,  were"}
    VBG = {'full_name': "verb be,  gerund/present participle", 'short_name': "VBG", 'example': "being"}
    VBN = {'full_name': "verb be,  past participle", 'short_name': "VBN", 'example': "been"}
    VBP = {'full_name': "verb be,  sing. present,  non-3d", 'short_name': "VBP", 'example': "am,  are"}
    VBZ = {'full_name': "verb be,  3rd person sing. present", 'short_name': "VBZ", 'example': "is"}
    VH = {'full_name': "verb have,  base form", 'short_name': "VH", 'example': "have"}
    VHD = {'full_name': "verb have,  past tense", 'short_name': "VHD", 'example': "had"}
    VHG = {'full_name': "verb have,  gerund/present participle", 'short_name': "VHG", 'example': "having"}
    VHN = {'full_name': "verb have,  past participle", 'short_name': "VHN", 'example': "had"}
    VHP = {'full_name': "verb have,  sing. present,  non-3d", 'short_name': "VHP", 'example': "have"}
    VHZ = {'full_name': "verb have,  3rd person sing. present", 'short_name': "VHZ", 'example': "has"}
    VV = {'full_name': "verb,  base form", 'short_name': "VV", 'example': "take"}
    VVD = {'full_name': "verb,  past tense", 'short_name': "VVD", 'example': "took"}
    VVG = {'full_name': "verb,  gerund/present participle", 'short_name': "VVG", 'example': "taking"}
    VVN = {'full_name': "verb,  past participle", 'short_name': "VVN", 'example': "taken"}
    VVP = {'full_name': "verb,  sing. present,  non-3d", 'short_name': "VVP", 'example': "take"}
    VVZ = {'full_name': "verb,  3rd person sing. present", 'short_name': "VVZ", 'example': "takes"}
    WDT = {'full_name': "wh-determiner", 'short_name': "WDT", 'example': "which"}
    WP = {'full_name': "wh-pronoun", 'short_name': "WP", 'example': "who,  what"}
    WP2 = {'full_name': "possessive wh-pronoun", 'short_name': "WP$", 'example': "whose"}
    WRB = {'full_name': "wh-abverb", 'short_name': "WRB", 'example': "where,  when"}
    DOLLAR_SIGN = {'full_name': "$", 'short_name': "$", 'example': "$"}
    OCTOTHORPE = {'full_name': "#", 'short_name': "#", 'example': "#"}
    QUOTE = {'full_name': "Quotation marks", 'short_name': "“", 'example': "‘ “"}
    ACUTE_DOUBLE = {'full_name': "Opening quotation marks", 'short_name': "``", 'example': "‘ “"}
    OPEN_OR_LEFT_PARENTHESIS = {'full_name': "Opening brackets", 'short_name': "': ", 'example': "':  {"}
    CLOSE_OR_RIGHT_PARENTHESIS = {'full_name': "Closing brackets", 'short_name': "}", 'example': "} }"}
    COMMA = {'full_name': "Comma", 'short_name': ", ", 'example': ", "}
    COLON = {'full_name': "Punctuation", 'short_name': "': ", 'example': "– ; ':  — …"}

