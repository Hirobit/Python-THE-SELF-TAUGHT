# 非貪欲な正規表現を使った、Mad Libsゲーム
# Mad Libsゲームはいくつかの単語が抜けている文章を表示し、プレイヤーに抜けている単語を当ててもらうゲーム
# このプログラムはアンダースコア２つに挟まれた単語をre.findall関数を使い、ピックアップし、それを質問に使い、入力された文字を元の文に置き換えて最終的に表示する

import re
text = """ 
キリンは大昔から __複数名詞__ の興味の対象ですた。\n
キリンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。\n
キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と __体の一部__によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語（＝ヒント）の部分は後の２つのアンダースコアで挟んでください。
                ヒントの単語にはアンダースコアを含めないで下さい。__hint_hint__はダメです。__hint__はOKです。
    """

    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("/n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)