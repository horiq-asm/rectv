![IMG_5271](https://github.com/horiq-asm/rectv/assets/103295965/d0462400-499d-4a93-b4c4-2f1d146f0fef)

# web上の録画予約データを読み込んでrecpt1で録画する
>rectv　raspberry　pi　CM4　light　1Gでoverlay動作確認,<br>
cronで5分毎に起動<br>
4-59/5 * * * * /usr/bin/python3 /home/pi/rk1.py<br>
=======上記は録画機の設定ファイルです<br>
recpt1以外は動かないので軽い動作ができています。<br>
録画予約は別途webサーバで行います。<br>
ktest.html   rokuga.cgi がそのファイルになります。<br>
web上の録画予約データ例<br>
2024 02 13 22 00 45 31 正直不動産(6) 00<br>
2024 02 14 02 30 30 101 スイス・氷河特急の旅 00<br>
2024 02 14 10 00 60 101 幕末の冒険者・ジョン万次郎 00<br>
2024 02 14 08 55 10 101 番組4 00<br>
2024 02 13 19 30 01 14 番組5 00<br>
2024 02 13 19 35 01 14 番組6 00<br>
