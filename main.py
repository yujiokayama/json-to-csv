# Pandasをインポート
import pandas as pd

# 変換したいJSONファイルを読み込む
df = pd.read_json("./json/main.json")

# CSVに変換して任意のファイル名で保存
df.to_csv("./csv/main.csv")
