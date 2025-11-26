const int direction = 14;
const int step = 15;

int counter;
int direction_;


void setup() {
  // put your setup code here, to run once:
  pinMode(direction, OUTPUT);
  pinMode(step, OUTPUT);

  digitalWrite(direction, HIGH);

  counter = 0;

  direction_ = HIGH;

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(step, HIGH);
  delay(5000);

  digitalWrite(step, LOW);
  delay(5000);

  counter = counter + 1;

  if (counter % 200 == 0) {
    direction_ = !direction_;
    digitalWrite(direction, direction_);
    
    }

}
