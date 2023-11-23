import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar


df = pd.read_csv('accidents_2017.csv')

# Añado las columnas que necesito al dataset

# Añadimos columna con el año.
df['Year'] = 2017

# Añadimos columna nº de accidentes
df['n_accidentes']= 1
df.head(3)

len(df['Hour'].unique())

# Obtenemos los meses sin duplicados.
list(df['Month'].unique())
# ['October','September','December','July','May','June','January','April','March','November','February','August']

# Creamos un diccionario con mes (clave) - numero de mes (valor).
month_to_int = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

# Convertimos los nombres de los meses en números.
df['Month'].replace(month_to_int,inplace=True)

# Creamos una columna con el formato fecha que combina finlas hora, mes, dia y año.
df['Date']=pd.to_datetime(df[['Year', 'Month', 'Day']])

df.head(3)

# Borramos las columnas: hour, day, month, year, weekday
df.drop(['Hour','Day','Month','Year','Weekday'], axis=1, inplace=True)

df.head(3)

# Número de accidentes por meses
accidents_month = df.groupby(df['Date'].dt.month).count()

accidents_month.head(3)


# Número de accidentes por meses
accidents_month = df.groupby(df['Date'].dt.month).count()['Date']

# eje y
y_pos = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
accidents_month

################### GRÁFICO 1 ####################

plt.rcdefaults()


# Creación figura
fig = plt.figure(figsize=(15,6))

# Creación subplot dentro de la figura.
ax1 = fig.add_subplot(111)


# plot: accidentes por mes
grafico = ax1.barh(y_pos, 
                   accidents_month, 
                   align='center', 
                   color = 'lightblue',
                   alpha = 0.5)

# editamos colores de los meses con + nº de accidentes.
grafico[2].set_color('lightseagreen')
grafico[4].set_color('lightseagreen')
grafico[10].set_color('teal')

# invertimos etiquetas eje y (enero - diciembre)
ax1.invert_yaxis()

# Anotar números por cada mes y pintar valores + importantes.
for y,x in enumerate(accidents_month):
    if  y == 4 or y == 2:
        ax1.annotate(x, 
                     xy=(x+8,y),
                     va = 'center', 
                     fontstyle = 'italic', 
                     fontsize = 13,
                     color = '#ff0000')
        
    elif y == 10: 
        ax1.annotate(x, 
                     xy=(x+8,y),
                     va = 'center', 
                     fontstyle = 'italic', 
                     fontsize = 16 , 
                     color = '#ff0000')
    else:
        ax1.annotate(x, 
                     xy=(x+8,y),
                     va = 'center', 
                     fontstyle = 'italic',
                     fontsize = 11)

        
# Anotaciones adicionales        
mean = int(accidents_month.mean())
ax1.annotate(f"Media de accidentes\n en 2017",
             fontstyle = 'italic', 
             xy=(861, 'Febrero'),
             bbox=dict(boxstyle="round",fc="none", ec="teal"),
             xytext=(70, 39), 
             textcoords='offset points', 
             ha='center',
             arrowprops=dict(arrowstyle="->"))


ax1.annotate(f"$\mu$:\n{mean}",
             fontstyle = 'italic', 
             xy=(861, 12),
             xytext=(0, -26),
             textcoords='offset points', 
             ha='center',
             fontsize = 11,
             color = 'r')


ax1.axvline(mean, color = 'r', alpha = 0.45, linestyle ='--')

# modificamos spines (arriba y derecha)
ax1.spines['top'].set_alpha(0.0)
ax1.spines['right'].set_alpha(0.0)

# títulos
ax1.set_title('Accidentes en Barcelona en 2017\n(meses)', fontsize=18, weight= 'bold')
ax1.set_xlabel('Nº de accidentes',fontsize=15)



################## GRÁFICO 2 ###############
grouped_victims_df = df.groupby('Part of the day').sum()['n_accidentes']

labels = ['Tarde', 'Mañana', 'Noche']
colors = ['teal','mediumturquoise','azure']



# muestro el gráfico
plt.show()

################## GRÁFICO 2 ###############
grouped_victims_df = df.groupby('Part of the day').sum()['n_accidentes']

labels = ['Tarde', 'Mañana', 'Noche']
colors = ['teal','mediumturquoise','azure']

# Creación figura
fig2 = plt.figure(figsize=(15,10))

# Creación subplot dentro de la figura.
ax2 = fig2.add_subplot(211)


grouped_victims_df.name= 'Nº de accidentes'
# plot: accidentes por mes
grafico2 = ax2.pie(grouped_victims_df, 
                   labels = labels, 
                   textprops = dict(color ="black", fontsize = '14'),
                   explode= [0.07,0.04,0.001], 
                   shadow=True, 
                   autopct='%1.1f%%',
                   colors=colors, 
                   startangle=45, 
                   wedgeprops = {'edgecolor':'darkslategrey','linewidth': 1.5}, 
                   pctdistance= 0.6)

ax2.annotate(f"En 2017, casi el 50 % de los accidentes\nse produjeron por la tarde.",
             fontstyle = 'italic', 
             xy=(-0.19,0.16),
             bbox=dict(boxstyle="round",fc="none", ec="teal"),
             xytext=(-250, -80), 
             textcoords='offset points', 
             ha='center',
             fontsize=11,
             arrowprops=dict(arrowstyle="-|>"))


ax2.annotate(f"Fuente: https://opendata-ajuntament.barcelona.cat/es/",
             fontstyle = 'italic', 
             xy=(-1,-1),
             xytext=(370, -80), 
             textcoords='offset points', 
             ha='center',
             fontsize=11,
             weight= 'bold'
             )

plt.title('\n\n\nAccidentes en Barcelona en 2017\n(partes del día)', 
          fontsize=16, 
          weight= 'bold')

ax2.axis('equal')

#ax2.axvline(0, color = 'r', alpha = 0.85, linestyle =':')
plt.legend(loc = 'best', 
           fontsize = 14, 
           facecolor = 'aliceblue') 



# muestro el gráfico
plt.show()
