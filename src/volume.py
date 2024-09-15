from PyPDF2 import PdfMerger
from capitolo import Capitolo


class Volume:

    def __init__(self, numeri_capitoli: list[int], nome_file: str):
        self.numeri_capitoli = numeri_capitoli
        self.nome_file = nome_file
        self.lista_capitoli = []

    def scarica(self):
        for i,numero_capitolo in enumerate(self.numeri_capitoli,1):
            print(f"scaricando il capitolo {i}/{len(self.numeri_capitoli)}")
            capitolo = Capitolo(numero_capitolo)
            self.lista_capitoli.append(capitolo)
            capitolo.scarica()
            capitolo.converti_in_pdf()
            capitolo.elimina_immagini()

    def mergi_il_tutto(self):
        merger = PdfMerger()
        for capitolo in self.lista_capitoli:
            merger.append(f"{capitolo.numero_capitolo}.pdf", str(capitolo.numero_capitolo))
        merger.write(self.nome_file)
        merger.close()

    def elimina(self):
        for capitolo in self.lista_capitoli:
            capitolo.elimina_pdf()
