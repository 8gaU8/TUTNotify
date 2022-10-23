# TUT Notify
- 毎朝+授業開始前に時間割をLINEで通知
- Python3 + [LINE Notify](https://notify-bot.line.me/ja/)

## 使い方
1. 本リポジトリをクローンしてセットアップ
   ```shell
   $ #ターミナル
   $ git clone https://github.com/straxFromIbr/TUTNotify
   $ cd TUTNotify
   $ python3 -m pip install -r requirements.txt
   ```


1. LINE NotifyのAPIトークンを取得して`./token.txt`に保存
1. 大学教務システムの、トップページ > 履修・成績情報 > 履修時間割 のHTMLをダウンロードし、schedule.htmlに保存
1. HTMLからデータ取得, `schedule.json`が作成される
   ```shell
   python3 scrape.py
   ```
1. 任意の方法で実行！
- シェルから
  - 引数なし→その日の時間割
  ```shell
  $ python3 main.py
  ```

  - 引数あり→その時間の時間割
  ```shell
  $ python3 main.py 1 
  # 1限目の時間割
  ```

- crontabから
  ```cron
  # TUT Notify
   0  8 * * * /home/pi/TUTNotify/main.py
  40  8 * * * /home/pi/TUTNotify/main.py 1
  20 10 * * * /home/pi/TUTNotify/main.py 2
  50 12 * * * /home/pi/TUTNotify/main.py 3
  30 14 * * * /home/pi/TUTNotify/main.py 4
  10 16 * * * /home/pi/TUTNotify/main.py 5
  50 17 * * * /home/pi/TUTNotify/main.py 6
  ```


