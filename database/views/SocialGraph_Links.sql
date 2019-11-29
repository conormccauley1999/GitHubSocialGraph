use ghsocialgraph;
drop view if exists SocialGraph_Links;

create view SocialGraph_Links as
	select f.FollowerUserId `source`, f.FollowingUserId `target`
    from Follow f
    where
		f.FollowerUserId in (select Id from SocialGraph_Nodes) and
        f.FollowingUserId in (select Id from SocialGraph_Nodes)
;
