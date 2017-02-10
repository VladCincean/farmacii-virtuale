-- 10 februarie 2017

use master;

if exists(select * from sys.databases where [name] = 'Exam')
	alter database Exam set single_user with rollback immediate;
	drop database Exam
go

create database Exam;

go

use Exam;

-- 1) Create a relational data model in order to represent the required data. (4 points)

create table DepartureLines
(
	id int identity(1, 1) not null,
	[name] varchar(255) not null,
	[time] datetime not null,

	constraint pk_departure_lines primary key(id),

--	constraint u_departure_lines_name unique([name])
);

create table Gates
(
	id int identity(1, 1) not null,
	[name] varchar(255) not null,
	[time] datetime not null,

	constraint pk_gates primary key(id),

--	constraint u_gates_name unique([name])
);

create table Subways
(
	id int identity(1, 1) not null,
	id_number varchar(25) not null,
	line_id int not null,
	gate_id int not null,

	constraint pk_subways primary key(id),

	constraint fk_subways_departure_lines foreign key(line_id)
		references DepartureLines(id),
	constraint fk_subways_gates foreign key(gate_id)
		references Gates(id),

	constraint u_subways_id_number unique(id_number)
);

create table Stations
(
	id int identity(1, 1) not null,
	[name] varchar(255) not null,

	constraint pk_stations primary key(id),

);

create table Schedule
(
	subway_id int not null,
	station_id int not null,
	nr_passes_per_day int not null,

	constraint fk_schedule_subways foreign key(subway_id)
		references Subways(id),
	constraint fk_schedule_stations foreign key(station_id)
		references Stations(id),

	constraint pk_schedule primary key(subway_id, station_id)
);

--------------------------------------------------------------------

insert into DepartureLines([name], [time]) values
	('DepLine 1', convert(time, '08:00')), -- 1
	('DepLine 2', convert(time, '08:30')), -- 2
	('DepLine 3', convert(time, '09:00')), -- 3
	('DepLine 4', convert(time, '09:30')), -- 4
	('DepLine 5', convert(time, '10:00')), -- 5
	('DepLine 6', convert(time, '10:30')), -- 6
	('DepLine 7', convert(time, '11:00')), -- 7
	('DepLine 8', convert(time, '11:30')), -- 8
	('DepLine 9', convert(time, '12:00')), -- 9
	('DepLine 10', convert(time, '12:30')), -- 10
	('DepLine 11', convert(time, '13:00')), -- 11
	('DepLine 12', convert(time, '13:30')), -- 12
	('DepLine 13', convert(time, '08:00')), -- 13
	('DepLine 14', convert(time, '08:30')), -- 14
	('DepLine 15', convert(time, '09:00')), -- 15
	('DepLine 16', convert(time, '09:30')), -- 16
	('DepLine 17', convert(time, '10:00')), -- 17
	('DepLine 18', convert(time, '10:30')); -- 18

insert into Gates([name], [time]) values
	('Gate 1', convert(time, '08:00')), -- 1
	('Gate 2', convert(time, '08:30')), -- 2
	('Gate 3', convert(time, '09:00')), -- 3
	('Gate 4', convert(time, '09:30')), -- 4
	('Gate 5', convert(time, '10:00')), -- 5
	('Gate 6', convert(time, '10:30')), -- 6
	('Gate 7', convert(time, '11:00')), -- 7
	('Gate 8', convert(time, '11:30')), -- 8
	('Gate 9', convert(time, '12:00')), -- 9
	('Gate 10', convert(time, '12:30')), -- 10
	('Gate 11', convert(time, '13:00')), -- 11
	('Gate 12', convert(time, '13:30')), -- 12
	('Gate 13', convert(time, '08:00')), -- 13
	('Gate 14', convert(time, '08:30')), -- 14
	('Gate 15', convert(time, '09:00')), -- 15
	('Gate 16', convert(time, '09:30')), -- 16
	('Gate 17', convert(time, '10:00')), -- 17
	('Gate 18', convert(time, '10:30')); -- 18

