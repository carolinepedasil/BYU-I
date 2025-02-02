from formula import parse_formula

NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.941, 3],
        "Be": ["Beryllium", 9.012182, 4],
        "B": ["Boron", 10.811, 5],
        "C": ["Carbon", 12.0107, 6],
        "N": ["Nitrogen", 14.0067, 7],
        "O": ["Oxygen", 15.9994, 8],
        "F": ["Fluorine", 18.9984032, 9],
        "Ne": ["Neon", 20.1797, 10],
        "Na": ["Sodium", 22.98976928, 11],
        "Mg": ["Magnesium", 24.305, 12],
        "Al": ["Aluminum", 26.9815386, 13],
        "Si": ["Silicon", 28.0855, 14],
        "P": ["Phosphorus", 30.973762, 15],
        "S": ["Sulfur", 32.065, 16],
        "Cl": ["Chlorine", 35.453, 17],
        "Ar": ["Argon", 39.948, 18],
        "K": ["Potassium", 39.0983, 19],
        "Ca": ["Calcium", 40.078, 20],
        # Add all other elements as needed...
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity
    return total_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Exceed Requirements: Compute and return the total number of protons in a molecule."""
    total_protons = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]  # Access atomic number
        total_protons += atomic_number * quantity
    return total_protons

def get_formula_name(formula, known_molecules_dict):
    """Exceed Requirements: Try to find formula in the known_molecules_dict.
    If found, return the chemical name; otherwise, return 'unknown compound'.
    """
    return known_molecules_dict.get(formula, "unknown compound")

def main():
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    formula = input("Enter the molecular formula of the sample: ")
    mass = float(input("Enter the mass in grams of the sample: "))
    periodic_table = make_periodic_table()
    symbol_quantity_list = parse_formula(formula, periodic_table)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    num_moles = mass / molar_mass
    compound_name = get_formula_name(formula, known_molecules_dict)
    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    print(f"{molar_mass:.5f} grams/mole")
    print(f"{num_moles:.5f} moles")
    print(f"Compound name: {compound_name}")
    print(f"Total number of protons: {total_protons}")

main()
