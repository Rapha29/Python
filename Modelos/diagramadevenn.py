import matplotlib.pyplot as plt
from matplotlib_venn import venn2

a = 10
b = 10

# Criação do diagrama de Venn
venn = venn2(subsets=(a, b, a+b), set_labels=('Círculo A', 'Círculo B'))

# Configurações do diagrama
venn.get_label_by_id('10')
venn.get_label_by_id('10')

# Exibição do diagrama de Venn
plt.title('Diagrama de Venn - União de Círculos')
plt.show()