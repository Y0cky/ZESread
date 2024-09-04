import sys
import zes
import openz
import closez
import writeopc
import time
import os

def main():
    # Open the serial interface, clear output buffer, initialize data path and instrument.
    LMG = openz.init("COM7", "BAUD=38400 EOS=LF PROTO=RTS/CTS")
    
    # Timeout auf 2000ms verlängern
    zes.SetTimeout(LMG, 2000)
    
    # Skip first measuring cycle after reset, it could contain invalid values
    writeopc.Write_command_with_OPC(LMG, ":INIT:IMM")
    
    # Skriptdatei ans LMG senden
    zes.Write(LMG, "CALC:FORM \"#Variablen definieren im LMG500\n$pi=3.1415927;\n$M=Ain:1*10;\n$n=Ain:2*351;\nM=$M;\nn=$n;\nPmech=$M*$n*2*$pi/60;\n$I1=Itrms:1;\n$I2=Itrms:2;\n$I3=Itrms:3;\nI=($I1+$I2+$I3)/3;\n$U1=Utrms:1;\n$U2=Utrms:2;\n$U3=Utrms:3;\nU=($U1+$U2+$U3)/3;\n$P1=P:1;\n$P2=P:2;\n$P3=P:3;\nPauf=$P1+$P2+$P3;\neta=Pmech/Pauf;\n$Temp=Udc:5;\nTemperatur=$Temp*20;\nI_R_mess=Itrms:7;\nU_R_Mess=Utrms:6;\n$Pm1=Pm:1;\n$Pm2=Pm:2;\n$Pm3=Pm:3;\nPauf_m=Pm:1+Pm:2+Pm:3;\nPauf_mb=Utrms:1*Itrms:1*PF:1+Utrms:2*Itrms:2*PF:2+Utrms:3*Itrms:3*PF:3;\"")
    
    print("Messwerte vom LMG werden empfangen\nn, M, Pmech, I, U, Pauf, eta, Temperatur, I_R_mess, U_R_mess")
    
    # 10 Variablen aus Skript abfragen
    zes.Write(LMG, ":TRIG:ACT;:FETC:VAR? (0:9)")
    
    # Kontinuierlichen Modus starten
    zes.Write(LMG, "INIT:CONT ON")
    
    try:
        print("Messung gestartet")
        while True:
            Werte = zes.Read(LMG)
            if Werte:
                values = Werte.split(",")
                print("n: {:.2f}".format(float(values[0])))
                print("M: {:.2f}".format(float(values[1])))
                print("Pmech: {:.2f}".format(float(values[2])))
                print("I: {:.2f}".format(float(values[3])))
                print("U: {:.2f}".format(float(values[4])))
                print("Pauf: {:.2f}".format(float(values[5])))
                print("eta: {:.2f}".format(float(values[6])))
                print("Temperatur: {:.2f}".format(float(values[7])))
                print("I_R_mess: {:.2f}".format(float(values[8])))
                print("U_R_mess: {:.2f}".format(float(values[9])))
                print("\n")
            else:
                print("Keine Messwerte")
            time.sleep(0.2)
    finally:
        zes.Write(LMG, "INIT:CONT OFF")
        closez.close(LMG)
        print("Messung beendet und Verbindung geschlossen.")

if __name__ == "__main__":
    main()
