import pandas as pd


'''
Задание 1
Напишите функцию, которая классифицирует фильмы из материалов занятия по правилам:

оценка 2 и ниже — низкий рейтинг;
оценка 4 и ниже — средний рейтинг;
оценка 4.5 и 5 — высокий рейтинг.
Результат классификации запишите в столбец class.
'''


def classify_movie(df) -> pd.DataFrame:
    df['class'] = 'Не определён'
    df.loc[df['rating'] <= 2, 'class'] = 'низкий'
    df.loc[(2 < df['rating']) & (df['rating']<= 4), 'class'] = 'средний'
    df.loc[(4 < df['rating']) & (df['rating'] <= 5), 'class'] = 'высокий'
    return df

ratings = pd.read_csv('raw_data/ratings.csv')
ratings = classify_movie(ratings)
print (ratings)