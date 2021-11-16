create schema ufoffice;

-- Группы достижений
create table ufoffice.achievement_groups(
	achievement_group_id serial primary key,
	achievement_group_name varchar(500)
);

-- Достижения
create table ufoffice.achievements(
	achievement_id serial primary key,
	ach_name varchar(100),
	ach_desc varchar(250),
	ach_end_point smallint,
	id_achievement_group int,
	attch_image varchar(500)
);

-- Прогресс достижений
create table ufoffice.user_achievements(
	user_achievement_id serial primary key,
	usee_id int,
	achievement_id int,
	progress int,
	ach_status bool
);

-- Типы организаций
create table ufoffice.orgatization_type(
	org_type_id serial primary key,
	org_type_name varchar(200)
);

-- Пользователи
drop table ufoffice.users;
create table ufoffice.users(
	user_id serial primary key,
	username varchar(100) unique,
	user_sex varchar(1),
	user_birthday date,
	user_password varchar(1000),
	user_fio varchar(300),
	user_mail varchar(100),
	user_vk varchar(100),
	user_tg varchar(100),
	user_facebook varchar(100),
	user_role_id int,
	user_rating smallint,
	user_image varchar(1000),
	user_status varchar(200),
	profession_id int
);

-- Профессии
create table ufoffice.professions(
	profession_id serial primary key,
	profession_name varchar(200)
);

-- Организации
create table ufoffice.organizations(
	org_id serial primary key,
	--id_org_owner uniqueidentifier references dev.fct_org_owner(id_org_owner),
	org_type_id int,
	org_name varchar(100),
	legal_entity varchar(150),
	org_desc varchar(300),
	org_image varchar(1500)
);

-- Команды
create table ufoffice.teams(
	team_id serial primary key,
	org_id int,
	team_name varchar(100),
	team_desc varchar(300),
	team_image varchar(1500)
);

-- Команды организаций
create table ufoffice.organization_teams(
	organization_team_id serial primary key,
	org_id int,
	team_id int
);

-- Группы навыков
create table ufoffice.skill_groups(
	skill_group_id serial primary key,
	skill_group_name varchar(100)
);

-- Навыки
create table ufoffice.skills(
	skill_id serial primary key,
	skill_group_id int,
	skill_name varchar(100),
	skill_img varchar(1500)
);

-- Навыки пользователя 
create table ufoffice.user_skills(
	user_skill_id serial primary key,
	user_id int,
	skill_id int
);

-- Календарь
create table ufoffice.dim_calendar(
	date_id serial primary key,
	date_value date,
	day_num int,
	month_num int,
	year_num int,
	month_name varchar(20)
);

-- Статусы задач (список)
create table ufoffice.task_status_name(
	task_status_name_id serial primary key,
	task_status_name varchar(100),
	task_status_sysname varchar(100)
);

-- Задачи
create table ufoffice.tasks(
	task_id serial primary key,
	task_name varchar(200),
	create_dttm timestamp default now(),
	last_upd_dttm timestamp default now(),
	task_desc varchar(1000)
	end_dt date;
	task_status_id int
);

-- Статусы задач
create table ufoffice.task_status(
	task_status_id serial primary key,
	task_status_name_id int,
	task_id int
);

-- Задачи пользователя
create table ufoffice.user_tasks(
	user_task_id serial primary key,
	user_id int,
	task_id int
);

-- Бронирование отпусков
create table ufoffice.vacation_booking(
	vacation_book_id serial primary key,
	user_id int,
	head_user_id int,
	book_status bool,
	date_id int
);

-- Члены организации
create table ufoffice.org_participants(
	org_prt_id serial primary key,
	user_id int,
	org_id int
);

-- Члены команды
create table ufoffice.team_participants(
	team_prt_id serial primary key,
	user_id int,
	team_id int
);

-- Роли пользователей
create table ufoffice.user_roles(
	user_role_id serial primary key,
	user_role_name varchar(100),
	user_role_sysname varchar(100) default 'N/D'
);

create sequence ufoffice.new_notes_seq start 1;

-- Заметки
create table ufoffice.notes(
	note_id serial primary key,
	note_header varchar(500) default 'new note '||nextval('ufoffice.new_notes_seq'),
	note_body varchar(15000),
	user_id int
);
