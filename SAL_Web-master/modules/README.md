# module
***
このディレクトリにはカメラから受け取った動画に対する一定の処理を行うプログラムが格納されています。
```
・movie_to_img.py(仮実装)  ラズパイ０から受け取った動画に対して帰宅・外出判定、有効画像の検出及び保存を行います
・send_img.py  /viewer/public/imgフォルダの中身に変更（追加、変更、削除）が加えられたときに、変更に応じてsend_img_action.py,send_img_registorを実行します。
・send_img_action.py   変更されたファイルを市役所サーバ（現在はテスト用の自前ラズパイ）に送信するプログラムです。send_img.pyからimportされます。
・send_img_registor.py(仮実装)   変更されたファイルの情報を市役所サーバ（現在はテスト用の自前ラズパイ）のDBに登録するプログラムです。send_img.pyからimportされます。一部おかしい挙動はありますが動きます。
・DBregistor.py
・DBuploader.py
・B.py
・db_test_py
・test_c.sh
```
置いてあるmp4はテスト用動画
