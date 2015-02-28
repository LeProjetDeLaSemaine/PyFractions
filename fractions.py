#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Que le codeur qui lit ceci soit à jamais ébloui par le spectacle du bordel ambiant dans ce fichier ;)

# Méthodes utiles :
def pgcd(a,b):
	while b>0:
		a, b = b, a%b
	return a
	
def ppcm(a, b):
	if (a==0) or (b==0): #On évite ainsi trop de récursions. Voici un magnifique exemple d'une belle qualité du programmeur : la flemme !
		return 0
	else:
		return (a*b)//pgcd(a,b)
		
def intToFraction(x):
	return Fraction(*float(x).as_integer_ratio()) #Quelle belle ligne ! C'est pratique et lisible
		
def mettreAuMemeDenominateur(a, b):
	if type(a) != Fraction or type(b) != Fraction:
		return None
	nouveauDen = ppcm(a.denominateur, b.denominateur)
	a.numerateur = a.numerateur*(nouveauDen/a.denominateur)
	b.numerateur = b.numerateur*(nouveauDen/b.denominateur)
	a.denominateur = b.denominateur = nouveauDen
	return a, b
	
# Classe Fraction (le nom est assez explicite non ?)
class Fraction(object):
	def __init__(self, num=1, den=1):
		if type(num) == str:
			num, den = num.split('/')
		self.numerateur, self.denominateur = int(num), int(den)
		self = self.reduire()
		
	def reduire(self): #Obtention de la forme irréductible
		d = pgcd(self.numerateur, self.denominateur)
		self.numerateur /= d
		self.denominateur /= d
		return self
		
	def __repr__(self): #Représentation sous forme de str d'un objet Fraction
		return str(int(self.numerateur)) + '/' + str(int(self.denominateur))
		
	def __neg__(self): #Overload en cas de préfixe - devant l'objet
		return Fraction(-self.numerateur, self.denominateur)
		
	def __add__(self, terme): #Overload de l'opérateur +
		if type(terme) != Fraction:
			terme = Fraction(terme)
		self, terme = mettreAuMemeDenominateur(self, terme)
		self.numerateur += terme.numerateur
		return self
		
	def __radd__(self, terme):
		return self + terme
	
	def __sub__(self, terme): #Overload de l'opérateur -
		if type(terme) != Fraction:
			terme = Fraction(terme)
		self, terme = mettreAuMemeDenominateur(self, terme)
		self.numerateur -= terme.numerateur
		return self
		
	def __rsub__(self, terme):
		return terme + (-self)
	
	def __mul__(self, facteur): #Overload de l'opérateur *
		if type(facteur) != Fraction:
			self.numerateur *= facteur
		else:
			self.numerateur *= facteur.numerateur 
			self.denominateur *= facteur.denominateur
		return self
		
	def __rmul__(self, terme):
		return self*terme
		
	def __truediv__(self, div): #Overload de l'opérateur /
		if type(div) != Fraction:
			self.denominateur *= div
		else:
			self.numerateur *= div.denominateur
			self.denominateur *= div.numerateur
		return self
		
	def __rtruediv__(self, div):
		return div*self.inverse()
		
	def __pow__(self, puissance): #Overload de l'opérateur **
		if type(puissance) != Fraction:
			self.numerateur **= puissance
			self.denominateur **= puissance
		else:
			print("Pas encore implémenté") #La flemme je vous dis ! C'est Noël non mais !
		return self
		
	def inverse(self): #Obtention de l'inverse de la fraction
		return Fraction(self.denominateur, self.numerateur)
		
	def valeurExacte(self): #Obtention de la valeur exacte de la fraction
		return float(self.numerateur/self.denominateur)
		
	def __eq__(self, autre):
		if type(autre) != Fraction:
			autre = Fraction(autre)
		return (True if self.numerateur*autre.denominateur==self.denominateur*autre.numerateur else False)
		
#Exemples :
a = Fraction(1, 2)
b = Fraction('2/1')
