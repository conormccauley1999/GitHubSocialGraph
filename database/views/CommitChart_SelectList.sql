use ghsocialgraph;
drop view if exists CommitChart_SelectList;

create view CommitChart_SelectList as
    select u.Username
    from `User` u
    where
		u.IsExplored and
        not u.`Ignore`
;
