import sys
import time

def main():
    # Überprüfen der Anzahl der Übergabeparameter
    if len(sys.argv) != 3:
        print("Usage: Messung.py <Dateiname> <Anzahl>")
        sys.exit(1)

    # Dateiname und Anzahl der Messungen aus Übergabeparametern extrahieren
    name = sys.argv[1]
    try:
        num_measurements = int(sys.argv[2])
    except ValueError:
        print("Die Anzahl der Messungen muss eine Ganzzahl sein.")
        sys.exit(1)

    data_file = name + ".txt"
    log = open(data_file, 'w')
    log.close()
    print("Vergangene Werte geloescht")
    
    measurements_received = 0
    
    print("Messung startet in 4 sec")
    time.sleep(4)

    while measurements_received < num_measurements:
        try:
            # Öffnen der Datei für das Lesen der Messdaten
            f = open("data.txt", 'r')
            data = f.read()
            f.close()

            if data:
                # Öffnen der Logdatei und Anhängen der Messdaten
                log = open(data_file, 'a')
                log.write(data + "\n")
                log.close()
                
                print("Empfangene Daten:", data)
                measurements_received += 1
            else:
                print("Keine Daten gefunden.")
        except IOError:
            print("Fehler beim Zugriff auf die Datei.")

        # Wartezeit zwischen den Messungen
        time.sleep(0.5)

    print("Messung abgeschlossen. Insgesamt", measurements_received, "Messungen durchgefuehrt und in", data_file, "gespeichert.")
    
if __name__ == "__main__":
    main()
