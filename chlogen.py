#!/usr/bin/python

import feedparser
import os,sys

print 'Welcome to Chlogen Podcast Player'
print ''
print 'd - Developes\' Life Podcast'
print 'h - Hanselman Minutes Podcast'
print 't - Teach Me to Code Podcast'
print 's - Software Engineering Radio'
print 'g - Google Developer Podcast'
print 'f - FLOSS Weekly Podcast (Audio)'
print 'v - FLOSS Weekly Podcast (Video)'
print 'r - Drunkandretired Podcast'
print 'j - Javaposse Podcast'
print 'q - Quit'
print ''


pod_select = raw_input()
d = ''
if pod_select == 'd':
	d = feedparser.parse('http://feeds.feedburner.com/ThisDevelopersLife')
if pod_select == 'h':
	d = feedparser.parse('http://feeds.feedburner.com/HanselminutesCompleteMP3')
if pod_select == 't':
	d = feedparser.parse('http://feeds.feedburner.com/railscoach')
if pod_select == 's':
	d = feedparser.parse('http://feeds.feedburner.com/se-radio')
if pod_select == 'g':
	d = feedparser.parse('http://feeds.feedburner.com/GoogleDeveloperPodcast')
if pod_select == 'f':
	d = feedparser.parse('http://leoville.tv/podcasts/floss.xml')
if pod_select == 'r':
	d = feedparser.parse('http://feeds.feedburner.com/cote')
if pod_select == 'j':
	d = feedparser.parse('http://feeds.feedburner.com/javaposse')
if pod_select == 'v':
	d = feedparser.parse('http://feeds.twit.tv/floss_video_small')
if pod_select == 'q':
	sys.exit(0)
	

print d['feed']['title']
print d.feed.subtitle
print d.channel.description
print ''
print d.feed.link
print ''

links_list = []
i = 0
for entry in d['entries']:
	links_list.append(d['entries'][i].links[1].href)
	print i,')', d['entries'][i]['title'], '\n', d['entries'][i].links[1].href
	i += 1

print ''	
print 'Press the corresponding number to listen to the podcast.'
print 'Press Enter to Quit.'
print ''
try:
	pod_choice = raw_input('Podcast: ')
	download = raw_input('Download: (Y/N) ')
	if download == 'N':
		choice = str(links_list[int(pod_choice)])
		os.system('vlc %s' % choice)
	if download == 'Y':
		choice = str(links_list[int(pod_choice)])
		os.system('wget %s' % choice)
	else:
		print 'Invalid Input'
except ValueError:
	sys.exit(0)
