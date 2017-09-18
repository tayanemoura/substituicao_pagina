# -*- coding: utf-8 -*-
from random import randint

class PageReplacement:
	def __init__(self, frames):
		 self.frames = frames
		 self.pages = []
		 file = open('pages.txt')
		 self.pages = file.read().split('\n')
		 print self.pages 
		 self.random()

	def fifo(self):
		page_frames = [None]* frames
		print "fifo"	

	def lru(self):
		page_frames = [None]* frames
		print "LRU"

	def lfu(self):
		page_frames = [None]* frames
		print "LFU"

	def random(self):
		print "RANDOM"
		page_frames = [None]* frames
		print page_frames
		miss = 0
		hit = 0

		for page in self.pages:
			
			if(page in page_frames):
				print "hit"
				hit += 1
			else:
				i = self.free_space(page_frames)
				if (i != -1):
					page_frames[i] = page

				else:
					#numero aleatorio entre 0 e o numero total de frames
					i = randint(0,frames-1)
					print "random"
					print i 
					page_frames[i] = page

				print "miss"
				miss += 1

			print
			print page_frames
			print
		print "Miss: " + str(miss)
		print "Hit: " + str(hit)

		



	#retorna a posicao vazia se houver
	def free_space(self, page_frames):
		for i, frame in enumerate(page_frames):
			if frame is None:
				return i
		return -1



frames = input("Qual a capacidade total da memória?\n")


page = PageReplacement(frames)
