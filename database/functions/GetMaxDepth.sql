use ghsocialgraph;
drop function if exists GetMaxDepth;

delimiter //
create function GetMaxDepth() returns int
begin
    return (select `Value` from MaxDepth order by `DateModified` desc limit 1);
end //
delimiter ;
