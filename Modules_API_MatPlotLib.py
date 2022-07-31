import matplotlib.pyplot as plt



names = ["Cancer cell", "Immune cell", "Blood cell", "Cardiac cell", "Liver cell"]
values = [86, 43, 78, 101, 281]

'''
plt.bar(names, values)

plt.title("Hate Crimes Reported in SD County (per year), Total = " + str(sum(values)))
plt.ylabel('Hate crimes reported')
plt.xlabel('Year')

plt.savefig('bar.png')
plt.show()

print("Done! If bar.png doesn't update on Repl.it, delete it and run program again")
'''

'''
plt.plot(names, values, "r--")
#other data format values for dot plots:
#ro = red circle, r-- = red dashes,
# bs = blue squares, g^ = green triangles

plt.title("Hate Crimes Reported in SD County (per year), Total = " + str(sum(values)))
plt.ylabel('Hate crimes reported')
plt.xlabel('Year')

plt.savefig('dotplot.png')
plt.show()

print("Done! If dotplot.png doesn't update on Repl.it, delete it and run program ]again")
'''


plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1) #numrows, numcols, plot_number
plt.bar(names, values)

plt.subplot(1, 3, 2)
plt.scatter(names, values)

plt.subplot(1, 3, 3)
plt.plot(names, values)

plt.suptitle("[3 ways] Levels of protein in cell type sample (nM), Total protein = " + str(sum(values)))

plt.savefig('multi-plot.png')

print("Done! If multi-plot.png doesn't update on Repl.it, delete it and run program again")
