#! /usr/bin/env python

#description: --------------------------------------------------------------------
#this antistress tool was born after using LegolasTheElf's Automatic saint invocation
#for depressed Veteran Unix Admins, called "mannaggia".
#Since it uses www.santiebeati.it to get today's saints and Google's text to speech
#for the voice part, basically it uses the cloud.
#But we think the cloud would be utter shit, if it only existed.
#This tool likes to be an off-the-(fucking-)cloud improved version of the original
#mannaggia.


#import --------------------------------------------------------------------------
import re, random, time, argparse, subprocess, os

#var -----------------------------------------------------------------------------
imprecazione = "Mannaggia" 	#the imprecation to be used as standard
dbfile = "santi_e_beati_utf8.txt"	#the santi e beati db

months = ["jan","feb","mar","apr","may","jun","jul","ago","sep","oct","nov","dec"]

for month in range(1,12+1):
	for day in range(1,31+1):
		today = str(day) + " " + months[month-1]
		#print today
		
		for line in open(dbfile):						#create the list with the santi of the date selected
			if today in line:
				santig = line
				break
		
		#santig = santig.decode("utf-8").encode("ascii","replace")
		
		santi = re.split('\:|\;', santig)
		del santi[0]
	
		#for santo in santi:
		for nsanto, santo in enumerate(santi):
			santo = santo.strip().replace(".","").replace(",","")
			print str(month).zfill(2) +"-"+ str(day).zfill(2) +" "+ str(nsanto+1).zfill(2) +" "+ santo
			
			mannaggia_fol = "wav_gtts/" + str(month).zfill(2) +"/"+ str(day).zfill(2)
			mannaggia_fil = mannaggia_fol +"/"+ str(nsanto+1).zfill(2) +" "+ santo + ".wav"
			
			if not os.path.isfile(mannaggia_fil):
				#mannaggia_cmd = 'pico2wave -w \"' + mannaggia_fil + '\" --lang=it-IT \"' + imprecazione +' '+ santo + '\"'
				#mannaggia_cmd = 'pico2wave -w mannaggia.wav --lang=\"it-IT\" \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && sox -v 0.9 mannaggia.wav -b 8 -r 16000 -c 1 \"' + mannaggia_fil + '\"'
				#mannaggia_cmd = 'pico2wave -w mannaggia.wav --lang=\"it-IT\" \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && lame --silent mannaggia.wav \"' + mannaggia_fil + '\"'
				
				#mannaggia_cmd = 'espeak -w mannaggia.wav -v it \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && sox -v 0.9 mannaggia.wav -b 8 -r 16000 -c 1 \"' + mannaggia_fil + '\"'
				#mannaggia_cmd = 'espeak -w mannaggia.wav -v it \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && lame --silent mannaggia.wav \"' + mannaggia_fil + '\"'
				
				#mannaggia_cmd = 'gtts-cli -l it -o mannaggia.mp3 \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && cp mannaggia.mp3 \"' + mannaggia_fil + '\"'
				mannaggia_cmd = 'gtts-cli -l it -o mannaggia.mp3 \"' + imprecazione +' '+ santo + '\" && mkdir -p \"' + mannaggia_fol + '\" && ffmpeg -i mannaggia.mp3 -acodec pcm_u8 -ar 16000 -ac 1 \"' + mannaggia_fil + '\"'
				
				
				#print mannaggia_cmd
				subprocess.call(mannaggia_cmd, shell=True) 		#send command to os

