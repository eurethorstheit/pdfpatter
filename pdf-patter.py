#!/usr/bin/python
# coding: utf8

from Tkinter import *
import sys, os
import subprocess
from subprocess import Popen

from tkFileDialog import askopenfilename
from string import Template

bashdatei = '~/Dokumente/Programmierung/Python/Zuschneiden/bashbash.sh'

def ende():
	t="./bashbash.sh ende "+ nav.pfad
	subprocess.call(t , shell=True)
	exit()

def datei_oeffnen():
	t="./bashbash.sh ende "+ nav.pfad
	subprocess.call(t , shell=True)
	
	nav.pfad=askopenfilename()		
	PFAD= []
	PFAD=nav.pfad.split("/")	
	nav.pfad_ordner=""	
	x=0
	while x <= (len(PFAD)-2) :
		nav.pfad_ordner += PFAD[x]+"/"	
		x += 1
	print nav.pfad_ordner	
	t="./bashbash.sh pfad "+ nav.pfad
	subprocess.call(t , shell=True)
	
def datei_rotation():
	t="./bashbash.sh rotation "+ nav.pfad 
	subprocess.call(t , shell=True)

def starte_cut():
	#Variablenübergabe und Test ob Leer	
	links=nav.eingabe_links.get()
	if not links:
		links="0"	
	rechts=nav.eingabe_rechts.get()
	if not rechts:
		rechts="0"	
	unten=nav.eingabe_unten.get()
	if not unten:
		unten="0"	
	oben=nav.eingabe_oben.get()
	if not oben:
		oben="0"	
	#Testen, ob leere Variable - funktioniert nicht
#	LeerTest = [links,rechts,unten,oben]
#	for pos in LeerTest:		
#		if not pos:			
#			pos="0" 
	t="./bashbash.sh schneiden "+ nav.pfad +" "+links+" "+unten+" "+rechts+" "+oben	
	subprocess.call(t , shell=True)
	
def starte_zerlegen():
	#Variablenübergabe und Test ob Leer	
	zerlegen_start=nav.eingabe_zerlegen_start.get()
	if not zerlegen_start:
		print "Start fehlt"
	zerlegen_ende=nav.eingabe_zerlegen_ende.get()
	if not zerlegen_ende:
		print "Ende fehlt"
	zerlegen_dateiname=nav.eingabe_zerlegen_dateiname.get()
	if not zerlegen_dateiname:
		print "Dateiname fehlt"
	Popen(["pdftk",nav.pfad,"cat",zerlegen_start+"-"+zerlegen_ende,"output",zerlegen_dateiname])
#Ladevorgang=subprocess.Popen(["wget","-O","Video_Royal.mp4",Video[(int(Auswahl)-1)]])
def cut_bestaetigen():
	nav.eingabe_links.delete(0,END)
	nav.eingabe_rechts.delete(0,END)
	nav.eingabe_unten.delete(0,END)
	nav.eingabe_oben.delete(0,END)
	nav.eingabe_links.focus_set()
def starte_undo():
	t="./bashbash.sh undo "+ nav.pfad
	subprocess.call(t , shell=True)

def starte_sortieren():
	t="./bashbash.sh sortieren "+ nav.pfad+" "+nav.pfad_ordner+"links.pdf"+" "+nav.pfad_ordner+"rechts.pdf"
	subprocess.call(t , shell=True)

def starte_scale():
	skala=nav.eingabe_scale.get()		
	t="./bashbash.sh scale "+ nav.pfad+" "+skala
	subprocess.call(t , shell=True)

def menu_seite_weg():	
	if nav.boolean_seite_weg == False:
		nav.seite_weg()
		nav.boolean_seite_weg = True
		nav.b_menu_seite_weg.config(text='Seite löschen')
		nav.eingabe_seite_weg.focus_set()
	else:
		nav.seite_weg.destroy()
		del nav.seite_weg
		nav.boolean_seite_weg = False

