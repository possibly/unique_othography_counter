def orthography_count(string, split_char, replace_func=[]):
  for func in replace_func:
    string = func(string)

  orthographic_marks = string.split(split_char)
  unique_orthography = {}
  for mark in orthographic_marks:
    try:
      unique_orthography[mark] = unique_orthography[mark] + 1
    except:
      unique_orthography[mark] = 1

  return unique_orthography