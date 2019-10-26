# .splitlines() => her bir satırdali elemanların arasına [,] ekler

# not : 


metin = """bilge
adam
beşiktaş
python
dersleri
"""

sonuc = metin.splitlines(True) # True ibaresi eklersek, \n karakterini ekler
print(sonuc)

# ['bilge', 'adam', 'beşiktaş', 'python', 'dersleri']
# ['bilge\n', 'adam\n', 'beşiktaş\n', 'python\n', 'dersleri\n']