def menu_zerlegen():	
	if nav.boolean_zerlegen == False:
		nav.zerlegen()
		nav.boolean_zerlegen = True
		nav.b_menu_zerlegen.config(text='Zerlegen')
		nav.zerlegen.focus_set()
	else:
		nav.zerlegen.destroy()
		del nav.zerlegen
		nav.boolean_zerlegen = False



def menu_speichern():	
	print nav.boolean_speichern
	if nav.boolean_speichern == False:
		nav.speichern()
		nav.boolean_speichern = True
		nav.b_menu_speichern.config(text='Datei speichern')
		nav.eingabe_dateiname.focus_set()
	else:
		nav.speichern.destroy()
		del nav.speichern
		nav.boolean_speichern = False

def starte_speichern():
	datei=nav.eingabe_dateiname.get()		
	pfad_datei_speichern=nav.pfad_ordner+datei
	t="./bashbash.sh fertig "+ nav.pfad+" "+pfad_datei_speichern
	subprocess.call(t , shell=True)
	menu_speichern()

def starte_seite_weg():
	seite=nav.eingabe_seite_weg.get()		
	t="./bashbash.sh seite_weg "+ nav.pfad+" "+seite
	subprocess.call(t , shell=True)
	menu_seite_weg()

def starte_rotation(rot):
	print rot	
	t="./bashbash.sh rotation "+ nav.pfad+" "+rot
	subprocess.call(t , shell=True)

def starte_test(was):
	if was == "bearbeiten":	
		t="./bashbash.sh bookmarks "+ nav.pfad+" "+was+" "+nav.pfad_ordner+"bookmarks.info"
		subprocess.call(t , shell=True)
	elif was == "vorbereiten":	
		t="./bashbash.sh bookmarks "+ nav.pfad+" "+was+" "+nav.pfad_ordner+"bookmarks.info"+" "+nav.pfad_ordner+"pdfmarks"
		subprocess.call(t , shell=True)
	elif was == "bookmarken":	
		t="./bashbash.sh bookmarks "+nav.pfad+" "+was+" "+nav.pfad_ordner+"pdfmarks"+" "+nav.pfad+"_bookmarked"
		subprocess.call(t , shell=True)
		
	else:	
		print "Ficken"

def menu_cut():
	if nav.boolean_cut == False:
		nav.cut()
		nav.boolean_cut = True
		nav.b_menu_zuschneiden.config(text='Zuschneiden schließen')
		nav.eingabe_links.focus_set()
		t="./bashbash.sh seite_mitte "+ nav.pfad
		subprocess.call(t , shell=True)
		
	else:
		nav.cut.destroy()
		del nav.cut
		nav.boolean_cut = False
		nav.b_menu_zuschneiden.config(text='Zuschneiden öffnen')

def menu_scale():
	if nav.boolean_scale == False:
		nav.scale()
		nav.boolean_scale = True
		nav.b_menu_scale.config(text='Skalieren schließen')
		nav.eingabe_scale.focus_set()
	else:
		nav.scale.destroy()
		del nav.scale
		nav.boolean_scale = False
		nav.b_menu_scale.config(text='Skalieren öffnen')
def menu_rotation():
	if nav.boolean_rotation == False:
		nav.rotation()
		nav.boolean_rotation = True
	#	nav.b_menu_rotation.config(text='Menu Rotation schließen')
	else:
		nav.rotation.destroy()
		del nav.rotation
		nav.boolean_rotation = False
	#	nav.b_menu_rotation.config(text='Menu Rotation öffnen')
def menu_bookmarks():
	if nav.boolean_bookmarks == False:
		nav.bookmarks()
		nav.boolean_bookmarks = True
	else:
		nav.bookmarks.destroy()
		del nav.bookmarks
		nav.boolean_bookmarks = False


		
