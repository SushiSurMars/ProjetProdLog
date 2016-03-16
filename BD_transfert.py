#https://github.com/Kawrantin/master-ProjetPython/blob/master/Code/GestionEquipement.py
import csv
#import mysql.connector
import sqlite3

class BD_Transfert:
    def __init__(self):
        self.connec = sqlite3.connect('ma_base.db')
        #con = mysql.connector.connect(host="infoweb",user="E145620H",password="E145620H",database="E145620H")
        
    def keskiya(self):
        cursor = self.connec.cursor()
        cursor.execute("""SELECT * FROM equipements""")
        ligne = cursor.fetchall()
        print(ligne)
        cursor.execute("""SELECT * FROM activites""")
        ligne = cursor.fetchall()
        print(ligne)

    def creation_table_equipements(self):
        cursor = self.connec.cursor()
        try:
            cursor.execute(""" CREATE TABLE IF NOT EXISTS equipements (ComInsee INTEGER,ComLib TEXT,InsNumInstall INTEGER,InstNom TEXT,EquipementId INTEGER,EquipNom TEXT, EquipNomBatiment TEXT)""")
    #création de la table ACTIVITES

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activites(
                    CodeINSEE INTEGER,
                    NomCommune TEXT,
                    NumeroFicheEquipement INTEGER,
                    NbEquipIdentique TEXT,
                    ActivCode INTERGER,
                    ActivLibel TEXT,
                    ActivPraticable BOOL,
                    ActivPratiquee BOOL,
                    SalleSpecial BOOL,
                    NivEffectPratiquer TEXT,
                    FOREIGN KEY (codeINSEE) REFERENCES installations(codeINSEE),
                    FOREIGN KEY (codeINSEE) REFERENCES equipements(ComINSEE),
                    FOREIGN KEY (NomCommune) REFERENCES installations(nomCommune),
                    FOREIGN KEY (NomCommune) REFERENCES equipements(ComLib)
                    )
                """)

        except:
            print ("ERROR: problème lors de la création de la table")
        else:
            self.connec.commit()
    

    def insert_equipement(self,ComInsee,ComLib,InsNumInstall,InstNom,EquipementId, EquipNom,EquipementNomBati):

        cursor = self.connec.cursor()
        try:
            cursor.execute("""
                INSERT INTO equipements(ComInsee,ComLib,InsNumInstall,InstNom,EquipementId, EquipNom,EquipNomBatiment) VALUES (?,?,?,?,?,?,?)""", (ComInsee,ComLib,InsNumInstall,InstNom,EquipementId, EquipNom,EquipementNomBati)
                )
        except:
            print("ERROR: problème lors de l'insertion de la ligne")
        
        self.connec.commit()

    def recup_fichier(self):
        try:
            with open('/hometu/etudiants/r/o/E145382Z/Téléchargements/info2/semestre4/prod_log/iutnantes/data.paysdelaloire.fr/data.paysdelaloire/equipements.csv','r') as f:
                reader = csv.reader(f)
                i = 0
                for row in reader:
                    try:
                        if(i> 1):
                            self.insert_equipement(int(row[0]),row[1],int(row[2]),row[3],int(row[4]),row[5],row[6])
                        i = i+1 
                        print(i)
                    except:
                        print("HELP US: ",i)
        except:
            print ("problème chargement fichier")
            
    def ajout_activites(self):
        with open('/hometu/etudiants/r/o/E145382Z/Téléchargements/info2/semestre4/prod_log/iutnantes/data.paysdelaloire.fr/data.paysdelaloire/23440003400026_J334_equipements_activites_table.csv','r') as file :
            spamreader = csv.reader(file, delimiter=',' , quotechar= '"' )
            i=0
            for row in spamreader :
                #if(i>30) : break
                #else :
                    user = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    self.cursor.execute("""INSERT INTO activites 
                    (CodeINSEE,
                    NomCommune,
                    NumeroFicheEquipement,
                    NbEquipIdentique,
                    ActivCode,
                    ActivLibel,
                    ActivPraticable,
                    ActivPratiquee,
                    SalleSpecial,
                    NivEffectPratiquer) 
                    VALUES(?,?,?,?,?,?,?,?,?,?)""", user)
                    i+=1
                    print(i)
        self.connec.commit()
    
        
bd = BD_Transfert()
bd.creation_table_equipements()
bd.recup_fichier()
bd.ajout_activites()
bd.keskiya()

"""         FOREIGN KEY (ComInsee) REFERENCES activites(CodeInsee)
            FOREIGN KEY (ComLib) REFERENCES activites(NomCommune)
            FOREIGN KEY (InsNumInstall) REFERENCES installations(numeroInstall)"""
