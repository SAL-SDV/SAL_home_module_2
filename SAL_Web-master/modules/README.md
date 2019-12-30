# module
***
このディレクトリにはカメラから受け取った動画に対する一定の処理を行うプログラムが格納されています。

## send_img.py（メイン)
/viewer/public/imgフォルダの中身に変更（追加、変更、削除）が加えられたときに、変更に応じてsend_img_action/配下のモジュールを呼び出します。

## send_img_action配下(モジュール)
- **movie_to_img.py**  ラズパイ０から受け取った動画に対して帰宅・外出判定、有効画像の検出及び保存を行う。
- **registor_img.py**  有効画像の情報をDBに登録する。
- **send_img_action.py**  有効画像を市役所サーバに送信する（scp使用） 　
- send_img_registor.py   有効画像の情報を市役所サーバのDBに登録する。使いません。


置いてあるmp4はテスト用動画
