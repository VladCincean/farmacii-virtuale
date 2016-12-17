use Trivia;

/**
--------------------------------------------------------------------------------
| Q_nr | WHERE | GROUP BY | DISTINCT | HAVING |   JOIN TABLES  |   JOIN m:n-r  |
--------------------------------------------------------------------------------
|  01  |   x   |          |          |        |                |               |
|  02  |       |     x    |          |        |        x       |               |
|  03  |       |          |    x     |        |                |               |
|  04  |       |     x    |          |   x    |                |               |
|  05  |   x   |     x    |          |        |        x       |       x       |
|  06  |       |     x    |    x     |   x    |                |               |
|  07  |   x   |     x    |    x     |   x    |        x       |               |
|  08  |       |     x    |          |   x    |        x       |               |
|  09  |   x   |          |          |        |        x       |               |
|  10  |   x   |     x    |          |        |        x       |       x       |
|  11  |       |          |          |        |        x       |       x       |
|  12  |   x   |          |          |        |        x       |       x       |
|  13  |       |     x    |          |        |        x       |               |
--------------------------------------------------------------------------------
| Total|   6   |     8    |    3     |   4    |        9       |       4       |
--------------------------------------------------------------------------------
 */

-- Q1:	All players with level >= 4
-- where
select username, [level]
from Players
where [level] >= 4;

-- Q2: Number of questions in each cathegory ordered decreasing
-- inner join, group by
select c.cathegory_name as cathegory,
		count(q.cathegory_id) as number 
from Questions q
inner join Cathegories c
on q.cathegory_id = c.id
group by c.cathegory_name
order by number desc;

-- Q3: All players' locations
-- distinct
select distinct [location]
from Players;

-- Q4: All players that played at least 4 games and scored 100 pts, in average
-- group by, having
select username, count(id) as [game count], avg(score) as score
from Games
group by username
having count(id) >= 4 and avg(score) >= 100;

-- Q5: All chemistry questions that were asked as bonus questions
-- 2x inner join, where, group by
select question_text, count(questionBonus_id) as [number of times]
from Questions
inner join GameSessions
on Questions.id = GameSessions.questionBonus_id
inner join Cathegories
on Cathegories.id = Questions.cathegory_id
where Cathegories.cathegory_name = 'Chemistry'
group by question_text;

-- Q6: Top browsers by number of logins, but having at least 2 logins
--group by, having
select distinct browser, count(browser) as [nr of logins]
from LoginHistory
group by browser
having count(browser) >= 2
order by [nr of logins] desc;

-- Q7: All users and their emails that have logged in at least twice from Chrome
-- inner join, where, group by, having
select distinct u.username, min(u.email), count(lh_id)
from Users u
inner join LoginHistory lh
on u.username = lh.username
where browser = 'Chrome'
group by u.username
having count(lh_id) >= 2;

-- Q8: All players that have not played any game ever
-- join, group by, having
select distinct p.username--, count(g.id) as [count]
 from Players p
left join Games g
on p.username = g.username
group by p.username
having count(g.id) = 0;

-- Q9: All female players and their emails
-- inner join, where
select u.username, email
 from Users u
inner join Players p
on u.username = p.username
where p.gender = 'Female';

-- Q10: All computer science questions that were asked as 1st question
-- inner join, where, group by
select question_text, count(question1_id) as [nr of times]
from Questions
inner join GameSessions
on Questions.id = GameSessions.question1_id
inner join Cathegories
on Cathegories.id = Questions.cathegory_id
where Cathegories.cathegory_name = 'Computer Science'
group by question_text;

-- Q11: All questions with their difficulties ordered by the cathegory name
-- 2x inner join
select c.cathegory_name as cathegory,
		d.difficulty_name as difficulty,
		q.question_text as number
from Questions q
inner join Cathegories c
on q.cathegory_id = c.id
inner join Difficulties d
on q.difficulty_id = d.id
order by cathegory;

-- Q12:	The winner for every game session
-- 3x inner join, 2x where
select	'For the game session #',
		gs.id as [Session Id],
		', the winner is ',
		p.username as [username],
		' (score = ',
		g.score as [score],
		').'
from	GameSessions gs
inner join Games g
on gs.id = g.session_id
inner join Players p
on g.username = p.username
where	g.score >=
(
	select	g1.score
	from	GameSessions gs1
	inner join Games g1
	on gs1.id = g1.session_id
	where gs.id = gs1.id and g.username != g1.username
);

-- Q13: Top players by the number of games played
-- inner join, group by
select	p.username as [Player],
		count(g.id) as [nr of games]
from	Players p
inner join Games g
on g.username = p.username
group by p.username
order by [nr of games] desc;


-- Q14
-- ...
select	p1.username		as [Player],
		count(gs1.id)	as [Wins]/*,
		...				as [Drafts],
		...				as [Loses]*/
from	GameSessions gs1
inner join Games g1
on gs1.id = g1.session_id
inner join Players p1
on g1.username = p1.username
where	g1.score > 
(
	select	g11.score
	from	GameSessions gs11
	inner join Games g11
	on gs11.id = g11.session_id
	where	gs11.id = gs1.id and g11.username != g1.username
)
group by p1.username
/*and		-- ...
(
	-- ...
)*/