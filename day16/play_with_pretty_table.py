from prettytable import PrettyTable



table =PrettyTable()
table.add_column('Pokemon Names',['Charizard','Squirtle','Metapod'])
table.add_column('Type', ['Fire', 'Water', 'Bug'])
print(table)
table.align = 'l'
print(table.align)
print(table)