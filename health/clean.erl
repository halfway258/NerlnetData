-module(clean).

-export([start/0, start/1]).

%% clean all files ending with .csv in folder
start() ->
    {ok, Dir} = file:get_cwd(),
    {ok, Files} = file:list_dir(Dir),
    CSVs = [File || File <- Files, string:find(File, ".csv", trailing) /= nomatch],
    logger:info("Cleaning files: ~p",[CSVs]),
    [start(File) || File <- CSVs].

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


trimElem([], Data) -> Data;
trimElem([Elem | Elements], Data) ->
    case string:split(Elem, "\n") of
        [Val, _LinNum] ->  trimElem(Elements, Data ++ Val ++ "\n"); %% <------- CHANGE HERE
        _Normal -> trimElem(Elements, Data ++ Elem ++ ",")
    end.
