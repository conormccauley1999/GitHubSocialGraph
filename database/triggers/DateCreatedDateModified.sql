drop trigger if exists TR_User_DC;
drop trigger if exists TR_User_DM;
drop trigger if exists TR_Repository_DC;
drop trigger if exists TR_Repository_DM;
drop trigger if exists TR_Follow_DC;
drop trigger if exists TR_Follow_DM;
drop trigger if exists TR_Star_DC;
drop trigger if exists TR_Star_DM;

create trigger TR_User_DC before insert on `User` for each row set new.DateCreated = now();
create trigger TR_User_DM before update on `User` for each row set new.DateModified = now();
create trigger TR_Repository_DC before insert on Repository for each row set new.DateCreated = now();
create trigger TR_Repository_DM before update on Repository for each row set new.DateModified = now();
create trigger TR_Follow_DC before insert on Follow for each row set new.DateCreated = now();
create trigger TR_Follow_DM before update on Follow for each row set new.DateModified = now();
create trigger TR_Star_DC before insert on Star for each row set new.DateCreated = now();
create trigger TR_Star_DM before update on Star for each row set new.DateModified = now();