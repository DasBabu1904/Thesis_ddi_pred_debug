from rdkit import Chem
from rdkit.Chem import Draw

# Example SMILES string
smiles = "CCOC(=O)C1=C[C@@H](OC(CC)CC)[C@H](NC(C)=O)[C@@H](N)C1"  # Ethanol

# Convert SMILES to a molecule object
molecule = Chem.MolFromSmiles(smiles)

# Draw the molecule
Draw.MolToImage(molecule).show()
Draw.MolToImage(molecule).show()