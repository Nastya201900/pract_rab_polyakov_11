type TParrot = class
  msg: string = 'Привет, друзья!';
  procedure Say;
end;

procedure TParrot.Say;
begin
  writeln(msg);
end;

var
  p: Tparrot;

begin
  p := TParrot.Create;
  p.Say;
end.