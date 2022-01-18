"""
This library is a combination of functions for latter use
Developer: Reza Ferdowsi
Start date: 2022-01-17
End date:
"""

def text_line_counter(File):
  "This function gets a text file and returns the number of lines in the file"
  with open(File) as text_doc:
    lines = 0
    for line in text_doc.readlines():
      lines += 1
    text_doc.close()
    return lines 
# Hosna_lines=text_line_counter("how_many_lines.txt")
# print(f"number of Hosna_lines are: {Hosna_lines}","\n__________________________") 

