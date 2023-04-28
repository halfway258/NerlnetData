
-module(clean).

-export([start/1]).

start(FName) ->
    %% change ? => 0.0
    {ok, Data} = file:read_file(FName),
    io:format("Old: ~p~n",[Data]),
    NewData = string:replace(binary_to_list(Data), "?", "0.0", all),
    io:format("New: ~p~n",[NewData]),
    file:write_file(FName, NewData).