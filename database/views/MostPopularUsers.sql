use ghsocialgraph;
drop view if exists MostPopularUsers;

create view MostPopularUsers as
	select u.Username, max(ui.FollowerCount) Followers, sum(ri.StarCount) Stars
	from `User` u
	join UserInformation ui on ui.UserId = u.Id
	join Repository r on r.UserId = u.Id
	join RepositoryInformation ri on ri.RepositoryId = r.Id
	where
		u.IsExplored and not u.`Ignore` and r.IsExplored and
		(ui.FollowerCount + ri.StarCount) > 0
	group by u.Username
;
