import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Procesor ASCII Art"
    )

    parser.add_argument("input", nargs="?", help="Fisier imagine")
    parser.add_argument("--output", help="Fisier de iesire")
    parser.add_argument("--width", type=int, default=80, help="Latime ASCII")
    parser.add_argument("--scale", type=float, help="Factor scalare")
    parser.add_argument("--chars", default="@#*+=-:. ", help="Set caractere ASCII")
    parser.add_argument("--filter", nargs="*", default=[], help="Filtre imagine")
    parser.add_argument("--preview", action="store_true", help="Afisare in terminal")


    parser.add_argument("--text", help="Text de convertit in ASCII banner")
    parser.add_argument("--font", default="standard", help="Fond pentru text")


    return parse.parse_args()