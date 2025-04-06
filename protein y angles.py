from Bio.PDB import *
parser = MMCIFParser()
structure = parser.get_structure("6VYB", "6vyb.cif")  # Protéine Spike COVID
# Calcul des angles entre chaînes...
