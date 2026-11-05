import matplotlib.pyplot as plt
exp = [1400,600,300,410,250]
exp_label = ["homerent","Food", "phonebill", "Car", "other utilities"]
plt.pie(exp, labels = exp_label)
plt.axis("equal")

# to increase the size of chart.
# plt.pie(exp_label , labels = exp_label)
plt.pie(exp, labels = exp_label, autopct = "%0.1f%%", radius = 1.5, shadow= True, explode = [0,0,1,1,0], startangle = 45)
plt.show()





