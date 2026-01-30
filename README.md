# Procesor-de-imagini-ASCII-art

## Autor
- **Nume:** Damian Anghel
- **Grupa:** [1.1]
- **Email:** [damian-samuel.anghel@student.upt.ro]
- **An academic:** 2025-2026

## Descriere
Procesor de imagini ASCII art in Python. Conversie PNG/JPG si text in ASCII, cu filtre si export.

## Tehnologii folosite
- **Limbaj:** Python 3.11
- **Biblioteci:**
  - Pillow - procesare imagini
  - pyfiglet - conversie text → ASCII banner
- **Tools:** Git, Docker

## Cerinte sistem
- Python 3.12
- Windows / Linux / macOS
- Biblioteca Pillow si pyfiglet instalate (`pip install -r requirements.txt`)

## Instalare
```bash
#Clone repository
git clone https://github.com/angheldamian/Procesor-de-imagini-ASCII-art.git
cd Procesor-de-imagini-ASCII-art

#Instalare dependente
pip install -r requirements.txt

#Conversie imagine
py src/main.py data/input.png --width 80 --preview

#Conversie text in banner ASCII
python src/main.py --text "HELLO" --font banner

#Exemple de utilizare

#1.Conversie imagine cu caractere implicite:
py src/main.py data/input.png --width 60

#2.Conversie text in banner ASCII:
py src/main.py --text "HELLO" --font banner

#3.Conversie imagine cu set de caractere custom:
py src/main.py data/input.png --chars "@#*+=-:. " --width 80

#4.Aplicare filtre imagine si preview:
py src/main.py data/input.png --filter grayscale --preview

#5.Export ASCII in fisier text:
py src/main.py data/input.png --output data/output.txt --width 60

Functionalitati implementate:
Convertire imagini PNG/JPG in ASCII art
Convertire text in banner ASCII art
Scalare dimensiune (resize cu pastrarea proportiilor)
Filtre: grayscale, invert, contrast, blur
Set de caractere configurabil
Export in fisier text
Ajustare nivel de detaliu (rezolutie ASCII)
Preview in terminal



Decizie de design:
Parser-ul CLI este separat in cli.py pentru claritate si reutilizare.
Conversia imaginilor in ASCII este in ascii_converter.py, iar filtrele in filters.py pentru modularitate.

Probleme intalnite si solutii:
Problema: Pillow nu gasea fisierul input.png.
Solutie: Fisierul a fost mutat in folderul data/ si Docker foloseste montarea folderului local.
Problema: Module Python nu erau gasite.
Solutie: Am corectat importurile si structura src/.

#Testare
 
Puteti testa functionalitatile aplicatiei manual ruland scriptul principal cu imagini sau text.

##Teste manuale recomandate

#1.Export ASCII in fisier text
py src/main.py data/input.png --output data/output.txt --width 80
#2. Combina optiuni multiple
py src/main.py data/input.png --chars "@#*+=-:. " --width 60 --filter grayscale --output data/output2.txt
#3.Aplicare filtre imagine
py src/main.py data/logo.png --filter grayscale --preview
py src/main.py data/test.png --filter invert --preview
py src/main.py data/logo.png --filter blur --preview
py src/main.py data/test.png --filter contrast --preview
#4.Test text si export
python src/main.py --text "TEST" --font banner --output data/text_banner.txt

Docker

#1️.Build imagine Docker
docker build -t angheldamian/procesor-de-imagini-ascii-art .

#2️.Run container
docker run -it -v ${PWD}/data:/app/data angheldamian/procesor-de-imagini-ascii-art data/input.png --width 80 --preview

Resurse folosite:
(https://chatgpt.com)
(https://medium.com/@kumarishriti27/convert-an-image-into-ascii-art-using-python-google-colab-9c20231426d9)
(https://github.com/mark-rez/Ascii-Image-Processor/blob/main/main.py)

Profil GitHub:(https://github.com/angheldamian)
