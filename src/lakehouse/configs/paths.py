from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA = PROJECT_ROOT / "data"

BRONZE = DATA / "bronze"

SILVER = DATA / "silver"

GOLD = DATA / "gold"

CHECKPOINTS = DATA / "checkpoints"