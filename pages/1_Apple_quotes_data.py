# импоритурем используемые библиотеки и модули
import yfinance as yf
import streamlit as st
import pandas as pd

# задаем параметры отображения страницы, иконку и тектовое наполнение
st.set_page_config(page_title='Котировки Apple', page_icon='🍏')
st.title(
    'Отображение основных котировок компании Apple'
    )
st.write('### Значения отображаются за заданный период времени с дискретностью 1 день')

# задаем константу, так как по условию задания, интересуют только котировки APPLE
TICKER_SYMBOL = 'AAPL'

# задаем значения диапазона дат по умолчанию, скажем, за 10летний период
default_start_date = pd.to_datetime('2014-1-1')
default_end_date = pd.to_datetime('2024-1-1')

# функция получения исторических данных из библиотеки yfinance
# попробовал кешировать, по ТЗ к домашке ну и по логике, чтобы постоянно не
# тянуть файлы оттуда (не уверен, что кеширование тут корректно и нужно)
@st.cache_data
def load_data(ticker_symbol, start_date, end_date):
    ticker_data = yf.Ticker(TICKER_SYMBOL)
    return ticker_data.history(period='1d', start=start_date, end=end_date)

# ввод пользовательских дат (с заранее введенными значениями по умолчанию)
start_date = st.date_input(
    label='Введите дату начала отчетности (по умолчанию 2014-01-01):',
    value=default_start_date
    )
end_date = st.date_input(
    label='Введите дату окончания отчетности (по умолчанию 2024-01-01):',
    value=default_end_date
    )

# кнопка, нажатие которой отслеживаем для пересчета значений для пользовательских дат
button = st.button(label='Перечитать значения')

# логика работы, если была нажата кнопка
if button:
    ticker_df = load_data(TICKER_SYMBOL, start_date, end_date)
# если кнопка не была нажата, то считаем данные по умолчанию
else:
    ticker_df = load_data(TICKER_SYMBOL, default_start_date, default_end_date)

# функция вывода информации на страницу веб-приложения
# одновременно реализуется доп. задание к домашке про использование
# графиков, отличных от st.pyplot()
def visualize_metric(metric: str, label: str) -> None:
    st.write(f'## {label}')
    st.line_chart(data=ticker_df[metric])

# вызов функции для каждой из метрик
visualize_metric('Open', 'Цена открытия (Open Price)')
visualize_metric('Close', 'Цена закрытия (Closing Price)')
visualize_metric('Volume', 'Объем продаж (Volume)')
visualize_metric('High', 'Максимальная цена (High Price)')
visualize_metric('Low', 'Минимальная цена (Low Price)')
