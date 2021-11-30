<h1>SAL_home_module</h1>

## 使い方
1. `cd SAL_Web_master/modules`
2. `sudo python3.5 send_img.py`

## 役割
1. カメラモジュールから受け取った動画から有効画像を切り出し、~/SAL_Web_master/mediaに保存する。
2. １の画像を市役所サーバに送信する。
3. 外出情報のログを本モジュールから確認できるようにする。

### 注意事項
- django及びSQLの設定は済んでいるいるものとします。
- 現在opencvのバージョンの関係でpython3.5でしか実行を確認できていません。よってpython3.5での実行推奨です。
- カメラモジュールと市役所サーバが動作中であることが前提になっています。もし単体でデバックを行いたい場合、send_img.pyとその関連プログラムを微調整してください。
- send_img_send.pyで送信先のIPアドレスを直接指定しているので、送信先のIPアドレスが変更された場合はそこをいじってください。

![スクリーンショット 2021-11-30 225337](https://user-images.githubusercontent.com/52097096/144059864-619b545b-c0a7-49ac-afa6-8380ac52bab0.jpg)
