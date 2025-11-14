import subprocess
import datetime
import os
import sys

def take_photo(output_dir="photos", width=1920, height=1080):
    """
    Nimmt ein Foto mit rpicam-still auf und speichert es im angegebenen Verzeichnis.
    """
    try:
        # Verzeichnis anlegen, falls nicht vorhanden
        os.makedirs(output_dir, exist_ok=True)

        # Zeitstempel für Dateinamen
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"photo_{timestamp}.jpg"
        filepath = os.path.join(output_dir, filename)

        # rpicam-still Befehl
        cmd = [
            "rpicam-still",
            "-o", filepath,          # Ausgabedatei
            "--width", str(width),   # Bildbreite
            "--height", str(height), # Bildhöhe
            "--timeout", "1000"      # 1 Sekunde Vorlauf
        ]

        print(f"[INFO] Foto wird aufgenommen: {filepath}")
        subprocess.run(cmd, check=True)
        print("[OK] Foto erfolgreich gespeichert.")

    except FileNotFoundError:
        print("[FEHLER] rpicam-still nicht gefunden. Bitte libcamera-apps installieren.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[FEHLER] Aufnahme fehlgeschlagen: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[FEHLER] Unerwarteter Fehler: {e}")
        sys.exit(1)

if __name__ == "__main__":
    take_photo()
