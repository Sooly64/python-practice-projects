# UX DECLARATIONS
error_message = "Invalid input, please try again!"
INVALID_CODON = "Invalid Codon"


# Amino acid variable Declarations
PHE = "Phenylalanine"
LEU = "Leucine"
ILE = "Isoleucine"
MET = "Methionine"
VAL = "Valine"
SER = "Serine"
PRO = "Proline"
THR = "Threonine"
ALA = "Alanine"
TYR = "Tyrosine"
STOP = "Stop"
HIS = "Histidine"
GLN = "Glutamine"
ASN = "Asparagine"
LYS = "Lysine"
ASP = "Aspartic acid"
GLU = "Glutamic acid"
CYS = "Cysteine"
TRP = "Tryptophan"
ARG = "Arginine"
GLY = "Glycine"

# Amino acid mapping
DNA_CODON_PAIRS = {
    "TTT": PHE, "TTC": PHE,
    "TTA": LEU, "TTG": LEU, "CTT": LEU, "CTC": LEU, "CTA": LEU, "CTG": LEU,
    "ATT": ILE, "ATC": ILE, "ATA": ILE,
    "ATG": MET,
    "GTT": VAL, "GTC": VAL, "GTA": VAL, "GTG": VAL,
    "TCT": SER, "TCC": SER, "TCA": SER, "TCG": SER,
    "CCT": PRO, "CCC": PRO, "CCA": PRO, "CCG": PRO,
    "ACT": THR, "ACC": THR, "ACA": THR, "ACG": THR,
    "GCT": ALA, "GCC": ALA, "GCA": ALA, "GCG": ALA,
    "TAT": TYR, "TAC": TYR,
    "TAA": STOP, "TAG": STOP, "TGA": STOP,
    "CAT": HIS, "CAC": HIS,
    "CAA": GLN, "CAG": GLN,
    "AAT": ASN, "AAC": ASN,
    "AAA": LYS, "AAG": LYS,
    "GAT": ASP, "GAC": ASP,
    "GAA": GLU, "GAG": GLU,
    "TGT": CYS, "TGC": CYS,
    "TGG": TRP,
    "CGT": ARG, "CGC": ARG, "CGA": ARG, "CGG": ARG,
    "GGT": GLY, "GGC": GLY, "GGA": GLY, "GGG": GLY
}

RNA_CODON_PAIRS = {
    "UUU": PHE, "UUC": PHE,
    "UUA": LEU, "UUG": LEU, "CUU": LEU, "CUC": LEU, "CUA": LEU, "CUG": LEU,
    "AUU": ILE, "AUC": ILE, "AUA": ILE,
    "AUG": MET,
    "GUU": VAL, "GUC": VAL, "GUA": VAL, "GUG": VAL,
    "UCU": SER, "UCC": SER, "UCA": SER, "UCG": SER, "AGU": SER, "AGC": SER,
    "CCU": PRO, "CCC": PRO, "CCA": PRO, "CCG": PRO,
    "ACU": THR, "ACC": THR, "ACA": THR, "ACG": THR,
    "GCU": ALA, "GCC": ALA, "GCA": ALA, "GCG": ALA,
    "UAU": TYR, "UAC": TYR,
    "UAA": STOP, "UAG": STOP, "UGA": STOP,
    "CAU": HIS, "CAC": HIS,
    "CAA": GLN, "CAG": GLN,
    "AAU": ASN, "AAC": ASN,
    "AAA": LYS, "AAG": LYS,
    "GAU": ASP, "GAC": ASP,
    "GAA": GLU, "GAG": GLU,
    "UGU": CYS, "UGC": CYS,
    "UGG": TRP,
    "CGU": ARG, "CGC": ARG, "CGA": ARG, "CGG": ARG, "AGA": ARG, "AGG": ARG,
    "GGU": GLY, "GGC": GLY, "GGA": GLY, "GGG": GLY
}

def getAcids(sequence, isDNA):
    if isDNA:
        used_pairs = DNA_CODON_PAIRS
    else:
        used_pairs = RNA_CODON_PAIRS
    acids = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if codon in used_pairs:
            # Stop on Last Codon
            if used_pairs[codon] == STOP:
                break
            acids.append(used_pairs[codon])
        else:
            acids.append(INVALID_CODON)
    return acids

# RNA/DNA Sequence getter
def get_valid_sequence(isDNA):
    while True:
        if isDNA:
            sequence = input("Enter a DNA sequence: ").upper().strip()
            if len(sequence) % 3 != 0:
                print("Sequence length must be a multiple of 3.")
            elif not all(char in "ATCG" for char in sequence):
                print("DNA must contain only A, T, C, or G.")
            else:
                return sequence
        else:
            sequence = input("Enter a RNA sequence: ").upper().strip()
            if len(sequence) % 3 != 0:
                print("Sequence length must be a multiple of 3.")
            elif not all(char in "ACGU" for char in sequence):
                print("RNA must contain only A, C, G, or U.")
            else:
                return sequence

# DNA or RNA determiner
def get_isDNA():
    while True:
        command = input("DNA or RNA sequence? R/D: ").lower().strip()
        if command == "r":
            return False
        elif command == "d":
            return True
        else:
            print(error_message)

def print_protein(acids):
    print("Protein Sequence: ", end="")
    print("-".join(acids))

# Main Control Flow
while True:
    exit_command = input("Do you want to translate a sequence? y/n: ").lower().strip()
    if exit_command == "n":
        print("Exiting the program. Goodbye!")
        break
    elif exit_command == "y":
        isDNA = get_isDNA()
        sequence = get_valid_sequence(isDNA)
        acids = getAcids(sequence, isDNA)
        print_protein(acids)
    else:
        print(error_message)
