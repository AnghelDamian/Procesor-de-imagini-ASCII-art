import pyfiglet

def text_to_banner(text, font):
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(text)