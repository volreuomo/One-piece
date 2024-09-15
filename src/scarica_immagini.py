import requests
from bs4 import BeautifulSoup
from pathlib import Path
from rich.progress import Progress

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36"}
URL = f"https://ww1.tcbscans.org/manga/one-piece/"


def recupera_link(numero_capitolo: int) -> list[str]:
    response = requests.get(f"{URL}chapter-{numero_capitolo}", headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    return [img["src"] for img in soup.find_all(class_="wp-manga-chapter-img")]


def scarica_immagine(link, file_path):
    response = requests.get(link)
    response.raise_for_status()
    with open(file_path, "wb") as f:
        f.write(response.content)


def scarica_immagini(capitolo: int) -> int:
    chapter_dir = Path(str(capitolo))
    chapter_dir.mkdir(exist_ok=True)
    lista_immagini = recupera_link(capitolo)
    with Progress() as progress:
        task = progress.add_task(
            "[green]Scaricando le immagini...", total=len(lista_immagini)
        )
        for pagina, link in enumerate(lista_immagini, 1):
            file_path = Path.joinpath(chapter_dir, f"{pagina}.jpg")
            scarica_immagine(link, file_path)
            progress.update(task, advance=1)
    return len(lista_immagini)
