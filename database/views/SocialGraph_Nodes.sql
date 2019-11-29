use ghsocialgraph;
drop view if exists SocialGraph_Nodes;

create view SocialGraph_Nodes as
	select u.Id, u.Username, c.Connectivity
    from `User` u
    join UserInformation ui on ui.UserId = u.Id
    join SocialGraph_Connectivity c on c.UserId = u.Id
    where
		u.IsExplored and not u.`Ignore`
;
