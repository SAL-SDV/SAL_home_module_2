#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
受け取った動画に対して以下の処理を行う
1. 動画をフレーム毎に分析
2. 重心が中心に来ている画像(有効画像)を抽出、保存
3. フレーム差分から移動方向を計算 外出・帰宅を判定
*)要　pip install opencv-python
     pip install opencv-contrib-python
"""
import cv2
import time

def change_img(path):
    #name = "2019-12-08-18-17-10.h264"  #動画のパス名
    name = path
    name_fraze = name[:-30]+"images/111001_" + name[-24:-5]
    #name ="ss.mp4"
    cap = cv2.VideoCapture(name)  # opencvで動画を扱うための処理

    # 幅
    W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # 高さ
    H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # 総フレーム数
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 前フレームを格納するための変数
    before = None

    num = 1
    min = W
    frame_num = 0
    judge = [0,0]
    while(cap.isOpened()):  # 最終フレームまで処理を繰り返す
        ret, frame = cap.read()  # retはフレーム内か判定するためのフラグ、frameは１フレームの画像
        if ret == True:  # 画像がフレーム内のものだったら
            # -----以下に画像処理を記述-----
            # frame = cv2.resize(frame, (int(frame.shape[1]/3), int(frame.shape[0]/3)))  #リサイズが必要なら追加
            # グレースケール化
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 変数beforeに前フレームの画像をコピー
            if before is None:
                before = gray.copy().astype('float')
                continue
            # 現フレームと前フレームの差を計算(加重平均)
            cv2.accumulateWeighted(gray, before, 0.5)
            mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))

            # 動いているエリアとそれ以外で２値化
            thresh = cv2.threshold(mdframe, 3, 255, cv2.THRESH_BINARY)[1]
            # 輪郭データに変換
            #image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # opencvのバージョンが４以前の場合はこっち
            contours, hierarchy= cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            max_area = 0
            target = contours[0]

            # contoursには輪郭のリストが格納されている
            for cnt in contours:
                area = cv2.contourArea(cnt)  # 輪郭の面積を求める
                # 輪郭が一番大きい & 大きさが一定値以内
                if max_area < area and area < 10000 and area > 1000:
                    max_area = area;
                    target = cnt

            # 十分な大きさ（面積が１０００）の動体の輪郭が見つかったとき
            if max_area >= 1000:
                # 輪郭の左上のx,y、幅、高さを代入
                x,y,w,h = cv2.boundingRect(target)
                # もし輪郭の重心が画像の中心に近かったらフレーム番号を記録
                if abs(x+w/2 - W/2) < min:
                    frame_num = num
                    min = abs(x+w/2 - W/2)
                # もし最後の１０フレーム以内だったら外出判定用変数に加算
                if (count - num - 1) < 10:
                    judge[0] +=  x+w/2  # 重心の位置を加算
                    judge[1] += 1  # 加算回数を記録

             # -----画像処理終了-----
            num += 1  #ファイル名用の変数

        else:  # 画像がフレーム外のものだったら
            break
    
    #もし外出画像だったら
   # print(judge,judge[0]/judge[1])
    #print(frame_num)
    cap.release()

    cap = cv2.VideoCapture(name)  # opencvで動画を扱うための処理    
    if judge[0]/judge[1] > W/2:
        # 一番動体が画像の中心に近いフレームを指定
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        ret, frame = cap.read()
        #print(ret,frame)
        if ret:
            #cv2.imwrite("picture{:0=3}".format(frame_num)+".jpg",frame)  #画像を保存
            cv2.imwrite(name_fraze+".jpg",frame)  #画像を保存
            print(name_fraze+".jpg")   #保存画像のファイル名表示

    cap.release()
if __name__=='__main__':
    change_img('/home/pi/SAL_Web-master/media/movie/2019:12:26:18:25:46.h264')
    print("a")