class NAVIGATION(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.pfad='/home/Dokumente'	
		self.pfad_ordner='/home/Dokumente'		
		self.boolean_cut=False	
		self.boolean_scale=False
		self.boolean_speichern=False
		self.boolean_rotation=False
		self.boolean_bookmarks=False
		self.boolean_seite_weg=False
		self.boolean_zerlegen=False

	def menu(self):	
		self.menu = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.menu.pack(side=TOP,fill=X, expand=YES)       
		self.menu1 = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.menu1.pack(side=TOP,fill=X, expand=YES)       
				
		self.funktionen = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.funktionen.pack()       
		
#-------------------MENU##################
		self.b_datei=Button(master=self.menu,text="Datei wählen", command=datei_oeffnen, padx=10, pady=5).pack()
		self.b_menu_speichern=Button(master=self.menu,text="Datei speichern", command=lambda:menu_speichern(), padx=10, pady=5)
		self.b_menu_speichern.pack()
		self.b_ende=Button(master=self.menu,text="Programm Beenden", command=ende, padx=10, pady=5).pack()
		self.b_menu_zuschneiden=Button(master=self.menu1,text="Zuschneiden öffnen", command=lambda:menu_cut(), padx=10, pady=5)
		self.b_menu_zuschneiden.pack()
		self.b_menu_scale=Button(master=self.menu1,text="Skalieren öffnen", command=lambda:menu_scale(), padx=10, pady=5)
		self.b_menu_scale.pack()
		self.b_menu_seite_weg=Button(master=self.menu1,text="Seite löschen", command=lambda:menu_seite_weg(), padx=10, pady=5)
		self.b_menu_seite_weg.pack()
		self.b_menu_zerlegen=Button(master=self.menu1,text="Datei zerlegen", command=lambda:menu_zerlegen(), padx=10, pady=5)
		self.b_menu_zerlegen.pack()
						
		#-------------------MENU##################
		#-------------------MENU1##################
		self.b_menu_rotation=Button(master=self.menu1,text="Menu Rotieren", command=lambda:menu_rotation(), padx=10, pady=5).pack()
		self.b_menu_bookmarks=Button(master=self.menu1,text="Menu Bookmarks", command=lambda:menu_bookmarks(), padx=10, pady=5).pack()
		#-------------------MENU1##################		
#-------------------FUNKTIONEN##################
		self.b_undo=Button(master=self.funktionen,text="UNDO", command=starte_undo, padx=10, pady=5).pack()		
		self.b_sortieren=Button(master=self.funktionen,text="Sortieren", command=starte_sortieren, padx=10, pady=5).pack()						
#-------------------FUNKTIONEN##################
		self.mainloop()	


	def bookmarks(self):
		self.bookmarks = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.bookmarks.pack()       				
		self.b_bearbeiten=Button(master=self.bookmarks,text="Bookmarks bearbeiten", command=lambda:starte_test("bearbeiten"), padx=10, pady=5).pack()
		self.b_vorbereiten=Button(master=self.bookmarks,text="Bookmarks vorbereiten", command=lambda:starte_test("vorbereiten"), padx=10, pady=5).pack()
		self.b_bookmarken=Button(master=self.bookmarks,text="Bookmarks einfügen", command=lambda:starte_test("bookmarken"), padx=10, pady=5).pack()
	def rotation(self):
		self.rotation = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.rotation.pack()       
				
		self.b_rot_rechts=Button(master=self.rotation,text="Rechts herum", command=lambda:starte_rotation("rechts"), padx=10, pady=5).pack()
		self.b_rot_link=Button(master=self.rotation,text="Links herum", command=lambda:starte_rotation("links"), padx=10, pady=5).pack()
		self.b_rot_invert=Button(master=self.rotation,text="180 Grad", command=lambda:starte_rotation("invert"), padx=10, pady=5).pack()

	def speichern(self):
		self.speichern = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.speichern.pack()       
				
		self.eingabe_dateiname = Entry(master=self.speichern,background='grey',foreground='blue',font='courier')
		self.eingabe_dateiname.pack()
		self.b_speichern=Button(master=self.speichern,text="Datei speichern", command=starte_speichern, padx=10, pady=5).pack()


	def zerlegen(self):
		self.zerlegen = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.zerlegen.pack()       				
		self.eingabe_label = Label(master=self.zerlegen,text="Startseite").pack(side=TOP)		
		self.eingabe_zerlegen_start = Entry(master=self.zerlegen,background='grey',foreground='blue',font='courier')
		self.eingabe_zerlegen_start.pack()
		self.eingabe_label = Label(master=self.zerlegen,text="Endseite").pack(side=TOP)		
		self.eingabe_zerlegen_ende = Entry(master=self.zerlegen,background='grey',foreground='blue',font='courier')
		self.eingabe_zerlegen_ende.pack()
		self.eingabe_label = Label(master=self.zerlegen,text="Dateiname").pack(side=TOP)		
		self.eingabe_zerlegen_dateiname = Entry(master=self.zerlegen,background='grey',foreground='blue',font='courier')
		self.eingabe_zerlegen_dateiname.pack()

		self.b_zerlegen=Button(master=self.zerlegen,text="PDF zerlegen", command=starte_zerlegen, padx=10, pady=5)
		self.b_zerlegen.pack()

	def seite_weg(self):
		self.seite_weg = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.seite_weg.pack()       
				
		self.eingabe_seite_weg = Entry(master=self.seite_weg,background='grey',foreground='blue',font='courier')
		self.eingabe_seite_weg.pack()
		self.b_seite_weg=Button(master=self.seite_weg,text="Seite löschen", command=starte_seite_weg, padx=10, pady=5).pack()
		
	def scale(self):
		self.scale = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.scale.pack()       
		self.eingabe_scale = Entry(master=self.scale,background='grey',foreground='blue',font='courier')
		self.eingabe_scale.pack()
		self.b_scale=Button(master=self.scale,text="Datei skalieren", command=starte_scale, padx=10, pady=5).pack()									
		
	def cut(self):

		self.cut = Frame(self,relief=RIDGE, bd=6,width = '30', height = '5c')
		self.cut.pack()       
#-------------------SCHNEIDEN##################
		self.info_label = Label(master=self.cut,text="Info")
		self.info_label.pack(side=TOP)		
		self.eingabe_label = Label(master=self.cut,text="Links").pack(side=TOP)		
		self.eingabe_links = Entry(master=self.cut,background='grey',foreground='blue',font='courier')
		self.eingabe_links.pack(side=TOP)	
		self.eingabe_label = Label(master=self.cut,text="Rechts").pack(side=TOP)
		self.eingabe_rechts = Entry(master=self.cut,background='grey',foreground='blue',font='courier')
		self.eingabe_rechts.pack(side=TOP)
		self.eingabe_label = Label(master=self.cut,text="Oben").pack(side=TOP)
		self.eingabe_oben = Entry(master=self.cut,background='grey',foreground='blue',font='courier')
		self.eingabe_oben.pack(side=TOP)
		self.eingabe_label = Label(master=self.cut,text="Unten").pack(fill=X)
		self.eingabe_unten = Entry(master=self.cut,background='grey',foreground='blue',font='courier')
		self.eingabe_unten.pack(fill='x')
		self.b_cut=Button(master=self.cut, text="Zuschneiden", command=starte_cut, padx=10, pady=5).pack()		
		self.b_cut_bestaetigen=Button(master=self.cut, text="Neue Eingabe", command=cut_bestaetigen, padx=10, pady=5).pack()		
#-------------------SCHNEIDEN##################		
	



nav = NAVIGATION()

def main():
	nav.title('PDFs bearbeiten')
	nav.menu()	

if __name__ == "__main__":
    main()






