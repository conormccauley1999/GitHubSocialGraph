use ghsocialgraph;
drop function if exists GetUserId;

delimiter //
create function GetUserId(Username varchar(255)) returns int
begin
    return (select u.Id from `User` u where u.Username = Username);
end //
delimiter ;
