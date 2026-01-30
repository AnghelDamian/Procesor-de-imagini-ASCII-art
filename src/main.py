import argparse
from PIL import Image
from ascii_art.converter import image_to_ascii

#Functia principala care permite setarea fisierului de intrare, latimea ASCII si a fisierului de iesire
def main():
    parser = argparse.ArgumentParser(
        description="Convertiti o imagine in ASCII art."
    )
    parser.add_argument(
        "image_path",
        help="Calea catre imagine de convertit"
    )
    parser.add_argument(
        "-w", "--width",
        type=int,
        default=100,
        help="Latime rezultata in caractere ASCII"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Fisier in care se salveaza rezultatul"
    )

    #Argumentele
    args = parser.parse_args()
    image_path = args.image_path
    width = args.width
    output_file = args.output

    #Deschidem imaginea
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Eroare: fisierul '{image_path}' nu a fost gasit.")
        return
    except Exception as e:
        print(f"Eroare la deschiderea imaginii: {e}")
        return

    #Convertim imagine in ASCII
    try:
        ascii_art = image_to_ascii(img, width=width, chars="@%#*+=-:. ")
    except Exception as e:
        print(f"Eroare la conversie: {e}")
        return

    #Afisam rezulatele in consola
    print(ascii_art)

    #Daca sa dat fisier de output salvam rezultatul
    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(ascii_art)
            print(f"Rezultatul a fost salvat in '{output_file}'")
        except Exception as e:
            print(f"Eroare la salvare: {e}")

if __name__ == "__main__":
    main()

