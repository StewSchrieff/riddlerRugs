import seaborn as sns
# sns.set()
import matplotlib.pyplot as plt
import pandas as pd
import warnings
from scipy import stats
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")


df = pd.read_csv('rugs.csv', header=None, names=['rugs', '1x4', '2x4', '3x4', '4x4'])
# print df
# df = pd.DataFrame(df, columns = ['rugs', '1x4','2x4', '3x4', '4x4'])


# ax = sns.regplot(x=df['rugs'], y=df['1x4'], fit_reg=True)
# ax = sns.regplot(x=df['rugs'], y=df['2x4'], fit_reg=True)
# ax = sns.regplot(x=df['rugs'], y=df['3x4'], fit_reg=True)
ax = sns.regplot(x=df['rugs'], y=df['4x4'], fit_reg=True)
# print(ax.get_lines()[0].get_ydata())

slope, intercept, r_value, p_value, std_err = stats.linregress(ax.get_lines()[0].get_xdata(), ax.get_lines()[0].get_ydata())
# ax = sns.regplot(data=df, x=df['rugs'])
# ax.set(yscale="log")
# print(df)
plt.show()




print('slope: ' + str(slope))
print('intercept: ' + str(intercept))


rugsPerGrid = 1 / slope
print('rugs Per 4x4 Grid: ' + str(rugsPerGrid))


