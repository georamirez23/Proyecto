#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
archivo_excel = pd.read_excel('ventas.xlsx', sheet_name='Ventas2019')


# In[23]:


columnas = ['Fecha', 'Codigo', 'Cliente', 'Factura', 'MBruto', 'MImpuesto',
       'MDescuento', 'TOTAL']
df_seleccionados = archivo_excel[columnas]
frame = pd.DataFrame(df_seleccionados)
frame


# In[107]:


# Ventas por mes del año 2019
columnascodmes = ['Fecha', 'MBruto', 'MImpuesto',
       'MDescuento', 'TOTAL']
df_seleccionadoscodmes = archivo_excel[columnascodmes]
frame2 = pd.DataFrame(df_seleccionadoscodmes)
df_seleccionadoscodmes.to_excel('VentasMes.xlsx', sheet_name='ventas mes')
df_seleccionadoscodmes.groupby(pd.Grouper(key='Fecha', freq='1M')).sum()


# In[102]:


# Ventas por cliente por mes
columnascod = ['Fecha', 'Codigo', 'Cliente', 'MBruto', 'MImpuesto',
       'MDescuento', 'TOTAL']
df_seleccionadoscod = archivo_excel[columnascod]
frame3 = pd.DataFrame(df_seleccionadoscod)

frame3.set_index('Codigo').dtypes
df_seleccionadoscodmes.to_excel('VentasClienteMes.xlsx', sheet_name='ventas cliente mes')
pd.DataFrame(df_seleccionadoscod.set_index('Fecha').groupby('Cliente')["TOTAL"].resample("M").sum())


# In[105]:


# Ventas por año por cliente
a= pd.DataFrame(archivo_excel.set_index('Fecha').groupby('Cliente')["TOTAL"].resample("Y").sum())
a.to_excel('VentasClienteanual.xlsx', sheet_name='ventas cliente anual')
a


# In[109]:


archivo_excel2 = pd.read_excel('ventas.xlsx', sheet_name='TotalVentas')
# Ventas de los últimos 3 años
columnasanual = ['Fecha', 'MBruto', 'MImpuesto',
       'MDescuento', 'TOTAL']
df_seleccionadosanual = archivo_excel2[columnasanual]
frame5 = pd.DataFrame(df_seleccionadoscodmes)
df_seleccionadosanual.to_excel('VentasAnuales.xlsx', sheet_name='Ventas')
df_seleccionadosanual.groupby(pd.Grouper(key='Fecha', freq='1Y')).sum()


# In[110]:


# Ventas por mes desde 01/10/2017
df_seleccionadosanual.groupby(pd.Grouper(key='Fecha', freq='1M')).sum()


# In[ ]:





# In[ ]:




