import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title='Страница загрузки датасетов', page_icon='📑')
st.title(
    'Реализация функционала загрузки файлов пользователем'
    )
st.write(
    '#### Для загрузки перетащи или прикрепи файл к виджету на боковой панели'
    )

upload_file = st.sidebar.file_uploader(
    label='Загрузи CSV файл (tips.csv)',
    type='csv'
    )

# кэшированная функция загрузки датасета пользователем
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return None

if upload_file is not None:
    df = load_data(uploaded_file=upload_file)
    st.write('### Первые 5 строчек загруженного датасета')
    st.write(df.head(5))
    st.write('### Тепловая карта зависимостей численных переменных')
    corr_matrix = df.corr(
        method='pearson', min_periods=1, numeric_only=True
        )
    fig, ax = plt.subplots()
    ax = sns.heatmap(
        data=corr_matrix,
        annot=True,
        cmap='coolwarm',
        linewidths=0.5
    )
    plt.tight_layout()
    st.pyplot(fig)

    fig.savefig('numbers_heatmap.png')

    with open('numbers_heatmap.png', 'rb') as file:
        # кнопку загрузки тоже вынесем на боковую панель для учебных целей
        button = st.sidebar.download_button(
            label='Сохранить созданную тепловую карту',
            data=file,
            file_name='numbers_heatmap.png',
            mime='image/png'
        )
else:
    st.stop()
