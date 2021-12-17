import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, source_url):
    # 検索対象取得
    df=pd.read_csv(source_url)
    source=list(df["name"])

    # 検索
    result = ""
    if word in source:
        result = f'『{word}』はあります'
    else:
        result = f'『{word}』はありません'
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(source_url ,encoding="utf_8-sig")
    print(source)
    
    return result