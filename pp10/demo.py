denver = [1700000, 4600000, 2100000]

philly = []
philly.append(1800000)
philly.append(5000000)
philly.append(2500000)

print(denver)
print(philly)

total = [0, 0, 0]
total[0] = denver[0] + philly[0]
total[1] = denver[1] + philly[1]
total[2] = denver[2] + philly[2]
average = (total[0] + total[1] + total[2]) / len(total)
print("Produkcja w roku 2012 wyniosła", "{:,d}".format(total[0]).replace(",", " "), "sztuk")

print("Produkcja w roku 2013 wyniosła", "{:,d}".format(total[1]).replace(",", " "), "sztuk")

print("Produkcja w roku 2014 wyniosła", total[2], "sztuk")

print("Średnia wyniosła", average)