-module(clean).

-export([start/1]).


start(FName) ->
    {ok, Data} = file:read_file(FName),
    % io:format("Old: ~p~n",[Data]),
    %% change ? => 0.0
    NewData = string:replace(binary_to_list(Data), "?", "0.0", all),
    %% remove line numbers
    NewerData = removeLineNum(NewData),
    % io:format("New: ~p~n",[NewData]),
    file:write_file(FName, NewerData).

removeLineNum(Data) ->
    Elements = string:split(Data, ",", all),
    %% some elements will look like X\nNUM, need to replace with X\n
    tl(string:split(trimElem(Elements, []), ",")).  %% and remove first line number


%% for int:     change to: trimElem(Elements, Data ++ string:left(Elem, 2))         %% <------- CHANGE HERE
%% for float:   change to: trimElem(Elements, Data ++ string:left(Elem, 3) ++ "\n") %% <------- CHANGE HERE
trimElem([], Data) -> Data;
trimElem([Elem | Elements], Data) ->
    case string:find(Elem, "\n") of
        nomatch -> trimElem(Elements, Data ++ Elem ++ ",");
        _Normal -> trimElem(Elements, Data ++ string:left(Elem, 2)) %% <------- CHANGE HERE
    end.

