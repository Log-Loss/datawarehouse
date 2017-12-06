create table comments
(
	id int auto_increment
		primary key,
	productId varchar(20) null,
	userId varchar(20) null,
	profileName varchar(100) null,
	helpfulCnt int null,
	rateCnt int null,
	score int null,
	time int null,
	summary varchar(200) null,
	text varchar(20000) null
)
;

create table products
(
	productId varchar(20) null
)
;

create table users
(
	userId varchar(20) not null
		primary key,
	profileName varchar(100) null
)
;

