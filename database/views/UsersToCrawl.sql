use ghsocialgraph;
drop view if exists UsersToCrawl;

create view UsersToCrawl as
	select u.`Name`
    from `User` u
    join UserRelationship r on r.UserId = u.Id
    where
		(not u.IsExplored) and
        r.CurrentDepth <= GetMaxDepth()
;
