from pathlib import Path
import pandas as pd

def test_dataset():
    caminho_csv = Path(__file__).resolve().parent.parent / "docs" / "auditoria_escopo_v06.csv"
    df = pd.read_csv(caminho_csv)

    assert len(df) == 180
    assert df["id_consulta"].nunique() == 180
    assert df["risco"].value_counts().to_dict() == {
        "baixo": 60,
        "moderado": 60,
        "alto": 60
    }
    assert (df["decisao"] == "INCLUIR").all()
