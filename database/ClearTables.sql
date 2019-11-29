update `User` set IsExplored = 0, LastCrawled = null where Id = 1;
delete from Crawler where Id != -1;
delete from `Commit` where Id != -1;
delete from UserRelationship where Id != 2;
delete from UserInformation where Id != -1;
delete from RepositoryInformation where Id != -1;
delete from Repository where Id != -1;
delete from Follow where Id != -1;
delete from `User` where Id not in (1, 2);
