type TParrot = class
  msg: string = 'Привет, друзья!';
  constructor Create(msg0: string);
  procedure Say;
  procedure NewText(msg0: string);
end;

constructor TParrot.Create(msg0: string);
begin
  msg := msg0;
end;

procedure TParrot.Say;
begin
  writeln(msg);
end;

procedure TParrot.NewText(msg0: string);
begin
  msg := msg0;
end;

var
  p: TParrot;

begin
  p := TParrot.Create('Гав!');
  p.Say;
  p.NewText('Мяу!');
  p.Say;
end.