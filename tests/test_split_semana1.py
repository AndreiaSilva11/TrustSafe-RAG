import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASTA = ROOT / "data" / "processed"

def test_quantidade_registros():
    treino = pd.read_csv(PASTA / "train_semana1.csv")
    teste = pd.read_csv(PASTA / "test_semana1.csv")
    registro = pd.read_csv(PASTA / "split_registro_semana1.csv")

    assert len(treino) == 146
    assert len(teste) == 34
    assert len(registro) == 180

def test_ids_sem_duplicidade_ou_intersecao():
    treino = pd.read_csv(PASTA / "train_semana1.csv")
    teste = pd.read_csv(PASTA / "test_semana1.csv")

    assert treino["id_consulta"].is_unique
    assert teste["id_consulta"].is_unique

    assert set(treino["id_consulta"]).isdisjoint(
        set(teste["id_consulta"])
    )

def test_grupos_nao_separados():
    treino = pd.read_csv(PASTA / "train_semana1.csv")
    teste = pd.read_csv(PASTA / "test_semana1.csv")

    assert set(treino["grupo_split"]).isdisjoint(
        set(teste["grupo_split"])
    )

def test_distribuicao_riscos():
    treino = pd.read_csv(PASTA / "train_semana1.csv")
    teste = pd.read_csv(PASTA / "test_semana1.csv")

    assert treino["risco"].value_counts().to_dict() == {
        "alto": 49, "baixo": 49, "moderado": 48
    }

    assert teste["risco"].value_counts().to_dict() == {
        "alto": 11, "baixo": 11, "moderado": 12
    }
