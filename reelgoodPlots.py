import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea
import numpy as np


def plot(df):
    # produce plot and return the 'axes'
    df_tv = df.groupby('mediatype').get_group('TV').reset_index(drop=True)
    print(df_tv['reelgood'].mean())
    print(df_tv['imdb'].mean())
    print(df_tv)
    df_mov = df.groupby('mediatype').get_group('Movie').reset_index(drop=True)
    print(df_mov['reelgood'].mean())
    print(df_mov['imdb'].mean())
    print(df_mov)

    # Line Plot of TV show Reelgood and IMDb scores over time
    # df_tv['year'] = pd.to_datetime(df_tv['year'], format='%Y')
    # df_tv = df_tv[df_tv['year'].dt.year <= 2022]
    # df_tv = df_tv.sort_values(by='year')
    # df_tv['reelgood'] = df_tv['reelgood'].div(10)
    # title = 'TV Show IMDb and Reelgood Scores over time'
    # ax = sea.lineplot(data=df_tv, x='year', y='reelgood', ci=None)
    # ax = sea.lineplot(data=df_tv, x='year', y='imdb', ci=None)
    # ax.legend(['Reelgood', 'IMDb'])
    # ax.set(xlabel='Year', ylabel='Scores', title=title)

    # Line Plot of Movie show Reelgood and IMDb scores over time
    # df_mov['year'] = pd.to_datetime(df_mov['year'], errors='coerce')
    # df_mov = df_mov.dropna(subset=['year'])
    # df_mov = df_mov[df_mov['year'].dt.year <= 2022]
    # df_mov = df_mov.sort_values(by='year')
    # df_mov['reelgood'] = df_mov['reelgood'].div(10)
    # title = 'Movie IMDb and Reelgood Scores over time'
    # ax = sea.lineplot(data=df_mov, x='year', y='reelgood', ci=None)
    # ax = sea.lineplot(data=df_mov, x='year', y='imdb', ci=None)
    # ax.legend(['Reelgood', 'IMDb'])
    # ax.set(xlabel='Year', ylabel='Scores', title=title)

    # Boxplot of IMDb scores for all 3276 Movies and all 5752 TV Shows
    # title = 'IMDb scores of all Movies and TV shows'
    # pal = {'TV': "#0ee694", 'Movie': "#e50914"}
    # ax = sea.boxplot(data=df, x="mediatype", y="imdb", palette=pal)
    # ax.set(xlabel='Media Type', title=title)

    # Boxplot of Reelgood scores for all 3276 Movies and all 5752 TV Shows
    # title = 'Reelgood scores of all Movies and TV shows'
    # pal = {'TV': "#0ee694", 'Movie': "#e50914"}
    # ax = sea.boxplot(data=df, x="mediatype", y="reelgood", palette=pal)
    # ax.set(xlabel='Media Type', title=title)

    # Joint KDE Plot of Scores for all Movies and TV shows
    title = 'Joint KDE Plot of Scores for all Movies and TV shows'
    df['reelgood'] = df['reelgood'].div(10)
    pal = {'TV': "#0ee694", 'Movie': "#e50914"}
    ax = sea.jointplot(data=df, x="imdb", y="reelgood", hue="mediatype", kind='kde', palette=pal)
    ax.fig.suptitle(title)

    return ax


def main_plots():
    df = pd.read_csv('reelgood.csv')
    plot(df)
    plt.show()


if __name__ == '__main__':
    main_plots()