insert into Subways(id_number, line_id, gate_id) values
	('1', 1, 5), -- 1
	('3', 1, 8), -- 2
	('4', 1, 13), -- 3
	('5', 2, 3), -- 4
	('6', 2, 6), -- 5
	('7', 3, 3), -- 6
	('8L', 4, 9), -- 7
	('24B', 12, 17), -- 8
	('25', 7, 3), -- 9
	('49', 2, 9), -- 10
	('100', 3, 5), -- 11
	('120', 18, 14), -- 12
	('7S', 4, 8), -- 13
	('99', 15, 10), -- 14
	('T4', 7, 2), -- 15
	('21', 10, 10), -- 16
	('22', 10, 10), -- 17
	('45', 14, 14); -- 18

insert into Stations([name]) values
	('Station 1'), -- 1
	('Station 2'), -- 2
	('Station 3'), -- 3
	('Station 4'), -- 4
	('Station 5'), -- 5
	('Station 6'), -- 6
	('Station 7'), -- 7
	('Station 8'), -- 8
	('Station 9'), -- 9
	('Station 10'), -- 10
	('Station 11'), -- 11
	('Station 12'), -- 12
	('Station 13'), -- 13
	('Station 14'), -- 14
	('Station 15'), -- 15
	('Station 16'), -- 16
	('Station 17'), -- 17
	('Station 18'); -- 18

insert into Schedule(subway_id, station_id, nr_passes_per_day) values
	(1, 2, 10), (1, 3, 10), (1, 4, 10),
	(2, 1, 4), (2, 2, 4), (2, 4, 1),
	(3, 2, 20), (4, 2, 5), (4, 5, 9),
	(9, 10, 4), (2, 18, 1), (4, 7, 1),
	(10, 12, 4), (11, 14, 15), (12, 18, 3),
	(12, 4, 16), (14, 9, 8), (5, 6, 9),
	(14, 1, 3), (14, 2, 6), (15, 15, 15),
	(16, 16, 16), (9, 9, 9), (9, 18, 12);

--------------------------------------------------------------------

-- 2) Create a stored procedure that add a new schedule for a given subway and station.
-- If the schedule exists, update the times of the passing. (2 points)

go
create procedure add_schedule
	@subway varchar(255),
	@station varchar(255),
	@nr_passes_per_day int
as
begin
	declare @subway_id int;
	declare @station_id int;

	begin transaction;
	begin try
		if @subway is null
			raiserror('Error: subway name is null', 16, 1);
		if @station is null
			raiserror('Error: station name is null', 16, 1);

		if not(exists(select id from Subways where id_number = @subway))
			raiserror('Error: invalid subway name', 16, 1);
		if not(exists(select id from Stations where [name] = @station))
			raiserror('Error: invalid subway name', 16, 1);

		set @subway_id = (select id from Subways where id_number = @subway);
		set @station_id = (select id from Stations where [name] = @station)

		if exists(select subway_id, station_id from Schedule
					where subway_id = @subway_id and station_id = @station_id)
			update Schedule
			set nr_passes_per_day = @nr_passes_per_day
			where subway_id = @subway_id and station_id = @station_id
		else
			insert into Schedule(subway_id, station_id, nr_passes_per_day) values
				(@subway_id, @station_id, @nr_passes_per_day);
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
	end catch
end
go

--------------------------------------------------------------------

-- 3) Create a view that list all subways that have been passed through
-- a station for at least 10 times today. (1 point)

go

create view view_subways_at_least_10
as
	select	Subways.id_number as Subway,
			Stations.[name] as Station,
			Schedule.nr_passes_per_day as [Nr. passes]
	from Subways
	inner join Schedule
		on Subways.id = Schedule.subway_id
	inner join Stations
		on Schedule.station_id = Stations.id
	where Schedule.nr_passes_per_day >= 10;
go

--------------------------------------------------------------------

-- 4) Create a function that list all the lines and gates and the time, where the duration
-- from the line to the gate of the subways is no longer than 30 minutes.

go

create function f_lines_and_gates()
returns table
as
	return
		select	DepartureLines.[name] as [Departure Line],
				Gates.[name] as [Gate],
				datediff(mi, DepartureLines.[time], Gates.[time]) as [Difference of time]
		from DepartureLines
		inner join Subways
			on DepartureLines.id = Subways.line_id
		inner join Gates
			on Subways.gate_id = Gates.id
		where datediff(mi, DepartureLines.[time], Gates.[time]) < 30