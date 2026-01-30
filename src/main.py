from ascii_art.converter import converte_image_to_ascii
from ascii_art.banner import text_to_ascii
from ascii_art.filters import apply_filters
from cli import parse_args  #importam functia de parsing

def main():
    args = parse_args()

    #Daca e text, convertim la banner
    if args.text:
        banner = text_to_ascii(args.text, font=args.font)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(banner)
        print(banner)
        return

    #Daca e imagine
    if args.input:
        image_path = args.input
        width = args.width
        chars = args.chars
        filters = args.filter

        try:
            from PIL import Image
            image = Image.open(image_path)
            image = apply_filters(image, filters)
            ascii_art = converte_image_to_ascii(image_path=image_path, width=width, chars=chars)
        except FileNotFoundError:
            print(f"Eroare: fisierul '{image_path}' nu a fost gasit.")
            return
        except Exception as e:
            print(f"Eroare la conversie: {e}")
            return

        print(ascii_art)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(ascii_art)

if __name__ == "__main__":
    main()
