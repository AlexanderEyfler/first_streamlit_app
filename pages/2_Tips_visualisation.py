# Реализован функционал с предварительно загруженным датасетом.
# Можно оптимизировать код, написав функцию сохранения картинки по кнопке,
# и потом после каждого графика вызывать функцию с нужными аргументами
# но сейчас наводить лоск в этом учебном приложении не считаю рациональной
# тратой времени.
# Также не стал отображать все графики из датасета, т.к. принцип понятен,
# а дальше просто дело времени и техники.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# начальные настройки страницы
st.set_page_config(page_title='Визуализация tips', page_icon='💸')
st.title(
    'Отображение графиков по результатам исследования датасета tips.csv'
    )
st.write(
    '### Датасет подготовлен и загружен заранее,'
    ' вам предлагается ознакомиться с графиками'
    )

# получаем интересующий датасет
tips = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    )

# 1. гистограмма total bill
st.write('#### Гистограмма распределения значений суммарного чека (Total bill)')
fig1 = sns.displot(
    data=tips,
    x= 'total_bill',
    kind='hist',
    kde=True
)
plt.tight_layout()
st.pyplot(fig1.figure)

# сохраняем гистограмму ее методом savefig(), чтобы потом можно было скачать по кнопке
fig1.figure.savefig('total_bill_histogram.png')

# скачиваем гистограмму по кнопке себе на машину
with open('total_bill_histogram.png', 'rb') as file:
    button = st.download_button(
        label='Сохранить график, представленный выше',
        data=file,
        file_name='total_bill_histogram.png',
        mime='image/png'
    )

# 2. Нарисуйте scatterplot, показывающий связь между total_bill and tip
st.write('#### Зависимость размера чаевых от суммы счета')
fig2, ax2 = plt.subplots()

ax2 = sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='sex'
)
ax2.set(
    title='Зависимость размера чаевые от суммы счета',
    ylabel='Чаевые (tip)',
    xlabel='Сумма счета (total_bill)'
)
plt.tight_layout()
st.pyplot(fig2)

fig2.savefig('scatter_tip_total_bill.png')

with open('scatter_tip_total_bill.png', 'rb') as file:
    button = st.download_button(
        label='Сохранить график, представленный выше',
        data=file,
        file_name='scatter_tip_total_bill.png',
        mime='image/png'
    )

# 3. Сделай аналогичный график используя многофункциональный метод relplot
st.write(
    '#### Более подробная аналитка по зависимости размера чаевых от суммы счета'
    )
fig3 = sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='day',
    col='time',
    row='sex'
)
plt.tight_layout()
st.pyplot(fig3)

fig3.figure.savefig('relplot_tip_total_bill.png')

with open('relplot_tip_total_bill.png', 'rb') as file:
    button = st.download_button(
        label='Сохранить график, представленный выше',
        data=file,
        file_name='relplot_tip_total_bill.png',
        mime='image/png'
    )

# 4. Покажите связь между днем недели и размером счета
st.write('#### Зависимость размера счета от дня недели')
days_order = ['Thur', 'Fri', 'Sat', 'Sun']

fig4, ax4 = plt.subplots(figsize=(8,4))
ax4 = sns.barplot(
    data=tips,
    x='day',
    y='total_bill',
    order=days_order,
    errorbar=None
)
ax4.set(
    title='Изменение размера счета в зависимости от дня недели',
    ylabel='Размер счета (total_bill)',
    xlabel='День недели (day)'
)
plt.tight_layout()
st.pyplot(fig4)

fig4.savefig('barplot_day_total_bill.png')

with open('barplot_day_total_bill.png', 'rb') as file:
    button = st.download_button(
        label='Сохранить график, представленный выше',
        data=file,
        file_name='barplot_day_total_bill.png',
        mime='image/png'
    )

# 5. Нарисуйте box plot c суммой всех счетов за каждый день,
# разбивая по time (Dinner/Lunch)
st.write(
    '#### Box plot c суммой всех счетов за каждый день,'
    ' c разбивкой по time (Dinner/Lunch)'
    )

fig5, ax5 = plt.subplots(figsize=(8,4))
ax5 = sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='time',
    order=days_order,
    gap=0.1
)
plt.tight_layout()
st.pyplot(fig5)

fig5.savefig('boxplot_day_total_bill.png')

with open('boxplot_day_total_bill.png', 'rb') as file:
    button = st.download_button(
        label='Сохранить график, представленный выше',
        data=file,
        file_name='boxplot_day_total_bill.png',
        mime='image/png'
    )
