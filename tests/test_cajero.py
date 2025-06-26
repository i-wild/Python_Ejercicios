import importlib
import builtins
import os
import sys

# Add repository root to path so we can import cajero module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_retirar_insuficiente(monkeypatch, capsys):
    # Ensure interactive input during module import doesn't block while importing
    monkeypatch.setattr(builtins, 'input', lambda *args, **kwargs: '0')
    cajero = importlib.import_module('ejercicios.cajero')
    importlib.reload(cajero)
    # Snapshot of cash before attempting withdrawal
    available_before = cajero.disponible.copy()
    cajero.retirar(cajero.total_disponible() + 1)
    captured = capsys.readouterr()
    assert "Error, no hay suficiente efectivo" in captured.out
    # No cash should be dispensed
    assert cajero.disponible == available_before
