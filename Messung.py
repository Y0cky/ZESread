import sys
import time

def main():
    # �berpr�fen der Anzahl der �bergabeparameter
    if len(sys.argv) != 3:
        print("Usage: Messung.py <Dateiname> <Anzahl>")
        sys.exit(1)

    # Dateiname und Anzahl der Messungen aus �bergabeparametern extrahieren
    name = sys.argv[1]
    try:
        num_measurements = int(sys.argv[2])
    except ValueError:
        print("Die Anzahl der Messungen muss eine Ganzzahl sein.")
        sys.exit(1)

    data_file = name + ".txt"
    measurements_received = 0

    while measurements_received < num_measurements:
        try:
            # �ffnen der Datei f�r das Lesen der Messdaten
            f = open("data.txt", 'r')
            data = f.read()
            f.close()

            if data:
                # �ffnen der Logdatei und Anh�ngen der Messdaten
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

    print("Messung abgeschlossen. Insgesamt", measurements_received, "Messungen durchgef�hrt und in", data_file, "gespeichert.")

if __name__ == "__main__":
    main()
