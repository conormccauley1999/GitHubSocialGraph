use ghsocialgraph;
drop view if exists RepositoriesToExplore;

create view RepositoriesToExplore as
	select r.Id RepositoryId, u.Username, r.`Name` RepositoryName
    from Repository r
    join `User` u on u.Id = r.UserId
    where
		(not u.`Ignore`) and
		(not r.IsExplored)
;
