use master;

if exists(select * from sys.databases where [name] = 'Trivia')
begin
	print 'DB found';
	drop database Trivia;
end
else
begin
	print 'DB does not exist';
end

go
create database Trivia;

go
use Trivia;

--> create table Cathegories
create table Cathegories
(
	id				int identity(1, 1)	not null,
	cathegory_name	varchar(30)			not null,
	[description]	text				not null,

	constraint pk_cathegories	primary key(id),
	constraint u_cathegory_name	unique(cathegory_name)
);

--> create table Difficulties
create table Difficulties
(
	id				int identity(1, 1)	not null,
	difficulty_name	varchar(30)			not null,
	
	constraint pk_difficulties		primary key(id),
	constraint u_difficulty_name	unique(difficulty_name)
);

--> create table Questions
create table Questions
(
	id				int identity(1, 1)	not null,
	cathegory_id	int					not null,
	difficulty_id	int					not null,
	question_text	varchar(255)		not null,
	optionA			varchar(100)		not null,
	optionB			varchar(100)		not null,
	optionC			varchar(100)		not null,
	optionD			varchar(100)		not null,
	correct_answer	varchar(1)			not null,
	is_active		bit					not null	constraint dc_is_active		default(0),

	constraint pk_questions			primary key(id),
	constraint v_correct_answer		check(correct_answer in('A', 'B', 'C', 'D')),
	constraint fk_cathegory_id		foreign key(cathegory_id)
		references	Cathegories(id),
	constraint fk_difficulty_id		foreign key(difficulty_id)
		references	Difficulties(id),
);

--> create table Titles
create Table Titles
(
	id				int identity(1, 1)	not null,
	title			varchar(30)			not null,
	[description]	varchar(255)		not null,
	icon_url		varchar(50)			not null,

	constraint	pk_titles		primary key(id),
	constraint	u_title			unique(title),
	constraint	u_description	unique([description])
);

--> create table Users
create table Users
(
	username	varchar(30)	not null,
	email		varchar(50)	not null,
	passwd		varchar(50)	not null,

	constraint	pk_users			primary key(username),
	constraint	u_users_username	unique(username),
	constraint	u_email				unique(email)
);

--> create table Players
create table Players
(
	username		varchar(30)	not null,
	[level]			int			not null	constraint	dc_level	default(0),
	score			int			not null	constraint	dc_score	default(0),
	title_id		int			not null,
	profile_picture	varchar(50)	not null,
	[location]		varchar(50)	not null,
	gender			varchar(15)	not null,

	constraint	pk_players				primary key(username),
	constraint	u_players_username		unique(username),
	constraint	v_level					check([level] >= 0),
	constraint	v_score					check(score >= 0),
	constraint	v_gender				check(gender in('Male', 'Female', 'Unspecified')),
	constraint	fk_username				foreign key(username)
		references	Users(username),
	constraint	fk_title_id				foreign key(title_id)
		references	Titles(id)
);

--> create table GameSessions
create table GameSessions
(
	id					int identity(1, 1)	not null,
	question1_id		int					not null,
	question2_id		int					not null,
	question3_id		int					not null,
	question4_id		int					not null,
	question5_id		int					not null,
	questionBonus_id	int					not null,
	datetime_start		datetime			not null,

	constraint	pk_sessions					primary key(id),
	constraint	fk_question1_id				foreign key(question1_id)
		references	Questions(id),
	constraint	fk_question2_id				foreign key(question2_id)
		references	Questions(id),
	constraint	fk_question3_id				foreign key(question3_id)
		references	Questions(id),
	constraint	fk_question4_id				foreign key(question4_id)
		references	Questions(id),
	constraint	fk_question5_id				foreign key(question5_id)
		references	Questions(id),
	constraint	fk_questionBonus_id			foreign key(questionBonus_id)
		references	Questions(id)
);

--> create table Games
create table Games
(
	id					int identity(1, 1)	not null,
	session_id			int					not null,
	username			varchar(30)			not null,
	q1_is_correct		bit					not null	default(0),
	q2_is_correct		bit					not null	default(0),
	q3_is_correct		bit					not null	default(0),
	q4_is_correct		bit					not null	default(0),
	q5_is_correct		bit					not null	default(0),
	qBonus_is_correct	bit					not null	default(0),
	score				int					not null	default(0),

	constraint	pk_game_id			primary key(id),
	constraint	v_game_score		check(score >= 0),
	constraint	fk_session_id		foreign key(session_id)
		references	GameSessions(id),
	constraint	fk_games_username	foreign key(username)
		references	Players(username)
);

--> create table Achievements
create table Achievements
(
	id					int identity(1, 1)	not null,
	achievement_name	varchar(30)			not null,
	[description]		varchar(255)		not null,
	icon_url			varchar(50)			not null,

	constraint	pk_achievemens		primary key(id),
	constraint	u_achievement_name	unique(achievement_name)
);

--> create table AchievementHistory
create table AchievementHistory
(
	id					int identity(1, 1)	not null,
	achievement_id		int					not null,
	username			varchar(30)			not null,
	time_achieved		datetime			not null,

	constraint	pk_achievement_history		primary key(id),
	constraint	fk_achievement_id			foreign key(achievement_id)
		references	Achievements(id),
	constraint	fk_ah_username				foreign key(username)
		references	Players(username)
);

--> create table VersionDB
create table VersionDB
(
	id				int identity(1, 1)	not null,
	current_version	int					not null,

	constraint pk_version_db			primary key(id)
);

insert into VersionDB(current_version) values (1);