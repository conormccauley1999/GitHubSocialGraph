delete from UserInformation where Id != -1;
delete from Repository where Id != -1;
delete from `User` where Id not in (1, 2);
