from util import orthography_count
from songs import songs

replace_functions = [
  lambda string: string.replace('\n', ' '),
  lambda string: string.replace('(', ''),
  lambda string: string.replace(')', ''),
  lambda string: string.replace(',', ''),
  lambda string: string.replace("'", ''),
  lambda string: string.replace('  ', ' '),
  lambda string: string.lower()
]

def _unique_orthographic_marks_by_song():
  unique_orthography_count = {}
  for title, lyrics in songs.iteritems():
    unique_orthography_count[title] = orthography_count(lyrics, ' ', replace_functions)
  return unique_orthography_count

def print_orthography_seperate():
  unique_orthography_count = _unique_orthographic_marks_by_song()
  for title, count in unique_orthography_count.iteritems():
    print '\n\n'+title + '\n\n'
    for mark, num in count.iteritems():
      print "{}: {}".format(mark, num)

def print_shared_marks(in_atleast_this_many_songs=2, appears_atleast_this_many_times=5):
  unique_orthography_count = _unique_orthographic_marks_by_song()
  unique_total = {}
  for title, count in unique_orthography_count.iteritems():
    for mark, num in count.iteritems():
      try:
        unique_total[mark]['appearances'] += 1
        if all([not t == title for t in unique_total[mark]['in songs']]):
          unique_total[mark]['in songs'] += [title]
      except:
        unique_total[mark] = {'appearances': num, 'in songs': [title]}
  for mark, stats in unique_total.iteritems():
    appearances, in_songs = stats.values()
    if len(in_songs) >= in_atleast_this_many_songs and appearances >= appears_atleast_this_many_times:
      print "{}: Appears: {}, In songs: {}".format(mark, appearances, map(lambda x: x[:10], in_songs))

print_shared_marks()