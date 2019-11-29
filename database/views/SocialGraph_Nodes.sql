use ghsocialgraph;
drop view if exists SocialGraph_Nodes;

create view SocialGraph_Nodes as
	select u.Id, u.Username, ui.FollowerCount Followers, ui.FollowingCount Following
    from `User` u
    join UserInformation ui on ui.UserId = u.Id
    where
		u.IsExplored and not u.`Ignore`
;
