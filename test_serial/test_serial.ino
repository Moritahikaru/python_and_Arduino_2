String data;

void setup() {
  Serial.begin(57600);
}

void loop() {
  //開始の合図が届くまで待つ
  while ( (Serial.available() > 0) == false ) {}
  char aizu=Serial.read();
  if (aizu=='a'){
    data=Serial.readString();
  }else if (aizu=='b'){
    Serial.println(data);
  }
  //届いているものをクリア。合図以外を捨てる。
  while (Serial.available()) { Serial.read(); }
}
