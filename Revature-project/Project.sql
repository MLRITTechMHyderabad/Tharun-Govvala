create database Youtube_data;
use Youtube_data;
drop table if exists data_set;
create table data_set(Channel_Name varchar(225),Youtuber_Name varchar(225),Total_Videos int,Best_Video varchar(225),
	Avg_Video_Length_min float ,Total_Subscribers int,Members_Count int,AI_Generated_Content_ int,
    Neural_Interface_Compatible boolean ,Metaverse_Integration_Level varchar(225),
    Quantum_Computing_Topics int,Holographic_Content_Rating varchar(225),Engagement_Score float,
    Content_Value_Index float);
    select * from data_set  limit 5;
    
    