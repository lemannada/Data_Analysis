from data.data_preparation import prepare_data
from scripts.visualizations1 import configure_styles, create_main_visualizations1
from scripts.visualizations2 import configure_styles, create_main_visualizations2
from scripts.visualizations3 import configure_styles, create_additional_visualizations
from scripts.analysis import perform_analysis


def main():
    # Подготовка данных
    df = prepare_data()

    # Настройка стилей графиков
    configure_styles()

    # Основные визуализации
    create_main_visualizations1(df)
    create_main_visualizations2(df)
    # Дополнительные визуализации
    create_additional_visualizations(df)

    # Аналитические расчеты
    perform_analysis(df)


if __name__ == "__main__":
    main()