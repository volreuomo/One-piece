import gestione_immagini
import scarica_immagini
import shutil
from pathlib import Path

URL = f"https://ww1.tcbscans.org/manga/one-piece/"


class Capitolo:

    def __init__(self, numero_capitolo: int):
        self.numero_pagine = None
        self.numero_capitolo = numero_capitolo

    def scarica(self):
        self.numero_pagine = scarica_immagini.scarica_immagini(self.numero_capitolo)

    def converti_in_pdf(self):
        immagini = [
            gestione_immagini.conv_rgba_to_rgb(f"{self.numero_capitolo}/{i}.jpg")
            for i in range(1, self.numero_pagine + 1)
        ]
        immagini[0].save(f"{self.numero_capitolo}.pdf", "PDF", append_images=immagini[1:], save_all=True)

    def elimina_immagini(self):
        path = Path(str(self.numero_capitolo))
        if path.exists():
            shutil.rmtree(str(self.numero_capitolo))

    def elimina_pdf(self):
        path = Path(f"{self.numero_capitolo}.pdf")
        path.unlink()

    @staticmethod
    def ultimo_capitolo() -> int:
        import requests
        from bs4 import BeautifulSoup
        url = f"{URL}ajax/chapters/"
        response = requests.post(url)
        soup = BeautifulSoup(response.text, "html.parser")
        chapter_links = [link["href"] for link in soup.find_all("a")]
        _, last_link, *_ = chapter_links
        chapter_number = last_link.split("-")[-1].strip("/")
        return int(chapter_number)
