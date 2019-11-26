use ghsocialgraph;
drop view if exists UsersToExplore;

create view UsersToExplore as
	select u.Id UserId, u.Username, r.CurrentDepth `UserDepth`
    from `User` u
    join UserRelationship r on r.UserId = u.Id
    where
		(not u.IsExplored) and
        r.CurrentDepth <= GetMaxDepth()
;
