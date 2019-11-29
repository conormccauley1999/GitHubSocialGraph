use ghsocialgraph;
drop view if exists Overview_Stats;

create view Overview_Stats as
	select
		(select sum(QueriesMade) from Crawler) Queries,
        (select count(Id) from `User` where not IsRoot) UsersIndexed,
        (select count(Id) from `User` where IsExplored and not `Ignore`) UsersExplored,
        (select count(Id) from Repository) ReposIndexed,
        (select count(Id) from Repository where IsExplored) ReposExplored,
        (select max(EndTime) from Crawler) LastCrawled
;
