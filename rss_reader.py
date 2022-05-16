import feedparser


def read_rss(site):

	f = feedparser.parse(site)
	for entry in f.entries:
		print(f"Data: {entry.published}\n\nTytuł: {entry.title}\n\nOpis: {entry.summary}\n\nLink: {entry.link}\n\n---------------------\n")


