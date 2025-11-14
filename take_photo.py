import time
from picamera2 import Picamera2

def main():
    picam2 = Picamera2()
    
    # Kamera initialisieren und Startparameter setzen
    camera_config = picam2.create_still_configuration()
    picam2.configure(camera_config)
    picam2.start()
    
    # Kurze Wartezeit, damit die Kamera korrekt initialisiert
    time.sleep(2)
    
    # Foto aufnehmen
    filename = "/home/pi/startup_foto.jpg"
    picam2.capture_file(filename)
    print(f"Foto aufgenommen und gespeichert unter: {filename}")
    
    # Kamera stoppen (optional, kann weiterlaufen falls Streaming benötigt wird)
    picam2.stop()

if __name__ == "__main__":
    main()
