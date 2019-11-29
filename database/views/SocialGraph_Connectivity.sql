use ghsocialgraph;
drop view if exists SocialGraph_Connectivity;

create view SocialGraph_Connectivity as
    select u.Id UserId, (f1.Connectivity + f2.Connectivity) Connectivity
    from `User` u
    join (
		select f.FollowerUserId UserId, count(f.FollowingUserId) Connectivity from Follow f
		where
			f.FollowerUserId in (select Id from `User` u where u.IsExplored and not u.`Ignore`) and
			f.FollowingUserId in (select Id from `User` u where u.IsExplored and not u.`Ignore`)
		group by f.FollowerUserId
    ) as f1 on f1.UserId = u.Id
    join (
		select f.FollowingUserId UserId, count(f.FollowerUserId) Connectivity from Follow f
		where
			f.FollowerUserId in (select Id from `User` u where u.IsExplored and not u.`Ignore`) and
			f.FollowingUserId in (select Id from `User` u where u.IsExplored and not u.`Ignore`)
		group by f.FollowingUserId
    ) as f2 on f2.UserId = u.Id
;
