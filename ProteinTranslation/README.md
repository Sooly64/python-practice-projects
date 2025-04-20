# DNA/RNA Codon Translator

This Python script translates DNA or RNA sequences into a sequence of amino acids based on the genetic code. It supports user interaction through the console, validates inputs, and stops translation when a stop codon is encountered.

---

## Features

- Accepts either **DNA** or **RNA** sequences
- Verifies valid characters and length (must be divisible by 3)
- Translates codons into amino acids
- Stops translation on encountering a stop codon (`TAA`, `TAG`, `TGA` for DNA or `UAA`, `UAG`, `UGA` for RNA)
- Graceful exit with an option to quit or continue

---

## How It Works

1. User is asked if they want to translate a sequence.
2. If yes, they choose between DNA or RNA.
3. They input a sequence.
4. The sequence is validated.
5. It is split into codons and translated until a stop codon is encountered.
6. The amino acid sequence is printed using `-` as a separator.

---

## 🧪 Sample Run

```
Do you want to translate a sequence? y/n: y
DNA or RNA sequence? R/D: d
Enter a DNA sequence: ATGGTTTAA
Protein Sequence: Methionine-Valine
Do you want to translate a sequence? y/n: n
Exiting the program. Goodbye!
```

---

## Supported Codons

All standard codons for DNA and RNA are supported based on the universal genetic code. Invalid or unknown codons will be labeled as `"Invalid Codon"`.

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```text
.
└── codon_translator.py   # Main script file
```

---

## Notes

- Sequence must be **uppercase** and of length multiple of 3
- DNA must contain only `A, T, C, G`
- RNA must contain only `A, C, G, U`
- The translator **stops** at the first Stop codon

---

## Author

Made with care and brainpower, lil bit of Mocha

---
