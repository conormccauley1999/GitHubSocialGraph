drop trigger if exists TR_User_DC;
drop trigger if exists TR_User_DM;
drop trigger if exists TR_Repository_DC;
drop trigger if exists TR_Repository_DM;
drop trigger if exists TR_Follow_DC;
drop trigger if exists TR_Follow_DM;
drop trigger if exists TR_Star_DC;
drop trigger if exists TR_Star_DM;
drop trigger if exists TR_UserRelationship_DC;
drop trigger if exists TR_UserRelationship_DM;
drop trigger if exists TR_MaxDepth_DC;
drop trigger if exists TR_MaxDepth_DM;
drop trigger if exists TR_UserInformation_DC;
drop trigger if exists TR_UserInformation_DM;
drop trigger if exists TR_RepositoryInformation_DC;
drop trigger if exists TR_RepositoryInformation_DM;
drop trigger if exists TR_Commit_DC;
drop trigger if exists TR_Commit_DM;

create trigger TR_User_DC before insert on `User` for each row set new.DateCreated = now();
create trigger TR_User_DM before update on `User` for each row set new.DateModified = now();
create trigger TR_Repository_DC before insert on Repository for each row set new.DateCreated = now();
create trigger TR_Repository_DM before update on Repository for each row set new.DateModified = now();
create trigger TR_Follow_DC before insert on Follow for each row set new.DateCreated = now();
create trigger TR_Follow_DM before update on Follow for each row set new.DateModified = now();
create trigger TR_Star_DC before insert on Star for each row set new.DateCreated = now();
create trigger TR_Star_DM before update on Star for each row set new.DateModified = now();
create trigger TR_UserRelationship_DC before insert on UserRelationship for each row set new.DateCreated = now();
create trigger TR_UserRelationship_DM before update on UserRelationship for each row set new.DateModified = now();
create trigger TR_MaxDepth_DC before insert on MaxDepth for each row set new.DateCreated = now();
create trigger TR_MaxDepth_DM before update on MaxDepth for each row set new.DateModified = now();
create trigger TR_UserInformation_DC before insert on UserInformation for each row set new.DateCreated = now();
create trigger TR_UserInformation_DM before update on UserInformation for each row set new.DateModified = now();
create trigger TR_RepositoryInformation_DC before insert on RepositoryInformation for each row set new.DateCreated = now();
create trigger TR_RepositoryInformation_DM before update on RepositoryInformation for each row set new.DateModified = now();
create trigger TR_Commit_DC before insert on `Commit` for each row set new.DateCreated = now();
create trigger TR_Commit_DM before update on `Commit` for each row set new.DateModified = now();
