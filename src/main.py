from volume import Volume
from typing import Optional
from typing_extensions import Annotated
from capitolo import Capitolo
import recupera_info_volumi
import typer

app = typer.Typer(name="Scarica Capitoli OnePiece")


@app.command()
def ultimo():
    ultimo_capitolo = Capitolo(Capitolo.ultimo_capitolo())
    ultimo_capitolo.scarica()
    ultimo_capitolo.converti_in_pdf()
    ultimo_capitolo.elimina_immagini()


@app.command()
def scarica_capitoli(
    capitolo: Annotated[int, typer.Argument(help="capitolo da scaricare")],
    capitolo2: Annotated[Optional[int], typer.Argument(help="ultimo capitolo")] = None,
):
    if capitolo2:
        capitoli = Volume(
            list(range(capitolo, capitolo2 + 1)), f"{capitolo}-{capitolo2}.pdf"
        )
        capitoli.scarica()
        capitoli.mergi_il_tutto()
        capitoli.elimina()

    else:
        capitolo = Capitolo(capitolo)
        capitolo.scarica()
        capitolo.converti_in_pdf()
        capitolo.elimina_immagini()


@app.command()
def scarica_volume(vol: Annotated[int, typer.Argument(help="volume da scaricare")]):
    dizionario = recupera_info_volumi.ottieni_volumi()
    chap1, chap2 = dizionario[vol]
    lista = list(range(chap1, chap2 + 1))
    volume = Volume(lista, f"volume n.{vol}.pdf")
    volume.scarica()
    volume.mergi_il_tutto()
    volume.elimina()


if __name__ == "__main__":
    app()
