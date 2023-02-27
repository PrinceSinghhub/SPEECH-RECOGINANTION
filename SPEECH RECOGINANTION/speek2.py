from win32com.client import Dispatch
speak = Dispatch("SAPI.Spvoice")
speak.Speak("Codex Coder")