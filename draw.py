import matplotlib.pyplot as plt

def Draw(x, y, xlabel, ylabel, name=''):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y, color = 'green')
    plt.grid(True, linestyle = "--", color = 'gray', linewidth = '0.5', axis='y')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks()
    plt.title(name)
    plt.savefig(name + '.png', dpi=100)
    plt.close('all')