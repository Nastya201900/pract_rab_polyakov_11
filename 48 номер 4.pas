type TParrot = class
  msg: string = 'Привет, друзья!';
  constructor Create(msg0: string);
  procedure Say;
end;

constructor TParrot.Create(msg0: string);
begin
  msg := msg0;
end;

procedure TParrot.Say;
begin
  writeln(msg);
end;

var
  p1, p2: TParrot;

begin
  p1 := TParrot.Create('Гав!');
  p2 := TParrot.Create('Мяу!');
  p1.Say;
  p2.Say;
end.