use ghsocialgraph;
drop function if exists CheckUserExists;

delimiter //
create function CheckUserExists(Username varchar(255)) returns int
begin
    return (select exists(select u.Id from `User` u where u.Username = Username));
end //
delimiter ;
