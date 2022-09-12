type TLampRow = class
  private FState: string;
  function getState: string;
  procedure setState(s: string);
  procedure Show;
  constructor Create;
end;

constructor TLampRow.Create;
begin
  FState := '00000000';
end;

procedure TLampRow.setState(s: string);
begin
  if Length(s) <> 8 then
    FState := '00000000'
  else
    FState := s;
end;

procedure TLampRow.Show;
var i: integer;
    is_empty: boolean;
begin
  is_empty := true;
  for i:=1 to Length(FState) do
    if FState[i] = '1' then begin
      is_empty := false;
      break;
    end;
  if is_empty = true then
    writeln('--------')
  else begin
    for i:=1 to Length(FState) do
      if FState[i] = '0' then
        write('-')
      else
        write('*');
    writeln;
    end;
end;

function TLampRow.getState: string;
begin
  getState := FState;
end;

begin
  var lamps := TLampRow.Create;
  lamps.Show;
  lamps.setState('10101010');
  writeln(lamps.getState);
  lamps.Show;
end.