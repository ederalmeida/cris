import win32gui
import win32process
import psutil

# Função para verificar qual a janela ativa do windows
def verifica_janela_ativa():
    w = win32gui
    w.GetWindowText (w.GetForegroundWindow())
    pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
    return psutil.Process(pid[-1]).name()