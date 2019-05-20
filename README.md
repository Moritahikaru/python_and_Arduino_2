# python_and_Arduino_2

# test_serial

## PC側

- Arduinoとのシリアル通信を開始（ボタン"connect"）。
- Arduinoへデータを送信（ボタン"send"、合図は'a'）。送信内容をprint
- Arduinoからデータを受信（ボタン"receive"、合図は'b'）。受信内容をprint

## Arduino側

- 電源投入後、シリアル通信開始待ち（setupにSerial.beginを書くだけ）。
- シリアル通信開始後、合図が送られてくるのを待つ。
- 合図が'a'（ボタン"send"が押された）、データを受け取り、変数dataに保存。
- 合図が'b'（ボタン"receive"が押された）、変数dataの内容を送る。
- その後、待ち状態へ。

## 参照

- [pySerial](https://pythonhosted.org/pyserial/index.html)（pythonでシリアル通信。importするときの名前はserial）
- [Arduino日本語リファレンス](http://www.musashinodenpa.com/arduino/ref/)（情報が古そうで、Serial.readStringなどは載っていない。）
- [Arduino Language Reference](https://www.arduino.cc/reference/en/)（Serial.readStringなどはこちらを見る）

# test_serial2

## PC側

- Arduinoとのシリアル通信を開始（ボタン"connect"）。
- Arduinoへデータ（そのときにエントリーに入力されているテキスト）を送信（ボタン"send"、合図は'a'）。送信内容をprint
- Arduinoからデータを受信（ボタン"receive"、合図は'b'）。受信内容をprint
- Arduinoへ送るためのデータを入力するエントリー。

## Arduino側

test_serialと同じ。