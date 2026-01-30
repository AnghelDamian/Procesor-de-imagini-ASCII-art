import pyfiglet

def text_to_ascii(text, font="standard"):
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(text)
