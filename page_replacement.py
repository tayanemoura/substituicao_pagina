# -*- coding: utf-8 -*-
from random import randint

class PageReplacement:
	def __init__(self, frames):
		 self.frames = frames
		 self.pages = []
		 file = open("pages.txt")
		 self.pages = file.read().split('\n')
		 print self.pages
		 self.fifo()		 
		 self.random()
		 self.lru()
		 self.lfu()
		 
	def fifo(self):
		print "\n", "\t", "\t", "ALGORITMO FIFO"
		print "-------------------------------------------------------"
		page_frames = [None]* frames

		#fila auxiliar
		queue = [None] * frames
		miss = 0
		hit = 0
		troca=0
		per_miss = 0
		per_hit = 0

		for page in self.pages:
			
			if(page in page_frames):
				print "JA EXISTE","\t",page,"\t","NA PAGINA: ","\t",page_frames
				hit += 1
			else:
				i = self.free_space(page_frames)
				if (i != -1):
					page_frames[i] = page
					queue.pop(0)
					queue.append(page)
					print "ACRESCENTANDO:","\t",page,"\t",'NA PAGINA: ',"\t",page_frames
				else:
								
					i = page_frames.index(queue[0])
					troca = page_frames[i]
					page_frames[i] = page
					queue.pop(0)
					queue.append(page)


					print "TROCANDO","\t",troca,"POR",page,'NA PAGINA: ', "\t", page_frames			
				miss+=1

		#cálculos
		per_miss = str("{0:.2f}".format(100 * float(miss) / float(len(self.pages)))) + " %"
		per_hit = str("{0:.2f}".format(100 * float(hit) / float(len(self.pages)))) + " %"
		
		print "\n"
		print "TOTAL DE MISS: " + str(miss), " - ", per_miss
		print "TOTAL DE HIT: " + str(hit), " - " , per_hit
		print "\n"

	def lru(self):
		print "\n", "\t", "\t", "ALGORITMO LRU"
		print "-------------------------------------------------------"
		page_frames = [None]* frames
		
		#fila auxiliar para guardar a ordem que entraram
		queue = [None] * frames

		miss = 0
		hit = 0
		troca=0
		per_miss = 0
		per_hit = 0
		
		for page in self.pages:
			
			if(page in page_frames):
				print "JA EXISTE","\t",page,"\t","NA PAGINA: ","\t",page_frames
				hit += 1
				queue.pop(queue.index(page))
				queue.append(page)
			else:
				i = self.free_space(page_frames)
				if (i != -1):
					page_frames[i] = page
					queue.pop(0)
					queue.append(page)
					print "ACRESCENTANDO:","\t",page,"\t",'NA PAGINA: ',"\t",page_frames
				else:
								
					i = page_frames.index(queue[0])
					troca = page_frames[i]
					page_frames[i] = page
					queue.pop(0)
					queue.append(page)

					print "TROCANDO","\t",troca,"POR",page,'NA PAGINA: ', "\t", page_frames			
				miss+=1

		#cálculos
		per_miss = str("{0:.2f}".format(100 * float(miss) / float(len(self.pages)))) + " %"
		per_hit = str("{0:.2f}".format(100 * float(hit) / float(len(self.pages)))) + " %"
		
		print "\n"
		print "TOTAL DE MISS: " + str(miss), " - ", per_miss
		print "TOTAL DE HIT: " + str(hit), " - " , per_hit
		print "\n"


	def lfu(self):
		print "\n", "\t", "\t", "ALGORITMO LFU"
		print "-------------------------------------------------------"
		page_frames = [None]* frames

		#fila auxiliar para guardar a ordem que entraram
		queue = [None] * frames
		#dict que guarda frequencia dos que estao na fila auxiliar
		frequency = {}

		miss = 0
		hit = 0
		troca=0
		per_miss = 0
		per_hit = 0

		victim = ""

		for page in self.pages:
			
			if(page in page_frames):
				print "JA EXISTE","\t",page,"\t","NA PAGINA: ","\t",page_frames
				hit += 1
				if page in frequency:
					frequency[page] += 1
				else:
					frequency[page] = 1
			else:
				i = self.free_space(page_frames)
				if (i != -1):
					page_frames[i] = page
					queue.pop(0)
					queue.append(page)
					if page in frequency:
						frequency[page] += 1
					else:
						frequency[page] = 1
					print "ACRESCENTANDO:","\t",page,"\t",'NA PAGINA: ',"\t",page_frames
				else:
					#primeiro verifica-se o com menor frequencia
					least = self.least_frequently(frequency)

					if(len(least)==1):
						victim = least[0]
					else:
						#se tiver mais de um, fifo:

						#verificar, dos que estão na lista dos menor frequencia qual aparece primeiro na fila
						victim = self.first_of_least(queue, least)

					i = page_frames.index(victim)
					troca = page_frames[i]
					page_frames[i] = page
					#atualiza dicionario de frequencia
					frequency[page] = 1
					frequency.pop(victim)

					#atualiza fila
					queue.pop(queue.index(victim))
					queue.append(page)

					print "TROCANDO","\t",troca,"POR",page,'NA PAGINA: ', "\t", page_frames			
				miss+=1
		#cálculos
		per_miss = str("{0:.2f}".format(100 * float(miss) / float(len(self.pages)))) + " %"
		per_hit = str("{0:.2f}".format(100 * float(hit) / float(len(self.pages)))) + " %"
		
		print "\n"
		print "TOTAL DE MISS: " + str(miss), " - ", per_miss
		print "TOTAL DE HIT: " + str(hit), " - " , per_hit
		print "\n"

	def random(self):
		print "\n", "\t", "\t", "ALGORITMO RANDOM"
		print "-------------------------------------------------------"
		page_frames = [None]* frames
		print page_frames
		miss = 0
		hit = 0
		troca = 0
		per_miss = 0
		per_hit = 0

		for page in self.pages:
			
			if(page in page_frames):
				print "JA EXISTE","\t",page,"\t","NA PAGINA: ","\t",page_frames
				hit += 1
			else:
				i = self.free_space(page_frames)
				if (i != -1):
					page_frames[i] = page
					print "ACRESCENTANDO:","\t",page,"\t",'NA PAGINA: ',"\t",page_frames

				else:
					#numero aleatorio entre 0 e o numero total de frames
					i = randint(0,frames-1)
					troca = page_frames[i]				
					page_frames[i] = page
					print "TROCANDO","\t",troca,"POR",page,'NA PAGINA: ', "\t", page_frames
				miss += 1
			
		#cálculos
		per_miss = str("{0:.2f}".format(100 * float(miss) / float(len(self.pages)))) + " %"
		per_hit = str("{0:.2f}".format(100 * float(hit) / float(len(self.pages)))) + " %"
		
		print "\n"
		print "TOTAL DE MISS: " + str(miss), " - ", per_miss
		print "TOTAL DE HIT: " + str(hit), " - " , per_hit
		print "\n"
		
	
	#retorna a posicao vazia se houver
	def free_space(self, page_frames):
		for i, frame in enumerate(page_frames):
			if frame is None:
				return i
		return -1

	def least_frequently(self, frequency):
		#pode ter mais de um com a mesma frequencia menor
		list_least = []
		least = frequency[frequency.keys()[0]]
		for key, value in frequency.iteritems():
			if value <= least:
				least = value
		for key, value in frequency.iteritems():
			if value <= least:
				list_least.append(key)

		return list_least

	def first_of_least(self, queue, least):
		for q in queue:
			if q in least:
				return q		


	print "\n "
	print " SIMULADOR DE TROCA DE PAGINA:"
		
frames = input("Qual a capacidade total da memoria?\n")
#caminho = input ("Qual o caminho do arquivo?\n")


page = PageReplacement(frames)