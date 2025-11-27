import json
import torch
from pathlib import Path
import numpy as np
from typing import Dict, List, Any
from datetime import datetime

class Config:
    """Configuración central del proyecto - VERSIÓN 2 REGIONES"""
    
    # Rutas
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    RAW_DIR = DATA_DIR / "raw"
    PROCESSED_DIR = DATA_DIR / "processed"
    SYNTHETIC_DIR = DATA_DIR / "synthetic"
    RESULTS_DIR = BASE_DIR / "results" / "fase1"
    
    # Modelo
    MODEL_NAME = "gpt2-xl"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Parámetros
    RANDOM_SEED = 42
    N_QUINTILES = 5
    N_EXAMPLES_PER_REGION = 50
    N_SYNTHETIC_PER_REGION = 30
    
    # ACTUALIZADO: Solo 2 regiones
    REGIONS = ['latam', 'europe']
    
    REGION_NAMES = {
        'latam': 'Latinoamérica',
        'europe': 'Europa (Grecia + Nórdica)'
    }
    
    @classmethod
    def setup_directories(cls):
        """Crear estructura de directorios"""
        for dir_path in [cls.RAW_DIR, cls.PROCESSED_DIR, 
                        cls.SYNTHETIC_DIR, cls.RESULTS_DIR]:
            dir_path.mkdir(parents=True, exist_ok=True)
        print("✓ Directorios creados")


def load_json(filepath: Path) -> List[Dict]:
    """Cargar archivo JSON con manejo de errores"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Cargados {len(data)} ejemplos desde {filepath.name}")
        return data
    except FileNotFoundError:
        print(f"✗ Archivo no encontrado: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"✗ Error al parsear JSON: {e}")
        return []


def save_json(data: Any, filepath: Path, indent: int = 2):
    """Guardar datos en JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
    print(f"✓ Guardado en {filepath}")


def log_decision(decision: str):
    """Registrar decisión metodológica"""
    log_file = Config.BASE_DIR / "FASE1_DECISIONES.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n[{timestamp}] {decision}\n")
    
    print(f"📝 Decisión registrada: {decision}")


def set_seed(seed: int = 42):
    """Fijar semilla para reproducibilidad"""
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    print(f"✓ Semilla fijada: {seed}")